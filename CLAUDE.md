# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

Stellar RWA Kit is a Bun monorepo starter kit for tokenizing real-world assets on Stellar/Soroban. **The canonical description of the kit is [`docs/overview.md`](docs/overview.md): read it before making any product, scope, or architecture decision.** Where anything else in this repo (README, older docs, code comments) describes the system differently, `docs/overview.md` wins.

The kit has two independent contract systems that must not be conflated:

1. **Income distribution** (`pilot-whitelist`, `pilot-income-token`, `pilot-payout-split`): a whitelist, a non-transferable income-participation token, and an evidence-gated payout-split contract. The `pilot-` prefix and "pilot", "ally", and "operator" naming in code come from the project the kit was extracted from (Akkuea); keep them consistent rather than renaming piecemeal.
2. **Asset tokenization and lending** (`defi-rwa`): fractional property-share tokenization and a collateralized DeFi lending protocol, documented in `docs/api/`, `docs/architecture/`, `docs/deployment/`, and `docs/operations/`.

The design reasoning behind both is recorded in `docs/decisions/`.

## Non-negotiables

These apply to every piece of output from this repository (code, comments, commit messages, pull requests, and documentation), with no exceptions:

- **Quality and professionalism come first.** This kit is meant to be forked and built on by teams shipping real financial products. Every artifact must read as something a skeptical, non-technical operational partner could be handed directly.
- **Never use an em dash, anywhere.** Use a comma, a period, a colon, or parentheses instead. This is enforced repo-wide (see the `style: remove em dashes from comments across the codebase` commit); do not reintroduce one in new code, comments, commits, or docs.
- **No emojis, ever.** Not in code, commit messages, PR descriptions, or documentation. **Icons are fine and encouraged** in the UI: `apps/webapp` uses `lucide-react` exclusively for iconography (see [`docs/design-system/components.md`](docs/design-system/components.md)). Don't introduce a second icon library, and don't substitute an emoji where an icon component belongs.
- **Follow the documentation, don't improvise around it.** Before building or changing anything, check whether `docs/overview.md`, `docs/decisions/`, `docs/design-system/`, or the relevant `docs/api/`, `docs/architecture/`, `docs/deployment/`, or `docs/operations/` file already answers the question. If a change contradicts what's documented, update the documentation in the same change rather than leaving it stale.
- **Follow the design system for any `apps/webapp` UI work.** Colors, typography, and effects are CSS custom properties defined in `apps/webapp/src/app/globals.css` and documented in [`docs/design-system/foundations.md`](docs/design-system/foundations.md); components live in `apps/webapp/src/components/ui` and are documented in [`docs/design-system/components.md`](docs/design-system/components.md). Use the existing tokens and components before adding new ones. Note the known inconsistency flagged in `components.md` (some components hardcode colors instead of using tokens); don't add more of that pattern.
- **CI must pass before any work is considered done.** See "Before considering a task complete" below. Do not tell the user something is finished, fixed, or ready if you have not actually run the relevant checks and seen them pass.

## Commands

Run from the repository root unless noted.

```bash
bun install                 # install all workspace dependencies

bun run dev                 # start webapp + api concurrently
bun run dev:webapp          # webapp only (localhost:3000)
bun run dev:api             # api only (localhost:3001)

bun run build                # build all workspaces
bun run build:contracts      # build Soroban contracts (./scripts/build.sh)

bun run test                 # bun test --workspaces (all TS workspaces)
bun run lint                 # eslint across all workspaces
bun run typecheck            # tsc --noEmit across all workspaces
bun run format                # prettier --write across the repo (excludes apps/contracts)

bun run smoke                 # ./scripts/smoke/run-smoke-tests.sh, post-deploy happy-path checks
bun run storybook              # apps/webapp component storybook
```

Per-workspace (when iterating on one app, from that app's directory):

```bash
cd apps/api && bun test                       # run a single API test file: bun test src/path/to.test.ts
cd apps/webapp && bun test                    # webapp unit tests
cd apps/shared && bun run build                # rebuild @stellar-rwa-kit/shared after changing shared types
```

Smart contracts (`apps/contracts`, Rust/Soroban, not a `bun` workspace):

```bash
cd apps/contracts/contracts/defi-rwa   # or any pilot-* contract dir
cargo fmt --check
cargo clippy -- -D warnings
cargo test
stellar contract build                  # target wasm32v1-none; do NOT use plain `cargo build --target wasm32-unknown-unknown` on recent toolchains, it emits reference-types the Soroban VM rejects
```

Deployment: [`docs/deployment/deploy-contracts.md`](docs/deployment/deploy-contracts.md) (`defi-rwa`) and [`docs/deployment/deploy-pilot-contracts.md`](docs/deployment/deploy-pilot-contracts.md) (the three income distribution contracts) are separate guides with separate scripts. Do not mix them up.

## Architecture

Four applications in one Bun monorepo (three `bun` workspaces plus the Rust contracts workspace, built separately):

| Path             | Role                                                                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `apps/webapp`    | Next.js 16 / React 19 frontend: marketplace, portfolio, lending, tokenization, KYC, and the income distribution dashboards                                  |
| `apps/api`       | Elysia REST API on Bun, admin-signs transactions, orchestrates KYC and whitelist review                                                                     |
| `apps/shared`    | `@stellar-rwa-kit/shared`: types, validation, Stellar SDK helpers, contract bindings, contract-ID resolution, test factories, imported by the API and webapp |
| `apps/contracts` | Rust/Soroban. Two independent contract systems: `defi-rwa` (fractional shares + lending) and `pilot-whitelist` / `pilot-income-token` / `pilot-payout-split` (income distribution) |

Contract IDs are data, not code: `apps/shared/src/contracts.testnet.json` and `apps/shared/src/contracts.mainnet.json` are the source of truth, read by both the API and the webapp. Recording a new deployment means updating one of these JSON files, not editing application code.

The webapp talks to the API and shares `@stellar-rwa-kit/shared` with it, and also talks to the contracts directly from the browser via a connected Stellar wallet for user-signed actions (Freighter or equivalent via `@creit.tech/stellar-wallets-kit`), while the API holds the admin key for admin-signed actions (minting, oracle configuration, role grants).

Full breakdown, diagrams, and data flows: [`docs/architecture/system-architecture.md`](docs/architecture/system-architecture.md).

## Before considering a task complete

Every GitHub Actions workflow that runs on a pull request must pass, no exceptions (see [`CONTRIBUTING.md`](CONTRIBUTING.md#cicd-workflows-must-pass)). Before saying a change is done, run this from the repository root and fix everything it reports until it passes:

```bash
make check
```

It runs, locally, the same checks the pull-request workflows run for the parts of the repository you changed: style rules, shell lint, shared, API (including the database tests when Docker is running), webapp, cross-workspace integration, and contracts. `make fix` applies the formatting fixes (Prettier per workspace, `cargo fmt`). `make check-all` runs everything. Then follow the pre-push checklist in [`AGENTS.md`](AGENTS.md).

After `make fix`, check that `git diff` only covers files this change actually touches. Unrelated reformatting must not be swept into the same commit.

If a check fails, fix the root cause and re-run it, don't suppress or skip it. If a workflow failure looks unrelated to the change (flaky test, transient network error), say so explicitly rather than silently ignoring it.

## Commit conventions

Conventional Commits, one atomic logical change per commit (see [`CONTRIBUTING.md`](CONTRIBUTING.md#commit-standards) for the full standard): `<type>(<scope>): <short, lowercase, no trailing punctuation>`. Common types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, `style`. Changes go through pull requests against `develop`; no direct pushes to `main` or `develop`.
