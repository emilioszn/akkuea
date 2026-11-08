"""
Stellar RWA Kit - 01 System Architecture
The monorepo: one Next.js frontend, one Elysia API, one shared TypeScript
library, and one Rust/Soroban contracts workspace holding two independent
contract systems (defi-rwa, and the three income distribution contracts).
Mirrors the mermaid diagram in docs/architecture/system-architecture.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _style import *
import graphviz

g = graphviz.Digraph("system-architecture")
g.attr(**base_graph_attr(
    rankdir="TB",
    splines="polyline",
    size="16,16",
    label=hl(
        "Stellar RWA Kit - System Architecture",
        "Bun monorepo on Stellar / Soroban",
    ),
))
g.attr("node", **base_node_attr())
g.attr("edge", **base_edge_attr())

with g.subgraph(name="cluster_frontends") as fe:
    fe.attr(
        label=hl("Frontend"),
        style="rounded,dashed",
        color=B_CLIENT,
        fontcolor=B_CLIENT,
        fontname=FONT,
        fontsize="11",
        penwidth="2",
        margin="14",
    )
    fe.node("webapp", hl("apps/webapp", "Next.js 16 + React 19"),
             fillcolor=F_CLIENT, color=B_CLIENT, penwidth="2")

g.node("api", hl("apps/api", "Elysia / Bun", "localhost:3001"),
       fillcolor=F_BACKEND, color=B_BACKEND, penwidth="2")
g.node("shared", hl("apps/shared", "Types . Validation", "Stellar SDK helpers"),
       fillcolor=F_MONOREPO, color=B_MONOREPO, penwidth="2")

g.node("db", hl("PostgreSQL", "via Drizzle"), shape="cylinder",
       fillcolor=F_DB, color=B_DB)
g.node("redis", hl("Redis", "optional cache"), shape="cylinder",
       fillcolor=F_DB, color=B_DB)

with g.subgraph(name="cluster_stellar") as st:
    st.attr(
        label=hl("Stellar Network (Soroban)", "apps/contracts - two independent contract systems"),
        style="rounded,dashed",
        color=B_CONTRACT,
        fontcolor=B_CONTRACT,
        fontname=FONT,
        fontsize="11",
        penwidth="2",
        margin="14",
    )
    st.node("rwa", hl("defi-rwa", "Shares + lending"),
             fillcolor=F_CONTRACT, color=B_CONTRACT, penwidth="2")
    st.node("wl", hl("pilot-whitelist", "Investor approval"), fillcolor=F_CONTRACT, color=B_CONTRACT)
    st.node("it", hl("pilot-income-token", "Income participation"), fillcolor=F_CONTRACT, color=B_CONTRACT)
    st.node("ps", hl("pilot-payout-split", "Evidence + distribution"), fillcolor=F_CONTRACT, color=B_CONTRACT)

# Frontend <-> API
g.edge("webapp", "api", dir="both", penwidth="2", color=E_CLIENT)

# Direct wallet calls to contracts
g.edge("webapp", "rwa", label="direct wallet calls", style="dashed", fontsize="9", color=E_CONTRACT)
g.edge("webapp", "ps", style="dashed", color=E_CONTRACT)

# API infra
g.edge("api", "db", dir="both", penwidth="2", color=E_BACKEND)
g.edge("api", "redis", dir="both", penwidth="2", color=E_BACKEND)
g.edge("api", "rwa", label="admin-signed transactions", fontsize="9", penwidth="2", color=E_BACKEND)
g.edge("api", "wl", penwidth="2", color=E_BACKEND)
g.edge("api", "it", penwidth="2", color=E_BACKEND)

# Contract-to-contract reads
g.edge("ps", "it", label="reads holders", fontsize="9", style="dotted", color=E_CONTRACT)
g.edge("it", "wl", label="checks approval", fontsize="9", style="dotted", color=E_CONTRACT)

# Shared library
g.edge("webapp", "shared", dir="none", style="dotted", color=E_DEFAULT)
g.edge("api", "shared", dir="none", style="dotted", color=E_DEFAULT)

render(g, "01-system-architecture")
