# Architecture decisions

[Portfolio](../../README.md) · [Ecosystem](ecosystem.md)

All decisions below are proposed and subject to implementation evidence.

| ID | Decision | Rationale | Tradeoff / revisit trigger |
| --- | --- | --- | --- |
| ADR-001 | Keep hub and three application repositories separate | Make ownership, testing and demonstrations independently reviewable | Contract drift; use versioned API contracts and integration checks |
| ADR-002 | Use FastAPI and Pydantic at service boundaries | Explicit validation and typed request/response schemas | Schema changes require compatibility review |
| ADR-003 | Begin classification with TF-IDF and a linear model | Establish an interpretable, inexpensive baseline | Compare alternatives only after leakage-safe evaluation |
| ADR-004 | Store embeddings in PostgreSQL with pgvector | Reuse SQL operational skills and simplify the initial stack | Revisit after measured recall, latency and scale constraints |
| ADR-005 | Use LangGraph for bounded agent workflows | Make state transitions and human approval explicit | More complexity than a fixed workflow; keep deterministic paths simple |
| ADR-006 | Use n8n for asynchronous automation | Expose workflow steps and integration retries | Requires authenticated callbacks and idempotent handlers |
| ADR-007 | Abstain and escalate when evidence is insufficient | Avoid unsupported answers and unsafe actions | Higher human workload; tune thresholds using evaluation |
| ADR-008 | Keep provider selection open | Evaluate cost, privacy, latency and structured output support first | Provider portability requires an adapter and contract tests |

For each accepted implementation decision, add date, evidence link, alternatives considered and consequences. No benchmark or provider selection has been completed.
