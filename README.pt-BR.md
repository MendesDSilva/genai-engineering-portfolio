# Generative AI Engineering Portfolio

**AI Engineer | AI Builder | Machine Learning | RAG | AI Agents**

[English](README.md)

Portfólio técnico de [Mateus Mendes](https://github.com/MendesDSilva), apoiado na experiência prévia informada com Python, SQL, Engenharia de Dados, Docker, Databricks, Airflow, dbt, PostgreSQL, Azure, AWS, Git e GitHub. O objetivo é apresentar propostas de soluções de IA, decisões técnicas e futuras evidências para oportunidades de AI Engineer e AI Builder.

## Visão geral dos projetos

Este repositório é um hub documental. O código das aplicações ficará em repositórios independentes. Os nomes abaixo são identificadores; a existência desses repositórios ainda não foi verificada.

| Projeto | Repositório previsto | Objetivo | Status |
| --- | --- | --- | --- |
| [AI Customer Service](docs/projects/customer-service.md) | `genai-customer-service` | Automatizar solicitações simples e encaminhar casos complexos | Planned |
| [Enterprise RAG Assistant](docs/projects/enterprise-rag.md) | `genai-enterprise-rag` | Responder perguntas com evidências documentais | Planned |
| [Intelligent Ticket Classifier](docs/projects/ticket-classifier.md) | `genai-ticket-classifier` | Classificar chamados com aprendizado supervisionado | Planned |

## Arquitetura integrada

A API de atendimento valida mensagens e aciona condicionalmente o classificador, o RAG e o agente com ferramentas. Nem toda solicitação exige recuperação documental. Incerteza, ausência de evidência ou falhas podem levar à revisão humana. n8n coordena automações assíncronas; PostgreSQL mantém registros operacionais e uma base separada, pertencente ao RAG, usa pgvector para a busca.

Consulte o [diagrama Mermaid e os limites dos serviços](docs/architecture/ecosystem.md), os [contratos de integração](docs/architecture/integration-contracts.md) e as [decisões arquiteturais](docs/architecture/architecture-decisions.md).

## Competências resumidas

| Área | Evidência planejada |
| --- | --- |
| Engenharia de software | APIs tipadas, Pydantic, testes e Docker |
| Machine Learning | TF-IDF, avaliação em teste separado e artefatos versionados |
| IA generativa | Recuperação, citações, abstenção e avaliação |
| Agentes e automação | Ferramentas LangGraph, aprovação humana e n8n |
| Operação | Logs correlacionados, métricas, segurança e CI |

A [matriz completa](docs/competencies/skills-matrix.md) distingue evidências planejadas de experiência prévia. Ainda não existem evidências de implementação das aplicações.

## Tecnologias previstas

Python, FastAPI, Pydantic, PostgreSQL, pgvector, scikit-learn, LangGraph, n8n, API de LLM, pytest, Docker, GitHub Actions e Lovable para a interface proposta. Provedores e versões serão definidos nos repositórios das aplicações.

## Práticas de engenharia

Estão previstos contratos REST, tipagem, testes, ferramentas com privilégio mínimo, revisão humana, observabilidade sem dados sensíveis e avaliações reproduzíveis. O hub inclui validação documental; testes e pipelines das aplicações permanecem planejados. Consulte [contribuição](CONTRIBUTING.md) e [segurança](SECURITY.md).

## Roadmap de desenvolvimento

| Datas de 2026 | Foco | Status |
| --- | --- | --- |
| 30–31/10 | Python, FastAPI, Git, Docker e preparação | Planned |
| 01–04/11 | Intelligent Ticket Classifier | Planned |
| 05–09/11 | Enterprise RAG Assistant | Planned |
| 10–14/11 | AI Customer Service e integração | Planned |
| 15/11 | Testes, documentação e CI/CD | Planned |
| 16/11 | Portfólio e entrevistas | Planned |
| 17/11 | Revisão final e candidatura | Planned |

As datas são metas, não entregas realizadas. Consulte o [roadmap de 19 dias](docs/learning-roadmap.md).

## Demonstrações e resultados

Ainda não há demonstrações, deploys, métricas ou screenshots. Resultados futuros deverão incluir execução reproduzível, dataset, versões e limitações. As pastas de [diagramas](assets/diagrams/) e [screenshots](assets/screenshots/) estão reservadas para esses materiais.

## Como navegar

1. Comece pelos documentos dos projetos na tabela inicial.
2. Consulte arquitetura, contratos e tratamento de falhas.
3. Use a matriz para acompanhar as evidências de implementação.
4. Revise o [roadmap](docs/learning-roadmap.md), a [preparação para entrevistas](docs/interview-preparation.md) e o [changelog](CHANGELOG.md).

Estados: **Planned** indica implementação ainda não iniciada; **In Progress** exige trabalho ativo com evidência vinculada; **Completed** exige critérios de aceite verificados e evidências. Documentar uma proposta não conclui sua aplicação.

## Independência e licença

Portfólio independente para preparação ao GEN AI iFood 2026, sem afiliação ou endosso oficial do iFood. Não inclui dados privados ou identidade visual da empresa. Licença [MIT](LICENSE).
