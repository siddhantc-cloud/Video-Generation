// AI-composed cheerful comedic cartoon music bed (license-clean, self-generated).
// Melody + bass + kick + offbeat hat, I–V–vi–IV in C major, ~120 BPM. Tiled to TARGET sec.
// Run: bun synth_music.js  (writes music.wav)
const SR = 44100, BPM = 120, beat = 60 / BPM, TARGET = 52;
const semis = (n) => 440 * Math.pow(2, (n - 9) / 12); // n=0 -> C4
// note names -> semitone index from C4
const N = { 'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11,'C5':12,'D5':14,'E5':16,'F5':17,'G5':19,'A5':21,'rest':null };
// 8-bar melody (each entry = [note, beats]) — bouncy, cheerful
const melody = [
  ['G',0.5],['A',0.5],['C5',1],['E5',1],['D5',1],          // bar1-2
  ['C5',0.5],['A',0.5],['G',1],['rest',1],['E',1],          // bar3-4
  ['F',0.5],['G',0.5],['A',1],['C5',1],['A',1],             // bar5-6
  ['G',1],['E',1],['C',1],['rest',1],                       // bar7-8
];
// bass: root of each bar's chord (C, G, Am, F) x2 cycles -> 8 bars
const chordRoots = ['C','C','G','G','A','A','F','F'].map(c => semis(N[c]) / 2); // octave down-ish
const total = Math.floor(TARGET * SR);
const buf = new Float32Array(total);
const env = (t, dur, a=0.01, r=0.06) => {
  if (t < a) return t / a;
  if (t > dur - r) return Math.max(0, (dur - t) / r);
  return 1;
};
// --- melody track (looped) ---
const melodyDur = melody.reduce((s, m) => s + m[1] * beat, 0);
function renderMelody(offset) {
  let t0 = offset;
  for (const [note, b] of melody) {
    const dur = b * beat;
    if (note !== 'rest' && N[note] !== null && N[note] !== undefined) {
      const f = semis(N[note]);
      for (let i = 0; i < dur * SR; i++) {
        const tt = i / SR, gi = Math.floor((t0 + tt) * SR);
        if (gi >= total) break;
        // square+sine blend for a bright but soft lead
        const s = 0.6 * Math.sin(2*Math.PI*f*tt) + 0.25 * Math.sign(Math.sin(2*Math.PI*f*tt));
        buf[gi] += 0.16 * s * env(tt, dur);
      }
    }
    t0 += dur;
  }
  return t0;
}
let off = 0; while (off < TARGET) off = renderMelody(off);
// --- bass + kick + hat over whole duration ---
const barDur = 4 * beat;
for (let gi = 0; gi < total; gi++) {
  const t = gi / SR;
  const bar = Math.floor(t / barDur) % 8;
  const fb = chordRoots[bar];
  const tb = t % barDur;
  // bass: note on each beat
  const inBeat = tb % beat;
  buf[gi] += 0.18 * Math.sin(2*Math.PI*fb*t) * env(inBeat, beat, 0.005, 0.08);
  // kick: beats 0 and 2
  const beatIdx = Math.floor(tb / beat);
  if ((beatIdx === 0 || beatIdx === 2)) {
    const kt = tb - beatIdx*beat;
    if (kt < 0.12) buf[gi] += 0.5 * Math.sin(2*Math.PI*(80 - 200*kt)*kt) * Math.exp(-28*kt);
  }
  // hat: offbeats
  const ht = tb % (beat/1) ;
  const hpos = tb - Math.floor(tb/(beat/2))*(beat/2);
  if (Math.floor(tb/(beat/2)) % 2 === 1 && hpos < 0.04) {
    buf[gi] += 0.06 * (Math.random()*2-1) * Math.exp(-120*hpos);
  }
}
// normalize / soft clip
let peak = 0; for (let i=0;i<total;i++) peak = Math.max(peak, Math.abs(buf[i]));
const g = peak > 0 ? 0.85/peak : 1;
const bytes = Buffer.alloc(44 + total*2);
bytes.write('RIFF',0); bytes.writeUInt32LE(36+total*2,4); bytes.write('WAVE',8);
bytes.write('fmt ',12); bytes.writeUInt32LE(16,16); bytes.writeUInt16LE(1,20);
bytes.writeUInt16LE(1,22); bytes.writeUInt32LE(SR,24); bytes.writeUInt32LE(SR*2,28);
bytes.writeUInt16LE(2,32); bytes.writeUInt16LE(16,34); bytes.write('data',36); bytes.writeUInt32LE(total*2,40);
for (let i=0;i<total;i++){ let v = Math.max(-1,Math.min(1, buf[i]*g)); bytes.writeInt16LE((v*32767)|0, 44+i*2); }
require('fs').writeFileSync('music.wav', bytes);
console.log('wrote music.wav', (total/SR).toFixed(1)+'s');
