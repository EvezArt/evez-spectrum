# EVEZ-TOOLS SECURITY ADDENDUM — Mesh Tool Registry Law
2026-10-11, Cipher. Read with the evez-tools spec (Distributed Tool Discovery & Invocation, v1.0.0) staged in the mesh docs.

## PRECEDENT FROM THIS SUBSTRATE (why this law exists)
- 2026-10-03, Hermes hardening pass on the VPS FOUND BOTH OF THESE LIVE:
  1. :9001 inter-agent coordination API accepted UNAUTHENTICATED task
     injection — anyone on the internet could POST a task assigned to `main`.
  2. The swarm's internal topology, task queue, and event chain were
     WORLD-READABLE. Fixed with a shared token + write gating; verified closed.
- The evez-tools spec is the same surface, generalized: "Any agent can discover
  and invoke any tool across the mesh," exposed over HTTP
  (POST /tools/:name/invoke, POST /tools/register, GET /tools).
  The philosophy line is the vulnerability unless the registry enforces it.

## REGISTRY LAW (mandatory before any mesh node runs tool traffic)
1. AUTH DEFAULT-DENY AT THE REGISTRY. A tool YAML omitting `auth.required: true`
   FAILS registration. There is no anonymous invoke path — not for agents,
   not for the health checks, not for "internal" nodes.
2. DISCOVERY IS CAPABILITY-SCOPED. Agents see only tools their role may invoke.
   GET /tools and GET /tools/:name must be role-filtered; a full directory
   dump is an attack map of the mesh (precedent: world-readable topology).
3. REGISTRATION IS NOT OPEN. POST /tools/register requires admin role +
   mesh-internal bind. A hostile node must not be able to register a tool
   that shadows a built-in (e.g. a fake `docker.build` that exfiltrates).
   Registration of built-in names by non-admin roles = reject + ThreatIntel row.
4. MESH-LAYER ENFORCEMENT, NOT TOOL-HONESTY. Rate limits and input_schema
   validation are enforced by the registry at invoke time. A tool node's
   YAML declared limits are declarations, not controls.
5. BUILT-INS ARE WEAPONS. `exec` (shell), `llm.complete` (unbounded spend),
   `k8s.deploy` (external effect) are capability-gated to admin-only unless
   a tool explicitly grants a role. Composite tools inherit the union of
   their children's requirements — deploy must not run if docker.build
   alone was authorized.
6. AUDIT EVERY INVOKE. caller identity, tool, params hash, result status,
   into the spine. A tool mesh without an invoke ledger cannot answer
   "who did what" — and this stack's whole claim is that it can.
7. HEALTH CHECKS LEAK NOTHING. GET /tools/:name/health returns up/down +
   latency only — never stack traces, versions, or endpoint URIs.

## FALSIFIER
Any mesh node exposing /tools/* invoke or register without auth,
any directory listing unscoped by role, or any exec-class capability
reachable by a non-admin identity = exposure violation: wheel row,
tool disabled at the registry until fixed.

- Cipher. The mesh is the toolbox. Toolboxes have locks, not open doors.
