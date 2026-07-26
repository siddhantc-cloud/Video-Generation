#!/usr/bin/env node

import { createHash } from "node:crypto";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, relative, resolve } from "node:path";
import { spawnSync } from "node:child_process";

const argv = process.argv.slice(2);
const flag = (name, fallback = null) => {
  const index = argv.indexOf(`--${name}`);
  return index >= 0 && index + 1 < argv.length ? argv[index + 1] : fallback;
};
const fail = (message) => {
  console.error(`ElevenLabs narration failed: ${message}`);
  process.exit(1);
};
const round = (value) => Number(value.toFixed(3));
const sha256 = (buffer) => createHash("sha256").update(buffer).digest("hex");

const projectDir = resolve(flag("project", "."));
const scriptPath = resolve(flag("script", join(projectDir, "SCRIPT.md")));
const outDir = resolve(flag("out-dir", join(projectDir, "assets/audio/voice")));
const audioMetaPath = resolve(flag("audio-meta", join(projectDir, "audio_meta.json")));
const voiceId = flag("voice-id", "cgSgspJ2msm6clMCkdW9");
const voiceName = flag("voice-name", "Jessica - Playful, Bright, Warm");
const modelId = flag("model", "eleven_multilingual_v2");
const apiKey = process.env.ELEVENLABS_API_KEY;

if (!apiKey) fail("ELEVENLABS_API_KEY is not available in the process environment");

const parseLines = (markdown) => {
  const lines = [];
  let current = null;
  const flush = () => {
    if (current?.text.trim()) lines.push({ frame: current.frame, text: current.text.trim() });
  };
  for (const line of markdown.split(/\r?\n/)) {
    const heading = line.match(/^##\s+Line\s+\d+.*?\(Frame\s+(\d+)\)/i);
    if (heading) {
      flush();
      current = { frame: Number(heading[1]), text: "" };
      continue;
    }
    if (!current) continue;
    const spoken = line.match(/^(?: {4,}|\t)(.+)$/);
    if (spoken) current.text += `${current.text ? " " : ""}${spoken[1].trim()}`;
  }
  flush();
  return lines;
};

const lines = parseLines(readFileSync(scriptPath, "utf8"));
if (!lines.length) fail(`no spoken lines found in ${scriptPath}`);

const separator = "\n\n";
const text = lines.map((line) => line.text).join(separator);
const offsets = [];
let cursor = 0;
for (const line of lines) {
  offsets.push({ start: cursor, end: cursor + line.text.length - 1 });
  cursor += line.text.length + separator.length;
}

console.log(
  `Submitting one authorized ElevenLabs request: ${text.length} characters, ${lines.length} frames, voice "${voiceName}".`,
);

const response = await fetch(
  `https://api.elevenlabs.io/v1/text-to-speech/${encodeURIComponent(voiceId)}/with-timestamps?output_format=mp3_44100_128`,
  {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "xi-api-key": apiKey,
    },
    body: JSON.stringify({
      text,
      model_id: modelId,
      voice_settings: {
        stability: 0.45,
        similarity_boost: 0.75,
        style: 0.35,
        use_speaker_boost: true,
      },
    }),
  },
);

if (!response.ok) {
  const detail = await response.text();
  fail(`HTTP ${response.status}: ${detail.slice(0, 500)}`);
}

const requestId = response.headers.get("request-id") ?? response.headers.get("x-request-id");
const payload = await response.json();
// The normalized stream can expand brand terms (for example "CryptoPack" to
// "Crypto Pack"). Prefer the raw stream so character offsets remain identical
// to the submitted copy; retain normalized alignment only as a fallback.
const alignment = payload.alignment ?? payload.normalized_alignment;
if (!payload.audio_base64 || !alignment?.characters?.length) {
  fail("provider response did not contain audio and timestamp alignment");
}

const alignedText = alignment.characters.join("");
if (alignedText !== text) {
  fail("provider alignment text differs from the submitted script; refusing unsafe timing inference");
}

mkdirSync(outDir, { recursive: true });
const masterBuffer = Buffer.from(payload.audio_base64, "base64");
const masterPath = join(outDir, "narration-v001-provider-master.mp3");
const alignmentPath = join(outDir, "narration-v001-alignment.json");
writeFileSync(masterPath, masterBuffer);
writeFileSync(
  alignmentPath,
  JSON.stringify(
    {
      characters: alignment.characters,
      character_start_times_seconds: alignment.character_start_times_seconds,
      character_end_times_seconds: alignment.character_end_times_seconds,
    },
    null,
    2,
  ),
);

const starts = alignment.character_start_times_seconds;
const ends = alignment.character_end_times_seconds;
const lastAudioEnd = ends.at(-1);
const voices = [];
const segmentMetadata = [];

for (let index = 0; index < lines.length; index++) {
  const line = lines[index];
  const bounds = offsets[index];
  const segmentStart = Math.max(0, starts[bounds.start] - 0.06);
  const nextSpeechStart =
    index + 1 < lines.length ? starts[offsets[index + 1].start] : lastAudioEnd + 0.8;
  const segmentEnd =
    index + 1 < lines.length
      ? Math.max(ends[bounds.end] + 0.18, nextSpeechStart - 0.08)
      : lastAudioEnd + 0.8;
  const outputName = `${String(line.frame).padStart(2, "0")}-narration-v001.wav`;
  const outputPath = join(outDir, outputName);

  const ffmpeg = spawnSync(
    "ffmpeg",
    [
      "-hide_banner",
      "-loglevel",
      "error",
      "-y",
      "-ss",
      String(segmentStart),
      "-to",
      String(segmentEnd),
      "-i",
      masterPath,
      "-ac",
      "2",
      "-ar",
      "48000",
      "-c:a",
      "pcm_s24le",
      outputPath,
    ],
    { encoding: "utf8" },
  );
  if (ffmpeg.status !== 0) fail(`ffmpeg split failed for frame ${line.frame}: ${ffmpeg.stderr}`);

  const probe = spawnSync(
    "ffprobe",
    [
      "-v",
      "error",
      "-show_entries",
      "format=duration",
      "-of",
      "csv=p=0",
      outputPath,
    ],
    { encoding: "utf8" },
  );
  if (probe.status !== 0) fail(`ffprobe failed for frame ${line.frame}: ${probe.stderr}`);
  const duration = round(Number(probe.stdout.trim()));

  const words = [];
  for (const match of line.text.matchAll(/\S+/g)) {
    const startIndex = bounds.start + match.index;
    const endIndex = startIndex + match[0].length - 1;
    words.push({
      id: `f${line.frame}-w${words.length + 1}`,
      text: match[0],
      start: round(starts[startIndex] - segmentStart),
      end: round(ends[endIndex] - segmentStart),
    });
  }

  const relativePath = relative(projectDir, outputPath).replaceAll("\\", "/");
  const outputBuffer = readFileSync(outputPath);
  voices.push({
    frame: line.frame,
    path: relativePath,
    duration_s: duration,
    words,
  });
  segmentMetadata.push({
    frame: line.frame,
    text: line.text,
    source_start_s: round(segmentStart),
    source_end_s: round(segmentEnd),
    duration_s: duration,
    file: relativePath,
    sha256: sha256(outputBuffer),
  });
}

const audioMeta = { bgm: null, voices, sfx: [] };
mkdirSync(dirname(audioMetaPath), { recursive: true });
writeFileSync(audioMetaPath, JSON.stringify(audioMeta, null, 2));

const metadataPath = join(outDir, "narration-v001-metadata.json");
writeFileSync(
  metadataPath,
  JSON.stringify(
    {
      generated_at: new Date().toISOString(),
      provider: "ElevenLabs",
      request_id: requestId,
      voice_id: voiceId,
      voice_name: voiceName,
      model_id: modelId,
      output_format: "mp3_44100_128",
      submitted_characters: text.length,
      submitted_words: text.trim().split(/\s+/).length,
      settings: {
        stability: 0.45,
        similarity_boost: 0.75,
        style: 0.35,
        use_speaker_boost: true,
      },
      source_script: relative(projectDir, scriptPath).replaceAll("\\", "/"),
      provider_master: relative(projectDir, masterPath).replaceAll("\\", "/"),
      provider_master_sha256: sha256(masterBuffer),
      alignment: relative(projectDir, alignmentPath).replaceAll("\\", "/"),
      segments: segmentMetadata,
    },
    null,
    2,
  ),
);

console.log(
  `Narration complete: ${voices.length} frame WAVs, ${round(voices.reduce((sum, voice) => sum + voice.duration_s, 0))}s total.`,
);
