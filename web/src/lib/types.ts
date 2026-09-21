/**
 * The shape of the JSON `scripts/export_web.py` writes.
 *
 * Kept in step with that file by hand. The exporter is the authority: if these
 * disagree, the Python is right and this is stale.
 */

/** One bar. `share` is against the population counted, not the sum of bars. */
export interface Facet {
  label: string;
  n: number;
  share: number;
}

/** A research field: its admitted literature, and the readable slice of it. */
/** What the framework facet is a floor over: how many papers name anything. */
export interface FrameworkCoverage {
  core_total: number;
  core_named: number;
  total: number;
  named: number;
  core_any_tool: number;
  context_any_tool: number;
  context_total: number;
}

export interface Field {
  label: string;
  n: number;
  core: number;
  context: number;
  share: number;
  /** Shortlist size of the query family of the same name — a different taxonomy. */
  shortlisted: number;
  /** Admitted as a share of that shortlist, or null where there was none. */
  admitted_share: number | null;
  /** Admitted rows that came in under that same query group. */
  from_own_query: number;
  maturity: Facet[];
  systems: string[];
}

export interface FrameworkItem extends Facet {
  /** How many of the counted sources are core tier — i.e. actually read. */
  core: number;
}

export interface FrameworkKind {
  kind: string;
  items: FrameworkItem[];
}

/** Every term the derivation looks for, including those that matched nothing. */
export interface FrameworkTerm {
  label: string;
  kind: string;
  matched: boolean;
}

/** A span of report prose. `cite` is a citation resolved against papers.csv. */
export type Span =
  | { t: 'text'; v: string }
  | { t: 'code'; v: string }
  | { t: 'strong'; v: string }
  /**
   * `label` is the reference number, `name` the system behind it (for the
   * tooltip), and `tail` punctuation that must not break away from the marker.
   */
  | {
      t: 'cite';
      key: string;
      label: string;
      name: string;
      resolved: boolean;
      tail: string;
    };

export type EvidenceTag = 'Certain' | 'Likely' | 'Absent-searched';

export type Block =
  | { kind: 'heading'; level: 2 | 3; text: string }
  | { kind: 'para'; tag: EvidenceTag | null; spans: Span[]; cites: string[] }
  | { kind: 'list'; items: Span[][] };

export interface ReportSection {
  id: string;
  number: string;
  title: string;
  /**
   * Which page section this prose belongs beside. `touchpoints` exists only in
   * the 02_tango dataset — `03_touchpoints.md` is the run's central axis and gets
   * its own page group rather than being folded into `systems`.
   */
  group: 'overview' | 'fields' | 'systems' | 'evidence' | 'periphery' | 'touchpoints';
  blocks: Block[];
}

/** The verbatim evidence trail for a core paper, from `papers.md`. */
export interface Extract {
  source: string;
  source_note: string;
  quotes: string[];
  /** Questions the full text does not answer. An absence, stated as one. */
  not_found: string[];
  maturity_claimed: string;
  limitation: string;
}

/** One counted row of the executive-summary funnel. */
export interface FunnelRow {
  label: string;
  /** Null where the count could not be read. Renders as an em dash, never 0. */
  n: number | null;
  /** The population this is a share of, or null for the first row. */
  of: number | null;
  what: string;
  emphasis?: boolean;
  /** An honest caveat where the obvious question outruns the data. */
  note?: string;
}

export interface CountryCoverage {
  with_country: number;
  total: number;
  multi_country: number;
  distinct: number;
}

export interface Paper {
  key: string;
  /** Reference number, as cited in the report prose. */
  ref: number;
  tier: 'core' | 'context';
  system_id: string;
  title: string;
  authors: string;
  year: number | null;
  venue: string;
  url: string;
  source_type: string;
  subfield: string;
  subfield_secondary: string;
  task: string;
  techniques: string[];
  architecture: string;
  base_model: string;
  /** Every family the cell names. Multi-valued: a paper can be on this list twice over. */
  model_families: string[];
  /** ISO country codes of author institutions, from `enrich.py`. Often empty. */
  countries: string[];
  /** The run's own `venue`, or OpenAlex's source name where the run left it blank. */
  journal: string;
  tools_used: string;
  /**
   * Derived by keyword match over `tools_used` and `base_model`. Not a SCHEMA
   * column and not covered by any audit check — see `framework_terms`.
   */
  frameworks: string[];
  evaluation_method: string;
  baseline: string;
  held_out: string;
  data_type: string;
  reported_result: string;
  maturity_claimed: string;
  maturity_demonstrated: string;
  limitations: string;
  code_availability: string;
  access_status: 'full-text' | 'abstract-only';
  found_via: string;
  annotation: string;
  extract: Extract | null;
}

export interface Run {
  path: string;
  version: string;
  date: string;
  prompt: string;
  model: string;
  purpose: string;
  /** Null where the count could not be read. Renders as an em dash, never 0. */
  harvested: number | null;
  shortlisted: number | null;
  screened: number;
  admitted: number;
  core: number;
  context: number;
  audit_sample: number;
  false_negatives: number;
  api_calls: number;
  api_errors: number;
  queries_core: number;
  queries_periphery: number;
}

export interface AuditCheck {
  check: string;
  result: string;
  detail: string;
}

export interface Audit {
  checks: AuditCheck[];
  passed: number;
  harvested: number | null;
  shortlisted: number | null;
}

export interface Query {
  id: string;
  api: string;
  band: string;
  scope: string;
  group: string;
  query: string;
  status: string;
  available: number | null;
  results: number | null;
  new: number | null;
}

export interface PeripheryGroup {
  label: string;
  screened: number;
  available: number;
}

export interface Dataset {
  generated_at: string;
  run: Run;
  audit: Audit;
  rubric: Record<string, string>;
  tags: EvidenceTag[];
  fields: Field[];
  techniques: Facet[];
  techniques_core: Facet[];
  frameworks: FrameworkKind[];
  frameworks_coverage: FrameworkCoverage;
  framework_terms: FrameworkTerm[];
  funnel: FunnelRow[];
  journals: Facet[];
  types: Facet[];
  countries: Facet[];
  countries_coverage: CountryCoverage;
  models_multi: number;
  architectures: Facet[];
  architectures_core: Facet[];
  maturity: Facet[];
  models: Facet[];
  models_core: Facet[];
  data_types: Facet[];
  held_out: Facet[];
  years: Facet[];
  cuts: Facet[];
  periphery: PeripheryGroup[];
  queries: Query[];
  report: ReportSection[];
  papers: Paper[];
}

/**
 * What each core system actually drives — `transfer.csv`, which only the 02_tango
 * run has. `touchpoints` and `touchpoints_all` mirror the `techniques` /
 * `techniques_core` pair on `Dataset`: core first, the full admitted set behind a
 * disclosure, because a touchpoint read off an abstract is the abstract's word for
 * itself.
 */
export interface DriveRow {
  key: string;
  system_id: string;
  touchpoints: string[];
  what_it_drives: string;
  interface: string;
  autonomy: string;
}

export interface TransferFacets {
  touchpoints: Facet[];
  touchpoints_all: Facet[];
  interface: Facet[];
  autonomy: Facet[];
  failure_handling: { stated: number; not_stated: number; total: number };
  drives: DriveRow[];
}

export interface PaywalledSummary {
  total: number;
  blocked_by: Facet[];
  would_change_nothing: number;
}

/** The 02_tango export: everything `Dataset` has, plus what each system drives. */
export interface TangoDataset extends Dataset {
  transfer: TransferFacets;
  paywalled: PaywalledSummary;
}

// --- 03_gaps -----------------------------------------------------------------
// A different shape entirely: no corpus, no papers, no fields. The "run" here is
// a synthesis over two other runs' own artifacts, so its dataset is a list of
// gaps and the ledger of candidates that did not become one.

export type GapVerdict = 'confirmed-absent' | 'partially-addressed' | 'refuted' | 'undecidable';

export interface GapCandidate {
  id: string;
  run: string;
  kind: string;
  subject: string;
  statement: string;
  evidence_ref: string;
  count: number | null;
  denominator: number | null;
}

/** An evidence key resolved to the system it names, where that source was admitted. */
export interface NamedEvidence {
  key: string;
  name: string;
}

export interface Gap {
  id: string;
  title: string;
  candidates: string[];
  /** The `kind`s of the candidates this gap cites, derived for client-side filtering. */
  kinds: string[];
  runs: string[];
  verdict: GapVerdict | '';
  evidence: string[];
  evidence_named: NamedEvidence[];
  checked: string;
  blocks: Block[];
}

export interface DiscardedCandidate {
  id: string;
  reason: string;
  note: string;
}

export interface SourceRun {
  name: string;
  directory: string;
  commit: string;
}

export interface GapsRun {
  path: string;
  version: string;
  date: string;
  prompt: string;
  model: string;
  source_runs: SourceRun[];
}

export interface GapsDataset {
  generated_at: string;
  run: GapsRun;
  audit: Audit;
  candidates_total: number;
  gaps_total: number;
  cited_total: number;
  discarded_total: number;
  /** Candidates neither cited by a gap nor listed in the discard ledger. Empty on
   *  a clean run — `audit_gaps.py` fails one where it is not. */
  unaccounted: string[];
  verdicts: Facet[];
  kinds: Facet[];
  runs: Facet[];
  discard_reasons: Facet[];
  gaps: Gap[];
  discarded: DiscardedCandidate[];
  candidates: GapCandidate[];
}
