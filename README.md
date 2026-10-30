# Generative AI Engineering Portfolio

**AI Engineer | AI Builder | Machine Learning | RAG | AI Agents**

[Português](README.pt-BR.md)

Technical portfolio by [Mateus Mendes](https://github.com/MendesDSilva), building on prior experience with Python, SQL, data engineering, Docker, Databricks, Airflow, dbt, PostgreSQL, Azure, AWS, Git and GitHub. This hub presents proposed AI systems, engineering decisions and future evidence for AI Engineer and AI Builder opportunities.

## Project overview

This is a documentation hub. Application code will live in three independent repositories; their availability has not been verified, so repository names below are identifiers rather than links.

| Project | Intended repository | Business purpose | Status |
| --- | --- | --- | --- |
| [AI Customer Service](docs/projects/customer-service.md) | `genai-customer-service` | Automate routine requests and route complex cases to humans | Planned |
| [Enterprise RAG Assistant](docs/projects/enterprise-rag.md) | `genai-enterprise-rag` | Answer corporate questions using document evidence | Planned |
| [Intelligent Ticket Classifier](docs/projects/ticket-classifier.md) | `genai-ticket-classifier` | Categorize support tickets with supervised ML | Planned |

## Integrated architecture

The customer service API validates requests and orchestrates conditional calls to the classifier, RAG assistant and a tool-using agent. Routine requests can bypass retrieval; uncertain predictions, missing evidence or failures can trigger human review. n8n handles asynchronous workflows. PostgreSQL stores operational records, while a separate RAG-owned PostgreSQL database with pgvector stores searchable knowledge.

See the [Mermaid ecosystem diagram and service boundaries](docs/architecture/ecosystem.md), [integration contracts](docs/architecture/integration-contracts.md) and [architecture decisions](docs/architecture/architecture-decisions.md).

## Competency overview

| Area | Planned technical evidence |
| --- | --- |
| Software engineering | Typed APIs, Pydantic schemas, tests and Docker builds |
| Machine learning | TF-IDF baseline, held-out evaluation and versioned artifacts |
| Generative AI | Retrieval, source citations, abstention and evaluation |
| Agents and automation | LangGraph tools, human approval and n8n workflows |
| Operations | Correlated logs, metrics, security controls and CI |

The [complete skills matrix](docs/competencies/skills-matrix.md) separates planned evidence from prior experience. No application implementation evidence is available yet.

## Proposed technologies

Python, FastAPI, Pydantic, PostgreSQL, pgvector, scikit-learn, LangGraph, n8n, an LLM API, pytest, Docker, GitHub Actions and Lovable for a proposed interface. Providers and dependency versions will be selected in each application repository.

## Engineering practices

Proposed practices include REST contracts, typed boundaries, least-privilege tools, human review, redacted telemetry, reproducible evaluation and CI checks. This hub includes documentation validation; application testing and deployment pipelines remain planned. See [contribution guidelines](CONTRIBUTING.md) and [security guidance](SECURITY.md).

## Development roadmap

| Target dates (2026) | Focus | Status |
| --- | --- | --- |
| Oct 30–31 | Preparation: Python, FastAPI, Git, Docker | Planned |
| Nov 1–4 | Ticket classifier | Planned |
| Nov 5–9 | Enterprise RAG | Planned |
| Nov 10–14 | Customer service and integration | Planned |
| Nov 15 | Tests, documentation and CI/CD | Planned |
| Nov 16 | Portfolio and interviews | Planned |
| Nov 17 | Final review and application | Planned |

These are planning targets, not completed deliveries. See the [19-day roadmap](docs/learning-roadmap.md).

## Demonstrations and results

No demos, deployments, evaluation scores or screenshots are available yet. Future updates should link to reproducible runs and describe datasets, versions and limitations. Assets are reserved under [diagrams](assets/diagrams/) and [screenshots](assets/screenshots/).

## Navigate the portfolio

1. Read a project brief in the table above for scope and acceptance criteria.
2. Follow the architecture documents for responsibilities, contracts and failure handling.
3. Review the skills matrix for planned evidence and implementation status.
4. Consult the [roadmap](docs/learning-roadmap.md), [interview preparation](docs/interview-preparation.md) and [changelog](CHANGELOG.md).

Status vocabulary: **Planned** means not implemented; **In Progress** means active implementation with linked evidence; **Completed** means acceptance criteria are verified with linked evidence. Documentation of a proposal does not complete the proposed application.

## Independence and license

This independent portfolio supports preparation for GEN AI iFood 2026. It has no official affiliation with or endorsement from iFood. No private company data or branding is included. Released under the [MIT License](LICENSE).
