#  deep-research-agentic-geoscience — developer and run entry points.
#
#  Two audiences, and they need different things.
#
#    make check    repo health. No network, no API key, no run directory.
#                  MUST pass from a bare `git clone` + `uv sync --frozen`.
#                  That property is what makes CI meaningful.
#
#    make audit    the run-level gate. Checks one output directory against the
#                  output contract and exits non-zero on failure. This is the
#                  thing that says whether a run is finished.
#
#  Rule about both: they are append-only in spirit. Checks get added, never
#  removed or softened to go green. A gate that passes because it stopped
#  checking is worse than an honest failure — which is the whole reason
#  scripts/audit.py replaced a self-attested audit table.
#
#  The pipeline scripts need no dependencies at all: `python3 scripts/harvest.py`
#  works on a bare Python 3.11+. uv is only used for the dev tooling, so a
#  reviewer who wants to re-run the corpus never has to install anything.

#  The run every target defaults to. Override per invocation:
#      make audit OUT=outputs/01_landscape/v0.6
OUT ?= outputs/01_landscape/v0.5

#  The 02_tango and 03_gaps runs have their own OUT, because they are different runs
#  over different corpora. Override the same way:
#      make triage-tango OUT_TANGO=outputs/02_tango/v0.2
OUT_TANGO ?= outputs/02_tango/v0.1
OUT_GAPS  ?= outputs/03_gaps/v0.1

.DEFAULT_GOAL := help
.PHONY: help setup lint fmt typecheck test check \
        smoke harvest triage audit enrich export plan web web-dev clean \
        smoke-tango harvest-tango triage-tango audit-tango gaps audit-gaps

help: ## Show this help
	@grep -hE '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'
	@echo
	@echo "  OUT=$(OUT)"

# --- development -------------------------------------------------------------

setup: ## Create the venv, install dev tools and git hooks
	uv sync
	uv run pre-commit install --install-hooks
	@test -f .env || (cp .env.example .env && echo "Created .env from .env.example — fill it in.")

lint: ## Lint (no changes written)
	uv run ruff check .
	uv run ruff format --check .

fmt: ## Auto-fix lint and format in place
	uv run ruff check --fix .
	uv run ruff format .

typecheck: ## mypy --strict over scripts/ and tests/
	uv run mypy

test: ## Unit tests, excluding anything that touches the network
	uv run pytest -m "not network" -q

check: ## Repo health check — must pass from a bare clone
	uv run ruff check .
	uv run ruff format --check .
	uv run mypy
	uv run pytest -m "not network" --cov --cov-report=term-missing
	uv run pre-commit run --all-files
	@# The prompts are exposed as slash commands by symlink. A tool that replaces
	@# one with a copy forks the prompt: the skill and prompts/ drift apart, and a
	@# run then records a prompt version that is not what was executed.
	@for link in .claude/skills/*/SKILL.md; do \
		test -L "$$link" || { echo "FAIL: $$link is not a symlink into prompts/"; exit 1; }; \
		test -e "$$link" || { echo "FAIL: $$link is a broken symlink"; exit 1; }; \
	done
	@echo "skill symlinks intact"
	@# The two 22 MB artifacts are gitignored by design and regenerate in minutes.
	@test -z "$$(git ls-files 'outputs/**/screened.csv' 'outputs/**/triage.csv')" \
		|| { echo "FAIL: a regenerable harvest artifact is tracked by git"; exit 1; }
	@echo "CHECK_PASS"

# --- one run -----------------------------------------------------------------
#
# The loop is: edit the prompt or reference/queries.json → bump the version →
# run → inspect → commit the prompt and the output together.
#
# Never point harvest or triage at a directory that already holds screening.csv.
# harvest.py merges and is safe; triage.py refuses unless forced, because
# regenerating shortlist.md underneath decisions already made against the
# previous one leaves a run that looks finished and measures its recall against
# a sample file no longer on disk.

plan: ## Print the query plan without calling anything
	python3 scripts/harvest.py --out $(OUT) --dry-run

smoke: ## Mechanics test: 3 queries, one of them periphery. Needs OUT=…-test
	@case "$(OUT)" in *-test*) ;; *) \
		echo "Refusing: smoke writes a partial corpus. Use OUT=<version>-test."; exit 2;; esac
	python3 scripts/harvest.py --out $(OUT) --no-s2 --smoke
	python3 scripts/triage.py  --out $(OUT) --audit-n 40

harvest: ## Harvest the corpus into $(OUT)/screened.csv (needs OPENALEX_API_KEY)
	@test -n "$$OPENALEX_API_KEY" || echo "warning: no OPENALEX_API_KEY — the keyless \
budget is \$$0.10/day and a full harvest will abort partway through. See .env.example."
	python3 scripts/harvest.py --out $(OUT) --no-s2

triage: ## Rank the corpus and write the shortlist and recall sample
	python3 scripts/triage.py --out $(OUT)

audit: ## Check the run against the output contract. Exits non-zero on failure
	python3 scripts/audit.py --out $(OUT)

enrich: ## Fetch author-institution countries for the admitted set (one network step)
	@# Small, tracked, and keyless-friendly: ~3 OpenAlex calls for 155 DOIs. The
	@# output is committed so `make export` needs no network.
	python3 scripts/enrich.py --out $(OUT)

export: ## Export the run as the one JSON document the front end reads
	python3 scripts/export_web.py --out $(OUT)

# --- the 02_tango run -------------------------------------------------------------
#
# Same harvester, different research space: scripts/harvest.py is frozen and already
# takes --config, so 02 ships its query plan rather than a fork of the script. Triage
# and audit are 02's own, because the domain vocabulary and the output contract differ.

smoke-tango: ## Mechanics test for 02: 3 query cells, one of them periphery
	@case "$(OUT_TANGO)" in *-test*) ;; *) \
		echo "Refusing: smoke writes a partial corpus. Use OUT_TANGO=<version>-test."; exit 2;; esac
	python3 scripts/harvest.py --out $(OUT_TANGO) --no-s2 \
		--config reference/queries_tango_smoke.json
	python3 scripts/triage_tango.py --out $(OUT_TANGO) --audit-n 40

harvest-tango: ## Harvest the 02 corpus (needs OPENALEX_API_KEY)
	@test -n "$$OPENALEX_API_KEY" || echo "warning: no OPENALEX_API_KEY — the keyless \
budget is \$$0.10/day and a full harvest will abort partway through. See .env.example."
	python3 scripts/harvest.py --out $(OUT_TANGO) --no-s2 --config reference/queries_tango.json

triage-tango: ## Rank the 02 corpus. Read triage_stats.md before changing a threshold
	python3 scripts/triage_tango.py --out $(OUT_TANGO)

audit-tango: ## Check the 02 run against its contract. Exits non-zero on failure
	python3 scripts/audit_tango.py --out $(OUT_TANGO)

# --- the 03_gaps run --------------------------------------------------------------
#
# Reads finished runs; harvests nothing. RUNS is the list it reads, and a gaps document
# is a statement about those specific run directories at a specific commit.

RUNS ?= $(OUT) $(OUT_TANGO)

gaps: ## Extract gap candidates from the finished runs in RUNS
	python3 scripts/gaps.py --out $(OUT_GAPS) $(foreach r,$(RUNS),--run $(r))

audit-gaps: ## Check the 03 run against its contract. Exits non-zero on failure
	python3 scripts/audit_gaps.py --out $(OUT_GAPS)

web: ## Build the dashboard into web/dist/ (a folder that opens from the filesystem)
	@test -n "$$(ls web/src/data/*.json 2>/dev/null)" \
		|| { echo "No exported run. Run: make export OUT=$(OUT)"; exit 2; }
	cd web && npm install --no-audit --no-fund && npm run build
	@echo "open web/dist/index.html"

web-dev: ## Serve the dashboard with hot reload
	cd web && npm install --no-audit --no-fund && npm run dev

clean: ## Remove tool caches. Never touches outputs/
	rm -rf .pytest_cache .ruff_cache .mypy_cache .coverage htmlcov
	find . -type d -name __pycache__ -not -path './.venv/*' -exec rm -rf {} +
