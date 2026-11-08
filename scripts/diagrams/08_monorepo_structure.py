"""
Stellar RWA Kit - 08 Monorepo Structure
The apps/ workspace tree: four applications, three of them bun workspaces plus
the Rust contracts workspace, which itself holds two independent contract
systems. Mirrors the Project Structure section of README.md.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _style import *
import graphviz

g = graphviz.Digraph("monorepo-structure")
g.attr(**base_graph_attr(
    rankdir="TB",
    splines="polyline",
    size="16,14",
    label=hl(
        "Stellar RWA Kit - Monorepo Structure",
        "Bun workspaces under apps/, plus the Rust contracts workspace",
    ),
))
g.attr("node", **base_node_attr())
g.attr("edge", **base_edge_attr())

g.node("root", hl("stellar-rwa-kit/", "Bun monorepo root"),
       shape="box", style="filled,rounded,bold", fillcolor=F_MONOREPO, color=B_MONOREPO, penwidth="3")

g.node("apps", hl("apps/"), fillcolor=F_MONOREPO, color=B_MONOREPO, penwidth="2")
g.edge("root", "apps", penwidth="2")

g.node("webapp", hl("webapp/", "Next.js 16 + React 19", "@stellar-rwa-kit/webapp"),
       fillcolor=F_CLIENT, color=B_CLIENT)
g.node("api", hl("api/", "Elysia / Bun", "@stellar-rwa-kit/api"),
       fillcolor=F_BACKEND, color=B_BACKEND)
g.node("shared", hl("shared/", "TypeScript", "@stellar-rwa-kit/shared - imported by webapp, api"),
       fillcolor=F_KYC, color=B_KYC)
g.node("contracts", hl("contracts/", "Rust / Soroban", "Not a bun workspace, built separately"),
       fillcolor=F_CONTRACT, color=B_CONTRACT, penwidth="2")

for child in ("webapp", "api", "shared", "contracts"):
    g.edge("apps", child, penwidth="2")

with g.subgraph(name="cluster_contracts") as c:
    c.attr(
        label=hl("Two independent contract systems"),
        style="rounded,dashed",
        color=B_CONTRACT,
        fontcolor=B_CONTRACT,
        fontname=FONT,
        fontsize="11",
        penwidth="2",
        margin="14",
    )
    c.node("rwa", hl("defi-rwa/", "Fractional shares + lending"),
            fillcolor=F_CONTRACT, color=B_CONTRACT, penwidth="2")
    c.node("wl", hl("pilot-whitelist/", "Income distribution"), fillcolor=F_CONTRACT, color=B_CONTRACT)
    c.node("it", hl("pilot-income-token/", "Income distribution"), fillcolor=F_CONTRACT, color=B_CONTRACT)
    c.node("ps", hl("pilot-payout-split/", "Income distribution"), fillcolor=F_CONTRACT, color=B_CONTRACT)

for child in ("rwa", "wl", "it", "ps"):
    g.edge("contracts", child)

# shared library consumed by the other TypeScript workspaces
g.edge("webapp", "shared", style="dotted", dir="none", color=E_DEFAULT)
g.edge("api", "shared", style="dotted", dir="none", color=E_DEFAULT)

render(g, "08-monorepo-structure")
