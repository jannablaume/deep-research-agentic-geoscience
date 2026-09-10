/**
 * Rewrite absolute asset URLs in the built output to relative ones.
 *
 * The built site is meant to open by double-clicking `index.html`, with no
 * server anywhere. Astro emits `/assets/…` regardless of `base` (every value
 * of it produces something absolute), and an absolute path resolves against
 * the filesystem root when the page is opened as a file — so the page renders
 * unstyled and inert, but only for the person you sent it to, because it works
 * perfectly over `http://localhost`.
 *
 * Single page, single directory level, so a relative path is always `./`.
 */
import { readdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';

const DIST = new URL('../dist/', import.meta.url).pathname;

// Only inside an attribute, so a `/assets/` appearing in page text — or inside
// the JSON blob of run data compiled into the page — is left alone.
const ABSOLUTE_ASSET = /(\s(?:src|href)=")\/+(\.\/)*assets\//g;

// Stylesheets have the same problem in a different syntax: Vite rewrites a
// relative `url(...)` in CSS to an absolute `/assets/...`. A stylesheet in
// `assets/` sits beside what it references, so the relative form is the bare
// filename.
const ABSOLUTE_CSS_URL = /url\(\/+(?:\.\/)*assets\//g;

const entries = await readdir(DIST, { recursive: true });
let rewritten = 0;
let scanned = 0;

for (const file of entries) {
  const isHtml = file.endsWith('.html');
  const isCss = file.endsWith('.css');
  if (!isHtml && !isCss) continue;

  scanned += 1;
  const path = join(DIST, file);
  const before = await readFile(path, 'utf8');
  const after = isHtml
    ? before.replace(ABSOLUTE_ASSET, '$1./assets/')
    : before.replace(ABSOLUTE_CSS_URL, 'url(');
  if (after !== before) {
    await writeFile(path, after);
    rewritten += 1;
  }
}

console.log(`relativised asset URLs in ${rewritten}/${scanned} file(s)`);
