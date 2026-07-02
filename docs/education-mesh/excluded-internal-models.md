# Excluded Internal Models

Two folders were moved out of `modele` to remove ambiguity from the Education MVP workspace.

| Folder | Old Location | New Location | Status |
| --- | --- | --- | --- |
| `ReaAaS-n` | `modele\ReaAaS-n` | `Case study\ReaAaS-n` | Excluded from Education mesh |
| `NeuUuR-o` | `modele\NeuUuR-o` | `Case study\NeuUuR-o` | Excluded from Education mesh |

The folders are preserved. They are not deleted.

## Why They Are Excluded

They contain larger internal model/research material that can make the MVP scope ambiguous. The Education mesh is only allowed to use the 11 MVP repositories listed in the scope registry.

## Enforcement

The MCP mesh doctor checks that these folders are no longer present under `modele`.

