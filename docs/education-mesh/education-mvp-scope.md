# Education MVP Scope

The Education mesh is bounded to the 11 MVP repositories under:

`C:\Users\jeans\Desktop\Case study\modele`

## In Scope

| Repository | App | Domain | Mesh State |
| --- | --- | --- | --- |
| `FNP-QNN-MVP` | FNP-QNN | `fnpqnn.securedme.ca` | `mesh_ready` reference |
| `FfeD-QLC-MVP` | FfeD-QLC | `ffed-qlc.securedme.ca` | `mesh_pending` |
| `securedme-scholarium` | Scholarium | `scholarium.securedme.ca` | `mesh_pending` |
| `Synthia` | Synthia | `synthia.securedme.ca` | `mesh_pending` |
| `QuaNThoR` | QuaNThoR | `quanthor.securedme.ca` | `mesh_pending` |
| `VisualAlgorithmDesigner` | Visual Algorithm | `visual-algorithm.securedme.ca` | `mesh_pending` |
| `algorithm-builder-app` | Algorithm Builder | `algorithm-builder.securedme.ca` | `mesh_pending` |
| `algoquest-ams-discovry-labs-module-` | AlgoQuest | `algoquest.securedme.ca` | `mesh_pending` |
| `V.O.T-Guardian` | V.O.T Guardian | `vot-guardian.securedme.ca` | `mesh_pending` |
| `market-guardian-retailguard` | Market Guardian / RetailGuard | `market-guardian.securedme.ca` | `mesh_pending` |
| `tesla-resonance-recovery-workbench` | Tesla Workbench | `tesla-workbench.securedme.ca` | `mesh_pending` |

## Gateway Boundary

`fnpqnn_gateway_MVP` is a component inside `FNP-QNN-MVP`. It is not counted as a separate Education app.

## Exclusion Rule

The mesh must not import or depend on the true internal runtimes:

- real `SecuredMe_Engine`
- real `FNP-QNN`
- real `FfeD framework`
- `ReaAaS-n`
- `NeuUuR-o`

