# Proposed integration contracts

[Portfolio](../../README.md) · [Ecosystem](ecosystem.md)

Status: Planned. Paths and payloads here are illustrative design proposals, not live endpoints. Each application will own its OpenAPI specification. Initial version prefix: `/v1`.

| Owner | Proposed operation | Input | Output / behavior |
| --- | --- | --- | --- |
| Customer Service | `POST /v1/messages` | conversation ID, message, request ID | Durable message ID and processing state; client polls status |
| Customer Service | `GET /v1/messages/{message_id}` | Authorized message ID | Pending, answered, awaiting human or failed, plus authorized response |
| Classifier | `POST /v1/classify` | Text and request ID | Category, model version, uncertainty score semantics and review flag |
| RAG | `POST /v1/answers` | Question, server-derived access scope, request ID | Answer with source references or explicit insufficient-evidence status |
| Customer Service | `POST /v1/tickets/{ticket_id}/assignment` | Analyst ID and expected ticket version | Authorized assignment/reassignment and audit event |
| Customer Service | `POST /v1/workflow-events` | Event ID, type and ticket ID | Deduplicated asynchronous acknowledgement |

Illustrative classifier response:

```json
{
  "request_id": "example-request-001",
  "category": "entrega",
  "score": 0.62,
  "score_type": "illustrative_uncalibrated_score",
  "model_version": "example-v0",
  "requires_review": true
}
```

The number is a fictional schema example, not an evaluation result or calibrated probability. Initial categories: `pagamento`, `entrega`, `cancelamento`, `reembolso`, `cadastro`, `outros`. The `outros` category is a learned label; it is not a substitute for unavailable inference or uncertainty.

## Validation and compatibility

- Pydantic schemas reject unknown fields where appropriate; message size, IDs and content limits must be specified before implementation.
- Propagate `X-Request-ID` across calls; generate one when absent and validate incoming values.
- Authenticate service identities, enforce resource ownership, and derive tenant/access scope on the server. Never trust a user-provided scope alone.
- Source references contain document ID, chunk ID and permitted location; return only sources authorized for the caller.
- Use additive optional fields within v1. Breaking changes require a new version and migration window.
- Error envelope: `error.code`, safe `error.message`, `request_id`, and `retryable`. Avoid raw provider responses and stack traces.
- Proposed codes: 400 malformed input, 401 unauthenticated, 403 forbidden, 404 inaccessible or missing resource, 409 version conflict, 422 schema validation, 429 rate limit, 503 dependency unavailable.

## Reliability and state

Illustrative initial budgets: classifier 2 seconds, retrieval/generation 15 seconds and overall processing 25 seconds, to be tuned through measurement. Retries must fit the overall deadline. Retry transient, idempotent operations at most twice with backoff and jitter; never blindly retry side effects.

Mutating requests use an `Idempotency-Key` scoped to identity and operation. Persist the key, request fingerprint and result atomically with the state change; reject reuse with different payloads. Define key retention before implementation. n8n events use unique event IDs and a durable outbox/inbox approach where delivery must survive restarts.

Ticket transitions are proposed as `open → assigned → resolved`, with reassignment permitted under an optimistic version check and audited actor identity. Message processing states are separate from ticket lifecycle. Human handoff persists a pending task before reporting that a review was requested.

## Planned verification

Consumer/provider schema tests; duplicate event tests; dependency timeouts; unauthorized document retrieval; conflicting assignments; malformed tool calls; and full integration scenarios covering direct reply, RAG answer, abstention and human review. No integration tests have been executed yet.
