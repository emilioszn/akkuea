# Contract Deployment Records

> **This document's step-by-step deployment instructions have been superseded** by [`docs/deployment/deploy-contracts.md`](../deployment/deploy-contracts.md) (the `defi-rwa` contract) and [`docs/deployment/deploy-pilot-contracts.md`](../deployment/deploy-pilot-contracts.md) (the three income distribution contracts). Use those for actually deploying. This document keeps only what those two don't cover: the deployment records and the mainnet approval process.

> The testnet records below are deployments made by the original Akkuea project, which this kit was extracted from. Deploy your own contracts and replace these records and the IDs in `apps/shared/src/contracts.testnet.json`.

## Where contract IDs live

Deployed contract addresses are stored as JSON deployment artifacts at `apps/shared/src/contracts.testnet.json` and `apps/shared/src/contracts.mainnet.json`. The shared `CONTRACT_IDS` constant (`apps/shared/src/constants/index.ts`) and the API (`apps/api/src/config/contracts.ts`) read contract IDs from these files, so recording a new deployment is a data change, not a code change.

## Pilot Contracts Testnet Deployment Record (2026-08-18)

The three Cycle 6 pilot contracts were built with `stellar contract build` (target `wasm32v1-none`) and deployed to Stellar testnet as an independent system from `defi-rwa`.

- **Network**: testnet (`Test SDF Network ; September 2015`)
- **Deployer / admin account**: `GCG62FA2P6OFRYBRSDD2D4FRWVZ5HFLM233KE5LGIL3OV4QRVM7YYBFY`
- **Operator signer**: `GCG62FA2P6OFRYBRSDD2D4FRWVZ5HFLM233KE5LGIL3OV4QRVM7YYBFY`
- **Ally signer**: `GA6NZLRUHXNMOTD5WMQ342DKRTPTGR7AZZYVY7ARXJEL4KFVXZ3WZJ3N`
- **Platform fee recipient**: `GCG62FA2P6OFRYBRSDD2D4FRWVZ5HFLM233KE5LGIL3OV4QRVM7YYBFY`
- **USDC SAC**: `CBIELTK6YBZJU5UP2WWQEUCYKLPU6AUNZ2BQ4WWFEIE3USCIHMXQDAMA`
- **Deployed on**: 2026-08-18
- **Source of truth**: [`apps/shared/src/contracts.testnet.json`](../../apps/shared/src/contracts.testnet.json)

| Contract             | Contract ID                                                | Upload tx                                                          | Deploy tx                                                          | Init tx                                                            |
| -------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `PILOT_WHITELIST`    | `CAOIML5WZYESSX5CPRFHA2OY7UXVW2ISJLL362OVX7MY3G7CMRWN3QA4` | `5b7602fa4c7bf84e5c7afe326abadc88cdc646167e61ff0bf8b82d0cebd413fe` | `3e7086788c38c8edc4d57c11f41481dd19401770a30533dfc636ef59bea4c529` | `8fb3027f1360c267463edacf50208a16faa7f568336a1fc9dc090cae2df35588` |
| `PILOT_INCOME_TOKEN` | `CDQYJRBYP62Y2BSMDEUBJYM2I4V3JE2RL7TCR3JPTW42NRLUXWKUS3MZ` | `e1adc1932e3d6f74be916182f4f655392cb0e2b0f93d173991739928074a7457` | `5cad9ec764fd3cea61eb0f0a17239266cbea14a5559b66a11b0fd0e14960fd5f` | `e533c718aa704a75a267ac89adfe0923c3860b8d423fc441464ae48a1345ea4c` |
| `PILOT_PAYOUT_SPLIT` | `CBGDO2GUWYSDU4SK3SNJJHYX6HRADUNXCU7TKJFFGLRWA4FSRZNLAJ4J` | `cf6a84f24f917c1a9f4e0ac7eb9b86bcb3d7c253bf24c4dd939255ab538f56b8` | `b06ddd1f63b8f9c74fd3bad723fcdb35c55d6ed46a268d61cd2c360938079471` | `bbfb87ac7d4248e10f38e08b71a731840ea060ef8849312d4d81462195ea9ab2` |

Explorer links:

- PILOT_WHITELIST: <https://stellar.expert/explorer/testnet/contract/CAOIML5WZYESSX5CPRFHA2OY7UXVW2ISJLL362OVX7MY3G7CMRWN3QA4>
- PILOT_INCOME_TOKEN: <https://stellar.expert/explorer/testnet/contract/CDQYJRBYP62Y2BSMDEUBJYM2I4V3JE2RL7TCR3JPTW42NRLUXWKUS3MZ>
- PILOT_PAYOUT_SPLIT: <https://stellar.expert/explorer/testnet/contract/CBGDO2GUWYSDU4SK3SNJJHYX6HRADUNXCU7TKJFFGLRWA4FSRZNLAJ4J>
- USDC SAC: <https://stellar.expert/explorer/testnet/contract/CBIELTK6YBZJU5UP2WWQEUCYKLPU6AUNZ2BQ4WWFEIE3USCIHMXQDAMA>

Build, deployment, initialization, and verification commands: see [`docs/deployment/deploy-pilot-contracts.md`](../deployment/deploy-pilot-contracts.md).

## `defi-rwa` Testnet Deployment Record

Both instances were deployed from the same `rwa_defi_contract.wasm` (built with `stellar contract build`, target `wasm32v1-none`) on **Stellar testnet**.

- **Network**: testnet (`Test SDF Network ; September 2015`)
- **Deployer / admin account**: `GBN4ABG3ES6NHKY4BURL3EMP5RA6EFQJDR4EET6U66M6YIRADPWJ7OQ6`
- **Uploaded WASM hash**: `c13878bd0845d4965a5eb26138b77db617fdccbb70a70dc47acd8c460af6a0b1`
- **Deployed on**: 2026-05-31
- **Source of truth**: [`apps/shared/src/contracts.testnet.json`](../../apps/shared/src/contracts.testnet.json)

| Contract            | Contract ID                                                | Deploy (create) tx                                                 |
| ------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------ |
| `REAL_ESTATE_TOKEN` | `CBFQV2RY5VHVFU3HT2I72FLXWY5YNZC37LWJSOZQCX45B76NBO4YZHM4` | `ff4c6b52080df05d9ad443a6a3907894fb771e187b04dbd837306c62add89724` |
| `DEFI_LENDING`      | `CBFOZBCYMIDIZLNHT6ANMBU6LSGC6REM6Z5M4ST35E5T5FDWWZAWZLTX` | `490a50682d4da46c85a8080cc5ae6b50d727bf1156c97a2c9a00c532c441bdd4` |

**WASM upload transaction** (shared by both instances; submitted with the first deploy): `c5e2fd6753437a1c8dc217e5a9797b4abdd7621aed6747fedbd03c9c72ab8079`

Explorer links:

- REAL_ESTATE_TOKEN: <https://stellar.expert/explorer/testnet/contract/CBFQV2RY5VHVFU3HT2I72FLXWY5YNZC37LWJSOZQCX45B76NBO4YZHM4>
- DEFI_LENDING: <https://stellar.expert/explorer/testnet/contract/CBFOZBCYMIDIZLNHT6ANMBU6LSGC6REM6Z5M4ST35E5T5FDWWZAWZLTX>

Full build/deploy/verification steps: see [`docs/deployment/deploy-contracts.md`](../deployment/deploy-contracts.md).

## Mainnet Deployment: approvals and checklist

Deploying smart contracts to Stellar mainnet requires a rigorous process to ensure security, compliance, and platform integrity.

### 1. Required Approvals

Mainnet deployments are restricted and must be formally approved by:

- **Lead Smart Contract Engineer**: verifies code correctness and alignment with architectural specifications.
- **Lead Security Auditor**: confirms all vulnerabilities identified in audits have been resolved.
- **Product / Governance Multisig Signers**: requires M-of-N signatures from the authorized multisig key holders to authorize transaction submission and execute initial setup.

### 2. Pre-Deployment Checklist

- [ ] **Security Audit**: an external security audit of the smart contracts must be completed with all critical and high-severity issues fixed and verified.
- [ ] **Test Coverage**: contract code must have complete unit and integration test coverage; all test suites in the monorepo must pass.
- [ ] **Smoke Tests**: run the full smoke test suite on testnet to verify end-to-end integration with the API and frontend (see [`docs/testing/smoke-tests.md`](../testing/smoke-tests.md)).
- [ ] **Multisig Wallet Setup**: a mainnet multisig account (e.g. M-of-N) must be established to act as the contract admin/owner.
- [ ] **Account Funding**: ensure the deployer account has sufficient XLM balance (at least 20-50 XLM to cover fee surges and storage deposits).

### 3. Post-Deployment: Populating `contracts.mainnet.json`

1. Locate `apps/shared/src/contracts.mainnet.json`.
2. Populate the keys with the generated contract IDs (ensuring they start with `C` and are 56 characters long):
   ```json
   {
     "REAL_ESTATE_TOKEN": "C...",
     "DEFI_LENDING": "C...",
     "PILOT_WHITELIST": "C...",
     "PILOT_INCOME_TOKEN": "C...",
     "PILOT_PAYOUT_SPLIT": "C...",
     "USDC_TOKEN": "C..."
   }
   ```
3. Commit the changes and open a pull request.

### 4. Verifying Mainnet Contracts

```bash
stellar contract invoke \
  --id <CONTRACT_ID> \
  --source <your_account> \
  --network mainnet \
  --send=no \
  -- get_oracle_config   # or the equivalent read-only getter for the contract in question
```

Cross-check the deployment on a public explorer: `https://stellar.expert/explorer/public/contract/<CONTRACT_ID>`.
