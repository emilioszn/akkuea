# Stellar RWA Kit Documentation

**Start with [`overview.md`](overview.md).** It describes the kit's modules, the trust model, and what to change before building a product on top of it. Where any other document describes the system differently, the overview wins.

## Overview and design history

- [Overview](overview.md): modules, trust model, and what to adapt
- [Decision Log](decisions/decision-log.md): why the main design choices were made
- [Integration Decisions](decisions/integration-decisions.md): how DeFindex, EtherFuse, Trustless Work, and Spydra were verified, and which were adopted

## Design System

- [Overview](design-system/README.md): principles, what "auditable" looks like in the UI
- [Foundations](design-system/foundations.md): color tokens, typography, effects
- [Components](design-system/components.md): component inventory and conventions

## Quick Start

- [Local Setup](local-setup.md): clone, install, configure, run
- [Environment Setup Guide](ENV_SETUP.md): obtaining values for local development

## Architecture

- [System Architecture](architecture/system-architecture.md): monorepo structure, components, and data flows

## Deployment

- [Environment Variables](deployment/environment-variables.md): complete `.env` reference, secret warnings, network passphrases
- [Deploy Income Distribution Contracts](deployment/deploy-pilot-contracts.md): whitelist, income token, and payout split
- [Deploy `defi-rwa`](deployment/deploy-contracts.md): build, deploy, oracle setup, pool creation, role grants
- [Post-Deploy Checklist](deployment/post-deploy-checklist.md): liveness, oracle, roles, pool, API verification
- [Deployment Records](contracts/deployment.md): testnet/mainnet contract IDs and the mainnet approval checklist

## API Workflows

- [API Overview](api/overview.md): framework, authentication, rate limiting
- [Authentication](api/authentication.md): wallet-signature sessions
- [Launch Workflows](api/launch-workflows.md): end-to-end HTTP sequences with full payloads: KYC onboarding, property tokenization, share purchase
- [Minting Workflow](api/minting-workflow.md): tokenization path from HTTP request to on-chain `mint_shares`
- [KYC Workflow](api/kyc-workflow.md): off-chain compliance state machine, admin verification procedure, known gaps

## Operations Runbooks

Read these before an incident occurs.

Income distribution contracts:

- [Emergency Pause](operations/runbook-pilot-emergency-pause.md)
- [Admin Rotation](operations/runbook-pilot-admin-rotation.md)
- [Contract Migration](operations/runbook-pilot-contract-migration.md)
- [Review SLA](operations/pilot-review-sla.md): whitelist and evidence review turnaround target and metrics endpoint
- [TTL Policy](operations/pilot-ttl-policy.md): contract storage time-to-live

`defi-rwa` contract:

- [Emergency Pause](operations/runbook-emergency-pause.md): immediate pause, 24-hour timelock recovery, exact CLI commands
- [Oracle Failure](operations/runbook-oracle-failure.md): price feed outage, stale data response, backup oracle switch
- [Role Management](operations/runbook-role-management.md): grant/revoke EmergencyGuard, admin transfer procedure

Treasury:

- [Treasury Track](operations/runbook-treasury-track.md): DeFindex and EtherFuse venues

## Testing and Other Guides

- [Smoke Tests and Test Fixtures](testing/smoke-tests.md)
- [Buyer-Signed Share Purchase](testing/buyer-signed-share-purchase.md)
- [Accessibility Checklist](a11y-checklist.md): marketplace and lending flows
- [3D Property Capture Guide](guides/property-3d-capture.md): Gaussian Splatting property viewer

## Technology Stack

- **Blockchain**: Stellar Network (Testnet / Mainnet)
- **Smart Contracts**: Soroban (Rust)
- **Frontend**: Next.js 16, React 19, TypeScript, Tailwind CSS 4
- **Backend**: Elysia (Bun), TypeScript, Drizzle ORM
- **Package Manager**: Bun
- **CI/CD**: GitHub Actions

## Links

- **GitHub Repository**: [emilioszn/stellar-rwa-kit](https://github.com/emilioszn/stellar-rwa-kit)
- **API Documentation** (local dev): `http://localhost:3001/swagger`
- **Stellar Documentation**: [Stellar Developers](https://developers.stellar.org/)
- **Soroban Documentation**: [Soroban Docs](https://developers.stellar.org/docs/build/smart-contracts)

## Support

- Open an issue in the [GitHub repository](https://github.com/emilioszn/stellar-rwa-kit/issues)
- See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the contribution workflow
