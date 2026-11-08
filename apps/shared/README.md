# @stellar-rwa-kit/shared

Shared types, validation, Stellar SDK helpers, contract-ID resolution, and test
factories for the Stellar RWA Kit monorepo. Imported by the other TypeScript
workspaces (`apps/webapp`, `apps/api`).

## Generating Soroban TypeScript Bindings

Contract client bindings are generated using `stellar contract bindings typescript`
against deployed contract IDs from `contracts.testnet.json` (or
`contracts.mainnet.json`). The generated output is post-processed to follow the
project's quality standards: inlined into single files, `import type` for type-only
imports, `globalThis` polyfill guard, `override` on deploy/options, local
`Timepoint`/`Duration` aliases.

### Pilot contracts

```bash
cd apps/shared
bun run generate:pilot-bindings
```

This regenerates the typed clients for all three pilot contracts:

- `pilot-whitelist` - wrapper: `src/contracts/pilot/whitelist.ts`
- `pilot-income-token` - wrapper: `src/contracts/pilot/income-token.ts`
- `pilot-payout-split` - wrapper: `src/contracts/pilot/payout-split.ts`

Raw generated output is in `src/contracts/pilot/generated/`.

After regeneration:

1. Run `bun run type-check` to verify no type errors.
2. Run `bun run format` to fix formatting.
3. Run `bun test` to confirm existing tests still pass.

## Re-adding contract IDs

After a redeploy, update the appropriate JSON file:

- Testnet: `apps/shared/src/contracts.testnet.json`
- Mainnet: `apps/shared/src/contracts.mainnet.json`

Then regenerate bindings as described above.
