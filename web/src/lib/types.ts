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
  /** Which page section this prose belongs beside. */
  group: 'overview' | 'fields' | 'systems' | 'evidence' | 'periphery';
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
