# Controller Session Gate

The controller uses local SQLite-backed sessions with a TTL.

Session rules:

- start a session before live-write planning
- check session status before gated operations
- close the session when the task ends
- expired or closed sessions do not authorize live writes

The session database is local only and is not published.

## Live Write Gate

A live action must satisfy all conditions:

```text
execute=true
active controller session
redacted output
dry-run path available
```

Without those conditions, the controller returns a dry-run plan or a blocked state.
