// Spotlight entry for the "@crisxai5: AI & Crypto Expert on X" bounty (Node 22, stdlib only).
//
// The entry is the X post itself. This program validates POST.json at the repository
// root and copies it to the output directory, where the house reads it and then reads
// the post's public counts from X. Nothing written here about the post is scored.
//
// Locally, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

// An X post address: https://x.com/<handle>/status/<digits>, the same on
// twitter.com, with an optional www./mobile. prefix or /i/web/ segment.
const POST_URL = /^https:\/\/(?:www\.|mobile\.)?(?:x\.com|twitter\.com)\/(?:i\/web\/)?[A-Za-z0-9_]+\/status\/\d+(?:[?#].*)?$/;

function fail(message: string): never {
  console.error(`POST.json: ${message}`);
  process.exit(1);
}

let raw: string;
try {
  raw = readFileSync(join(BOT_DIR, 'POST.json'), 'utf8');
} catch (err) {
  fail(`could not be read: ${(err as Error).message}`);
}

let post: { url?: unknown };
try {
  post = JSON.parse(raw);
} catch {
  fail('is not valid JSON');
}

if (typeof post.url !== 'string' || post.url.length === 0) {
  fail('must be a JSON object with a non-empty "url" string');
}
// "PENDING" is the pre-post placeholder: valid to copy, refused by the gate
// until the real post address replaces it.
if (post.url !== 'PENDING' && !POST_URL.test(post.url)) {
  fail(`"url" is not an X post address: ${post.url}`);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(join(BOT_DIR, 'POST.json'), join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  fail(`could not be copied to the output directory: ${(err as Error).message}`);
}
