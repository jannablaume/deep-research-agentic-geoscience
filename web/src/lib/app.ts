/**
 * Filtering, the source record, the evidence-tag filter, and the nav.
 *
 * One filter state drives the list and the counts above it, so they cannot
 * disagree about what is selected. Everything else here is a small piece of
 * wiring that exists because the page has to work as a file on somebody's
 * desktop with no server: no fetch, no router, no framework.
 */

import type { EvidenceTag, Paper } from './types';

const papers: Paper[] = (window as unknown as { __PAPERS__?: Paper[] }).__PAPERS__ ?? [];

const $ = <T extends HTMLElement>(id: string) => document.getElementById(id) as T | null;

const controls = {
  q: $<HTMLInputElement>('f-q'),
  tier: $<HTMLSelectElement>('f-tier'),
  field: $<HTMLSelectElement>('f-field'),
  arch: $<HTMLSelectElement>('f-arch'),
  tech: $<HTMLSelectElement>('f-tech'),
  framework: $<HTMLSelectElement>('f-framework'),
  maturity: $<HTMLSelectElement>('f-maturity'),
  model: $<HTMLSelectElement>('f-model'),
  type: $<HTMLSelectElement>('f-type'),
  journal: $<HTMLSelectElement>('f-journal'),
  country: $<HTMLSelectElement>('f-country'),
  year: $<HTMLSelectElement>('f-year'),
  sort: $<HTMLSelectElement>('f-sort'),
};

const pretty = (s: string) => s.replace(/_/g, ' ');

/** Everything a search should look through — including the numbers. */
function haystack(p: Paper): string {
  return [
    p.title,
    p.system_id,
    p.authors,
    p.venue,
    p.task,
    p.subfield,
    p.subfield_secondary,
    p.architecture,
    p.base_model,
    p.tools_used,
    p.evaluation_method,
    p.baseline,
    p.reported_result,
    p.maturity_claimed,
    p.limitations,
    p.annotation,
    p.techniques.join(' '),
    p.frameworks.join(' '),
    p.model_families.join(' '),
    p.journal,
    p.source_type,
    p.countries.join(' '),
    p.key,
    `#${p.ref}`,
  ]
    .join(' ')
    .toLowerCase();
}

const searchIndex = new Map<string, string>(papers.map((p) => [p.key, haystack(p)]));

const level = (p: Paper): number => {
  const m = /^M([0-5])$/.exec(p.maturity_demonstrated.trim());
  // Unrated sorts below M0 rather than above M5. It is the absence of a
  // rating, not a high one, and 132 of 155 rows carry it — putting them first
  // would bury every system the run actually read.
  return m ? Number(m[1]) : -1;
};

function matches(p: Paper): boolean {
  const c = controls;
  if (c.tier?.value && p.tier !== c.tier.value) return false;
  if (c.field?.value && p.subfield !== c.field.value) return false;
  if (c.arch?.value && p.architecture !== c.arch.value) return false;
  if (c.tech?.value && !p.techniques.includes(c.tech.value)) return false;
  if (c.framework?.value && !p.frameworks.includes(c.framework.value)) return false;
  // Multi-valued: a paper matches if it names the family anywhere in the cell.
  if (c.model?.value && !p.model_families.includes(c.model.value)) return false;
  if (c.type?.value && p.source_type !== c.type.value) return false;
  if (c.journal?.value && p.journal !== c.journal.value) return false;
  if (c.country?.value && !p.countries.includes(c.country.value)) return false;
  if (c.year?.value && String(p.year) !== c.year.value) return false;

  const m = c.maturity?.value;
  if (m === 'rated' && level(p) < 0) return false;
  if (m === 'unrated' && level(p) >= 0) return false;
  if (m && m !== 'rated' && m !== 'unrated' && p.maturity_demonstrated.trim() !== m) return false;

  const q = c.q?.value.trim().toLowerCase();
  if (q && !(searchIndex.get(p.key) ?? '').includes(q)) return false;

  return true;
}

function ordered(rows: Paper[]): Paper[] {
  const mode = controls.sort?.value ?? 'tier';
  return [...rows].sort((a, b) => {
    if (mode === 'maturity') {
      const d = level(b) - level(a);
      if (d !== 0) return d;
    } else if (mode === 'year') {
      const d = (b.year ?? 0) - (a.year ?? 0);
      if (d !== 0) return d;
    } else if (mode === 'field') {
      const d = a.subfield.localeCompare(b.subfield);
      if (d !== 0) return d;
    } else if (mode === 'title') {
      return a.title.localeCompare(b.title);
    } else {
      // Default: the readable systems first, then by what they demonstrated.
      // The tier split is the most important thing about this corpus, so it is
      // the default ordering as well as a filter and a chip.
      if (a.tier !== b.tier) return a.tier === 'core' ? -1 : 1;
      const d = level(b) - level(a);
      if (d !== 0) return d;
    }
    return a.title.localeCompare(b.title);
  });
}

// --- rendering --------------------------------------------------------------

const esc = (s: string) =>
  String(s ?? '').replace(
    /[&<>"']/g,
    (ch) =>
      ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[ch] as string,
  );

/** `not stated` is a recorded silence, so it is set apart rather than hidden. */
const stated = (v: string) => {
  const s = (v ?? '').trim();
  if (!s || /^not stated/i.test(s) || s === 'none') {
    return `<span class="na">${esc(s || 'not stated')}</span>`;
  }
  return esc(s);
};

function pips(value: string): string {
  const m = /^M([0-5])$/.exec(value.trim());
  const on = m ? Number(m[1]) : 0;
  const label = m
    ? `Demonstrated maturity ${value.trim()} of M5`
    : 'No demonstrated maturity: abstract only';
  const cells = Array.from(
    { length: 5 },
    (_, i) => `<span class="pip${m && i < on ? ' on' : ''}"></span>`,
  ).join('');
  return `<span class="pips${m ? '' : ' unrated'}" role="img" aria-label="${esc(label)}" title="${esc(label)}">${cells}</span>`;
}

function drawList(rows: Paper[]): void {
  const list = $<HTMLDivElement>('list');
  const countN = $<HTMLElement>('count-n');
  const countSplit = $<HTMLElement>('count-split');
  if (!list) return;

  const core = rows.filter((p) => p.tier === 'core').length;
  if (countN) countN.textContent = String(rows.length);
  if (countSplit) {
    countSplit.textContent = rows.length
      ? `${core} core, ${rows.length - core} context · of ${papers.length} admitted`
      : `of ${papers.length} admitted`;
  }

  if (rows.length === 0) {
    list.innerHTML =
      '<p class="empty">No source matches those filters. That is a statement about the filters, not about the literature.</p>';
    return;
  }

  list.innerHTML = rows
    .map((p) => {
      const facts = [
        `<span class="chip tier-${p.tier}">${p.tier}</span>`,
        `<span class="chip">${esc(pretty(p.subfield))}</span>`,
        p.architecture && p.architecture !== 'not stated'
          ? `<span class="chip">${esc(p.architecture)}</span>`
          : '',
        ...p.frameworks.slice(0, 3).map((f) => `<span class="chip">${esc(f)}</span>`),
      ]
        .filter(Boolean)
        .join('');

      const maturity = /^M\d$/.test(p.maturity_demonstrated.trim())
        ? `${pips(p.maturity_demonstrated)} <span>${esc(p.maturity_demonstrated.trim())}</span>`
        : `${pips(p.maturity_demonstrated)} <span>not rated</span>`;

      // A system_id of `not stated` is a silence, and a row reading
      // "not stated — automating analysis of well plug documentation" puts the
      // silence where a name should be. Where there is no name, the task
      // stands on its own.
      const named = p.system_id && !/^not stated/i.test(p.system_id);
      const sub = [named ? esc(p.system_id) : '', p.task ? esc(p.task) : '']
        .filter(Boolean)
        .join(' — ');

      return `<button class="row" type="button" data-key="${esc(p.key)}">
        <span>
          <span class="title">${esc(p.title)}</span>
          <span class="sub">${sub}</span>
          <span class="facts">${facts}</span>
        </span>
        <span class="right">
          <span class="ref">${p.ref}</span>
          <span>${p.year ?? '—'}${p.venue ? ` · ${esc(p.venue)}` : ''}</span>
          <span style="display:inline-flex;align-items:center;gap:.35rem">${maturity}</span>
        </span>
      </button>`;
    })
    .join('');
}

// --- the source record ------------------------------------------------------

const dialog = $<HTMLDialogElement>('detail');
const body = $<HTMLDivElement>('detail-body');

function openDetail(key: string): void {
  const p = papers.find((x) => x.key === key);
  if (!p || !dialog || !body) return;

  const grid = [
    ['field', pretty(p.subfield) + (p.subfield_secondary ? ` · ${pretty(p.subfield_secondary)}` : '')],
    ['architecture', p.architecture],
    ['techniques', p.techniques.join(' · ')],
    ['generator model', p.base_model],
    ['model families', p.model_families.join(' · ')],
    ['can call', p.tools_used],
    ['evaluated by', p.evaluation_method],
    ['baseline', p.baseline],
    ['data', p.data_type],
    ['held out', p.held_out],
    ['reported', p.reported_result],
    ['journal or venue', p.journal],
    ['author countries', p.countries.join(', ')],
    ['code', p.code_availability],
  ]
    .map(([k, v]) => `<dt>${esc(k)}</dt><dd>${stated(String(v))}</dd>`)
    .join('');

  // The framework row is separated from the grid above because it is the one
  // derived value on the record, and a derived value sitting in a column of
  // read ones is how a reading becomes a fact.
  const derived = p.frameworks.length
    ? `<section>
        <h4>Frameworks named — derived</h4>
        <div class="chips">${p.frameworks.map((f) => `<span class="chip">${esc(f)}</span>`).join('')}</div>
        <p class="muted" style="margin:.75rem 0 0">Keyword match over the <code>can call</code> cell above, not a schema column.</p>
      </section>`
    : '';

  const claimed =
    p.maturity_claimed && !/^not stated/i.test(p.maturity_claimed)
      ? `<section>
          <h4>Claimed versus demonstrated</h4>
          <dl class="kv">
            <dt>demonstrated</dt><dd>${pips(p.maturity_demonstrated)} ${stated(p.maturity_demonstrated)}</dd>
            <dt>claimed</dt><dd>${esc(p.maturity_claimed)}</dd>
          </dl>
          <p class="muted" style="margin:.75rem 0 0">Demonstrated is rated from the evaluation section only. A gap between the two is itself a finding of the rubric.</p>
        </section>`
      : `<section>
          <h4>Demonstrated maturity</h4>
          <p style="margin:0">${pips(p.maturity_demonstrated)} ${stated(p.maturity_demonstrated)}</p>
        </section>`;

  const limitations = p.limitations && !/^not stated/i.test(p.limitations)
    ? `<section><h4>Limitations, in the authors' terms</h4><p class="muted" style="margin:0;line-height:1.6">${esc(p.limitations)}</p></section>`
    : '';

  // The evidence trail. This is the section that makes the rest of the page
  // checkable: verbatim sentences, and the questions the full text did not
  // answer stated as absences rather than left blank.
  const extract = p.extract
    ? `<section>
        <h4>Verbatim, from the full text</h4>
        <div class="quotes">
          ${p.extract.quotes.map((q) => `<blockquote>“${esc(q)}”</blockquote>`).join('')}
          ${p.extract.not_found
            .map((q) => `<blockquote class="absent">Not found in the full text: ${esc(q)}</blockquote>`)
            .join('')}
        </div>
        <p class="muted" style="margin:.9rem 0 0">
          Read from <a href="${esc(p.extract.source)}" target="_blank" rel="noopener">${esc(p.extract.source)}</a>${
            p.extract.source_note ? ` — ${esc(p.extract.source_note)}` : ''
          }
        </p>
      </section>`
    : `<section>
        <h4>No evidence trail</h4>
        <p class="muted" style="margin:0">Context tier: only an abstract was available, so nothing on this record was checked against an evaluation section and no maturity is rated.</p>
      </section>`;

  body.innerHTML = `
    <div class="chips" style="margin-bottom:1rem">
      <span class="chip tier-${p.tier}">${p.tier}</span>
      <span class="chip">${esc(p.access_status)}</span>
      <span class="chip">${esc(p.source_type)}</span>
      <span class="chip">found via ${esc(p.found_via)}</span>
    </div>
    <h3>${esc(p.title)}</h3>
    <p class="byline">${esc(p.authors)}${p.year ? ` · ${p.year}` : ''}${p.venue ? ` · ${esc(p.venue)}` : ''}</p>
    ${p.task ? `<p class="task">${esc(p.task)}</p>` : ''}
    ${p.annotation ? `<p class="muted" style="margin-top:.75rem">${esc(p.annotation)}</p>` : ''}
    <section>
      <h4>Comparison grid</h4>
      <dl class="kv">${grid}</dl>
    </section>
    ${derived}
    ${claimed}
    ${extract}
    ${limitations}
    <section>
      <h4>Identity</h4>
      <dl class="kv">
        <dt>system</dt><dd>${esc(p.system_id)}</dd>
        <dt>reference</dt><dd>${p.ref}</dd>
        <dt>key</dt><dd><code>${esc(p.key)}</code></dd>
        <dt>source</dt><dd><a href="${esc(p.url)}" target="_blank" rel="noopener">${esc(p.url)}</a></dd>
      </dl>
    </section>`;

  if (!dialog.open) dialog.showModal();
  body.scrollTop = 0;
}

dialog?.addEventListener('click', (event) => {
  // A click on the backdrop lands on the dialog itself, never on its contents.
  if (event.target === dialog) dialog.close();
});
$<HTMLButtonElement>('detail-close')?.addEventListener('click', () => dialog?.close());

// --- CSV of what is on screen ----------------------------------------------

const CSV_COLUMNS: (keyof Paper)[] = [
  'ref',
  'key', 'tier', 'system_id', 'title', 'authors', 'year', 'venue', 'source_type',
  'subfield', 'task', 'architecture', 'base_model', 'tools_used', 'evaluation_method',
  'baseline', 'held_out', 'data_type', 'reported_result', 'maturity_claimed',
  'maturity_demonstrated', 'code_availability', 'access_status', 'found_via', 'journal', 'url',
];

function downloadCsv(rows: Paper[]): void {
  // RFC 4180, every cell quoted, as the output contract requires of every CSV
  // in this repository — so a file exported from the page and a file written by
  // the run parse the same way.
  const cell = (v: unknown) => `"${String(v ?? '').replace(/"/g, '""').replace(/\r?\n/g, '; ')}"`;
  const header = [
    ...CSV_COLUMNS,
    'agentic_techniques',
    'frameworks_derived',
    'model_families',
    'countries',
  ];
  const lines = [
    header.map(cell).join(','),
    ...rows.map((p) =>
      [
        ...CSV_COLUMNS.map((c) => cell(p[c])),
        cell(p.techniques.join('; ')),
        cell(p.frameworks.join('; ')),
        cell(p.model_families.join('; ')),
        cell(p.countries.join('; ')),
      ].join(','),
    ),
  ];
  const blob = new Blob([`﻿${lines.join('\r\n')}\r\n`], {
    type: 'text/csv;charset=utf-8',
  });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `landscape-${rows.length}-sources.csv`;
  a.click();
  URL.revokeObjectURL(a.href);
}

// --- the evidence-tag filter ------------------------------------------------

/**
 * Hide claims by evidence tag, per prose block.
 *
 * A section's `[Likely]` paragraphs are the run's own reading rather than a
 * source's claim, and being able to drop them and re-read what is left is the
 * fastest way to see how much of a section is inference. The buttons start
 * pressed: the default view is the report as written.
 */
function wireTagFilters(): void {
  for (const prose of document.querySelectorAll<HTMLElement>('[data-prose]')) {
    const buttons = prose.querySelectorAll<HTMLButtonElement>('.tagfilter button');
    if (!buttons.length) continue;

    const apply = () => {
      const hidden = new Set<string>();
      buttons.forEach((b) => {
        if (b.getAttribute('aria-pressed') !== 'true') hidden.add(b.dataset.tag ?? '');
      });
      prose.querySelectorAll<HTMLElement>('[data-claim-tag]').forEach((claim) => {
        claim.hidden = hidden.has(claim.dataset.claimTag ?? '');
      });
    };

    buttons.forEach((b) =>
      b.addEventListener('click', () => {
        b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
        apply();
      }),
    );
  }
}

// --- wiring -----------------------------------------------------------------

function render(): void {
  drawList(ordered(papers.filter(matches)));
}

Object.values(controls).forEach((el) => {
  el?.addEventListener(el instanceof HTMLInputElement ? 'input' : 'change', render);
});

$<HTMLButtonElement>('f-reset')?.addEventListener('click', () => {
  Object.values(controls).forEach((el) => {
    if (el instanceof HTMLInputElement) el.value = '';
    else if (el instanceof HTMLSelectElement) el.selectedIndex = 0;
  });
  render();
});

$<HTMLButtonElement>('f-csv')?.addEventListener('click', () => {
  downloadCsv(ordered(papers.filter(matches)));
});

/**
 * One listener for everything that opens a record.
 *
 * Rows, citations inside report prose, and the system chips in the fields
 * table all do the same thing, and all three are either re-rendered or
 * numerous. Delegation means the citation buttons compiled into the page by
 * Astro need no wiring of their own.
 */
document.addEventListener('click', (event) => {
  const target = event.target as HTMLElement | null;
  const trigger = target?.closest<HTMLElement>('[data-key],[data-cite],[data-system]');
  if (!trigger) return;

  const key = trigger.dataset.key ?? trigger.dataset.cite;
  if (key) {
    openDetail(key);
    return;
  }

  // A system id can be shared by several sources on the same system; the
  // first core row is the one with the full text behind it.
  const system = trigger.dataset.system;
  if (system) {
    const p = papers.find((x) => x.system_id === system && x.tier === 'core')
      ?? papers.find((x) => x.system_id === system);
    if (p) openDetail(p.key);
  }
});

/**
 * The theme control.
 *
 * The page follows the reader's OS setting by default and only stamps
 * `data-theme` once they choose otherwise — so the first visit inherits their
 * preference and a later visit remembers their override. Every storage access
 * is guarded: a browser set to block site data throws on the accessor itself,
 * and a page that cannot remember a theme must still render in one.
 */
const themeButton = $<HTMLButtonElement>('theme');
themeButton?.addEventListener('click', () => {
  const root = document.documentElement;
  const dark = root.dataset.theme
    ? root.dataset.theme === 'dark'
    : window.matchMedia('(prefers-color-scheme: dark)').matches;
  const next = dark ? 'light' : 'dark';
  root.dataset.theme = next;
  try {
    localStorage.setItem('theme', next);
  } catch {
    // Not fatal: the choice holds for this page view and is simply not kept.
  }
});

/** The header grows a hairline once the page has moved, and nothing else. */
const header = document.querySelector('header.top');
if (header) {
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 8);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/**
 * Which section you are in, in the nav.
 *
 * An observer rather than a scroll handler, and it marks the last section whose
 * top has passed under the header — so the current item is the section you are
 * reading rather than whichever one happens to be tallest on screen.
 */
const navLinks = new Map<string, HTMLAnchorElement>();
document.querySelectorAll<HTMLAnchorElement>('nav a[data-nav]').forEach((a) => {
  navLinks.set(a.dataset.nav ?? '', a);
});
if (navLinks.size && 'IntersectionObserver' in window) {
  const seen = new Set<string>();
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) seen.add(entry.target.id);
        else seen.delete(entry.target.id);
      }
      const current = [...navLinks.keys()].find((id) => seen.has(id));
      navLinks.forEach((a, id) =>
        current === id ? a.setAttribute('aria-current', 'true') : a.removeAttribute('aria-current'),
      );
    },
    { rootMargin: '-20% 0px -70% 0px' },
  );
  navLinks.forEach((_a, id) => {
    const section = document.getElementById(id);
    if (section) observer.observe(section);
  });
}

/** A `#paper=<key>` fragment opens that record, so a row can be linked to. */
function openFromHash(): void {
  const m = /^#paper=(.+)$/.exec(decodeURIComponent(location.hash));
  if (m) openDetail(m[1]);
}
window.addEventListener('hashchange', openFromHash);

wireTagFilters();
render();
openFromHash();

export type { EvidenceTag };
