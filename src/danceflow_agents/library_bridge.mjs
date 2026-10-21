/** Fixed adapter for installed public APIs. Inputs are JSON data, never JavaScript. */
import {createRequire} from 'node:module';
import {readFileSync, realpathSync} from 'node:fs';
import path from 'node:path';

const MAX_INPUT = 1024 * 1024;
const MAX_RESULT = 4 * 1024 * 1024;
const packages = Object.freeze({
  dancemoves: '@kieransimkin/dancemoves',
  'react-timeline-sequence': 'react-timeline-sequence',
});
const allowed = Object.freeze({
  dancemoves: ['validate_page_config', 'validate_timing_file', 'validate_motion_capture'],
  'react-timeline-sequence': ['validate_beat_clock', 'sample_beat_clock', 'match_beat', 'beat_grid', 'lyric_state'],
});
const inside = (parent, child) => {
  const relative = path.relative(parent, child);
  return relative !== '..' && !relative.startsWith('..' + path.sep) && !path.isAbsolute(relative);
};
function api(library, name) {
  if (typeof library[name] !== 'function') throw new Error(`Installed package lacks required API ${name}; install a compatible released version`);
  return library[name];
}

async function main() {
  let text = '';
  for await (const chunk of process.stdin) {
    text += chunk.toString('utf8');
    if (Buffer.byteLength(text) > MAX_INPUT + 4096) throw new RangeError('Library input exceeds one MiB');
  }
  const {component, operation, arguments: args} = JSON.parse(text);
  if (!Object.hasOwn(packages, component) || !allowed[component].includes(operation)) throw new Error('Unsupported fixed library operation');
  const workspace = realpathSync(process.argv[2]);
  const name = packages[component];
  const root = realpathSync(path.join(workspace, 'node_modules', name));
  if (!inside(workspace, root)) throw new Error('Node package resolves outside the selected workspace');
  const manifestPath = realpathSync(path.join(root, 'package.json'));
  if (!inside(root, manifestPath)) throw new Error('Package metadata resolves outside its package');
  const manifest = JSON.parse(readFileSync(manifestPath, 'utf8'));
  if (manifest.name !== name) throw new Error('Package identity does not match the fixed adapter');
  const node = process.versions.node.split('.').map(Number);
  if (component === 'dancemoves' && (node[0] < 22 || (node[0] === 22 && node[1] < 14))) throw new Error('DanceMoves requires Node 22.14 or later');
  if (component === 'react-timeline-sequence' && node[0] < 20) throw new Error('React Timeline Sequence requires Node 20 or later');
  const require = createRequire(path.join(workspace, 'package.json'));
  const specifier = component === 'dancemoves' && operation !== 'validate_page_config' ? name + '/server' : name;
  const entry = realpathSync(require.resolve(specifier));
  if (!inside(root, entry)) throw new Error('Resolved module is outside the selected installed package');
  // Library diagnostics are not part of the JSON result or the MCP wire stream.
  console.log = console.info = (...values) => console.error(...values);
  const library = require(entry);
  let result;
  if (component === 'dancemoves') {
    if (operation === 'validate_page_config') result = api(library, 'validatePageConfig')(args.config);
    if (operation === 'validate_timing_file') result = api(library, 'validateTimingFile')(args.text, {
      kind: args.kind ?? 'cue', filename: args.filename, maxBytes: MAX_INPUT,
    });
    if (operation === 'validate_motion_capture') result = api(library, 'validateMotionCapture')(args.capture);
  } else {
    if (operation !== 'lyric_state') api(library, 'validateBeatClock')(args.clock);
    if (operation === 'validate_beat_clock') result = args.clock;
    if (operation === 'sample_beat_clock') {
      const phase = api(library, 'phasePipsAt'), tempo = api(library, 'tempoAtSeconds');
      const seconds = api(library, 'secondsAtPips');
      result = {
        at_seconds: args.seconds.map(value => ({seconds: value, pips: phase(args.clock, value), bpm: tempo(args.clock, value)})),
        at_pips: (args.pips ?? []).map(value => ({pips: value, seconds: seconds(args.clock, value)})),
      };
    }
    if (operation === 'match_beat') result = api(library, 'matchBeat')(args.clock, args.seconds, args.tolerance_seconds ?? .15);
    if (operation === 'beat_grid') result = api(library, 'beatGrid')(args.clock, args.start, args.end, args.limit ?? 2000);
    if (operation === 'lyric_state') result = api(library, 'lyricLineStatesAtTime')(args.lines, args.words ?? [], args.seconds, args.duration);
  }
  const response = JSON.stringify({status: 'ok', runtime: {package: name, version: manifest.version ?? null,
    node: process.versions.node, entry, api_checked: true}, result}, (_key, value) => {
      if (typeof value === 'number' && !Number.isFinite(value)) throw new RangeError('Native library returned a non-finite number');
      return value;
    });
  if (Buffer.byteLength(response) > MAX_RESULT) throw new RangeError('Native library result exceeds four MiB');
  process.stdout.write(response);
}

main().catch(error => {
  process.stdout.write(JSON.stringify({status: 'error', error: {
    name: String(error?.name ?? 'NativeLibraryError').slice(0, 100),
    message: String(error?.message ?? error).slice(0, 2000),
    code: typeof error?.code === 'string' ? error.code.slice(0, 100) : undefined,
  }}));
  process.exitCode = 1;
});
