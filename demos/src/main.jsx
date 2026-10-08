import React, {useEffect, useRef, useState} from 'react';
import {createRoot} from 'react-dom/client';
import {TimelineSequence} from 'react-timeline-sequence';
import 'react-timeline-sequence/styles.css';
import {createDanceMoves} from '@kieransimkin/dancemoves';
import {bindNative, catalogue, sample} from '@kieransimkin/dance-rudiments';
import createDanceRudiments from '@kieransimkin/dance-rudiments/wasm';
import './style.css';

const WEBSITE='https://kieransimkin.co.uk/danceflow/';
const AUDIO='./media/arcadians.mp3';
let nativePromise;
const WASM_URL=new URL('../node_modules/@kieransimkin/dance-rudiments/dist/wasm/dancerudiments.wasm',import.meta.url).href;
function loadPatterns(){return nativePromise ||= createDanceRudiments({locateFile:()=>WASM_URL}).then(bindNative);}

function MotionDemo({song,patterns=false}){
  const root=useRef(null), audio=useRef(null), chosen=useRef('circle');
  const [status,setStatus]=useState('Preparing the released runtime…');
  const [pattern,setPattern]=useState('circle'),[filter,setFilter]=useState('');
  const handles=useRef(null);
  useEffect(()=>{
    let disposed=false;
    const motion=createDanceMoves({root:root.current,bpm:song.bpm,diagnostics:true});
    Promise.all([motion.ready,loadPatterns()]).then(()=>{
      if(disposed)return;
      const token=root.current.querySelector('.motion-token'),state=root.current.querySelector('.motion-state'),section=root.current.querySelector('.current-section');
      let quality;
      const cue=motion.effects.cueTimeline({id:'demo:clock',root:root.current,audio:audio.current,
        cues:song.sections.map((x,i)=>({id:String(i),time:x.start,end:x.end,data:{label:x.label}})),render(s){
          const minimal=quality?.snapshot().index===2;
          const active=s.playing&&s.reason==='frame'&&!minimal&&!s.reducedMotion&&!s.forcedColours;
          const pip=Math.floor(s.time*song.bpm/60*64);
          const offset=sample(chosen.current,active?pip:0);
          token.style.transform=`translate(${offset.x*64}px,${offset.y*24}px)`;
          state.textContent=active?`Media ${s.time.toFixed(2)} s · pip ${pip}`:`Static pose · ${s.reason}`;
          section.textContent=s.active[0]?.data?.label || 'Arcadians';
        }});
      quality=motion.effects.quality({id:'demo:quality',root:root.current,render(s){root.current.dataset.quality=s.tier;cue.restore('quality-change');}});
      handles.current={motion,cue,quality};
      setStatus(`DanceMoves 3.1.15 + DanceRudiments 0.2.3 · ${catalogue.length} native patterns`);
    }).catch(error=>setStatus(error.message));
    return()=>{disposed=true;handles.current=null;motion.destroy();};
  },[song]);
  const selected=catalogue.find(x=>x.name===pattern);
  return <section ref={root} className="panel motion-demo"><h2>{patterns?'DanceRudiments':'DanceMoves'}</h2><p>{status}</p>
    {patterns&&<><label>Find a native movement <input value={filter} onChange={e=>setFilter(e.target.value)} placeholder="Try amen, circle or club"/></label><label>Pattern <select value={pattern} onChange={e=>{chosen.current=e.target.value;setPattern(e.target.value);handles.current?.cue.restore('pattern-change');}}>{catalogue.filter(x=>x.name===pattern||`${x.name} ${x.description}`.toLowerCase().includes(filter.toLowerCase())).map(x=><option key={x.name} value={x.name}>{x.name}</option>)}</select></label><p>{selected?.description} · {selected?.periodPips/64} beat cycle · 64 integer pips per beat</p></>}
    <div className="motion-stage"><div className="motion-token" aria-hidden="true">♪</div></div><p className="current-section">Arcadians</p><p className="motion-state">Static pose</p>
    <audio ref={audio} src={AUDIO} controls preload="metadata" data-dance-moves-master/><div className="buttons"><button onClick={()=>audio.current.play()}>Play Arcadians</button><button onClick={()=>audio.current.pause()}>Pause audio</button><button onClick={()=>{audio.current.currentTime=104.01;}}>Seek to Drop 1</button><button onClick={()=>handles.current?.quality.setTier(2,'demo-choice')}>Minimal quality</button><button onClick={()=>handles.current?.quality.setTier(0,'demo-choice')}>Restore quality</button><button onClick={()=>{handles.current?.motion.destroy();handles.current=null;setStatus('Runtime disposed; audio remains available');}}>Dispose effects</button></div>
    <p className="fine">Arcadians · Kieran Simkin · supplied 145 BPM. The native sampler uses actual media time; its grid does not claim inferred downbeat alignment. One 96 px subject stays within ±64 px horizontally and ±24 px vertically. DanceMoves owns playback, seeking, visibility, preferences, quality and teardown. Tilt, particles and intermittent accents are omitted from this focused demo.</p></section>;
}

function EvidenceDemo(){
  const [result,setResult]=useState(null),[filter,setFilter]=useState(''),[error,setError]=useState('');
  useEffect(()=>{fetch('./keywordmoves-example.json').then(x=>{if(!x.ok)throw Error('Evidence could not load');return x.json();}).then(setResult).catch(x=>setError(x.message));},[]);
  const words=result?.keywords?.filter(x=>x.phrase.toLowerCase().includes(filter.toLowerCase()))||[];
  return <section className="panel"><h2>KeywordMoves</h2><p>Explore actual <code>extract-literal</code> output from the canonical Arcadians lyrics. Occurrence counts describe this source text; they are not search volume. This static demo filters a saved tool result.</p><label>Filter phrases <input disabled={!result} value={filter} onChange={e=>setFilter(e.target.value)} placeholder="Try wild"/></label><p role="status">{error||(result?`${words.length} matching phrases`:'Loading phrase evidence…')}</p><div className="phrases">{words.slice(0,32).map(x=><span key={x.phrase}>{x.phrase}<b>{x.evidence[0].value}</b></span>)}</div><a href="./keywordmoves-example.json" download>Download the complete result JSON</a> · <a href="./media/lyrics.txt">Source lyrics</a></section>;
}

function App(){
  const [tab,setTab]=useState('timeline'),[song,setSong]=useState(null),[error,setError]=useState('');
  useEffect(()=>{fetch('./arcadians.json').then(x=>{if(!x.ok)throw Error('Arcadians could not load');return x.json();}).then(setSong).catch(x=>setError(x.message));},[]);
  const lanes=song?[{id:'wave',title:'Arcadians waveform',meta:'StemLab · 44.1 kHz',content:{type:'waveform',min:song.waveform.min,max:song.waveform.max}},{id:'sections',title:'Artist sections',content:{type:'blocks',items:song.sections}},{id:'lyrics',title:'Canonical lyrics',content:{type:'blocks',items:song.lyrics.map(x=>({...x,label:x.text}))}}]:[];
  const loops=song?song.sections.filter(x=>['Verse 1','Drop 1'].includes(x.label)).map(x=>({id:x.label,label:`Audition ${x.label}`,startSample:Math.round(x.start*44100),endSample:Math.round(x.end*44100),sampleRate:44100})):[];
  return <><header><a href={WEBSITE}>Kieran Simkin · DanceFlow</a><span>Public playground</span></header><main><h1>Explore the tools.<br/><em>Keep the evidence.</em></h1><p className="intro">Music, motion and media tools for people and agents. Start with Arcadians, try the released engines, and use the source and agent guides to build something of your own.</p><div className="track-card"><img src="./media/cover.jpg" alt="Official Arcadians cover artwork"/><div><strong>Arcadians</strong><p>Kieran Simkin · 145 BPM · released 25 September 2026</p><a href="https://kieransimkin.co.uk/arcadians/">Listen and explore the song</a> · <a href="./provenance.json">Example source and hashes</a></div></div><nav aria-label="Choose a demo">{[['timeline','Audio timeline'],['motion','Web motion'],['patterns','Movement patterns'],['keywords','Keyword evidence'],['tools','All tools']].map(([key,label])=><button key={key} aria-pressed={tab===key} onClick={()=>setTab(key)}>{label}</button>)}</nav>
  {!song&&<p role="status">{error||'Loading the Arcadians reference…'}</p>}
  {tab==='timeline'&&song&&<section className="panel"><h2>StemLab + React Timeline Sequence</h2><p>Play, seek, zoom and audition a section of Arcadians. The waveform comes from StemLab; sections and lyric timing are supplied artist references. One shared transport keeps every lane on the same timeline.</p><div className="timeline"><TimelineSequence audioSrc={AUDIO} duration={song.duration} title="Arcadians · Kieran Simkin · 145 BPM" lanes={lanes} loops={loops}/></div><p className="fine">Audition ranges use source sample frames at 44.1 kHz. They demonstrate looping controls; musical seam acceptance has not been established. MP3 decoding can include encoder padding.</p></section>}
  {(tab==='motion'||tab==='patterns')&&song&&<MotionDemo key={tab} song={song} patterns={tab==='patterns'}/>}
  {tab==='keywords'&&<EvidenceDemo/>}
  {tab==='tools'&&<section className="panel"><h2>The full ecosystem</h2><p>Each component has a portable skill, source link and contribution guide. Install the tools and models your task needs.</p><div className="tool-grid">{[['StemLab','stemlab','Music analysis, stems, timing and loops'],['DanceRudiments','dancerudiments','Deterministic rhythmic patterns'],['DanceMoves','dancemoves','Web clocks, effects and lifecycle'],['KeywordMoves','keywordmoves','Source-specific keyword evidence'],['RasterMoves','rastermoves','Local image upscaling'],['PixelCue','pixelcue','Local visual-media tagging'],['ThumbMoves','thumbmoves','Cache-only thumbnails'],['React Timeline Sequence','react-timeline-sequence','Shared audio transport and loops'],['EPK Social Metadata','epk-social-metadata','WordPress sharing metadata'],['DanceVault','dancevault','Experimental encrypted delivery']].map(([title,id,role])=><a key={id} href={`https://github.com/kieransimkin/DanceFlow/blob/main/docs/tools/${id}.md`}><strong>{title}</strong><span>{role}</span></a>)}</div><p className="fine">DanceVault hosting acceptance is pending.</p></section>}
  <section className="contribute"><h2>Use it. Improve it. Share a tested contribution.</h2><p>Inspect available features, start with a small reproducible example, and open a focused pull request.</p><a href="https://github.com/kieransimkin/DanceFlow">Install the agent toolkit</a><a href="https://github.com/kieransimkin/DanceFlow/issues">Find a contribution</a></section></main><footer><a href="https://kieransimkin.co.uk/">Kieran Simkin's website</a><a href={WEBSITE}>DanceFlow ecosystem</a><a href="https://github.com/kieransimkin/DanceFlow">Source and contribution guides</a><a href="./licences/DanceMoves.txt">Demo software licences</a></footer></>;
}

createRoot(document.getElementById('root')).render(<App/>);
