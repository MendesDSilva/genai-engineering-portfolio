# Intelligent Ticket Classifier

[Portfólio](../../README.pt-BR.md) · [Arquitetura](../architecture/ecosystem.md) · [Contratos](../architecture/integration-contracts.md)

Status: **Planned**. Repositório independente previsto: `genai-ticket-classifier`. Nenhuma funcionalidade foi implementada neste hub.

## Problema de negócio

Classificar chamados para melhorar o encaminhamento, mantendo revisão humana para previsões incertas.

## Funcionalidades previstas

- Preparação de dataset com origem e licença registradas
- Pré-processamento de texto e vetorização TF-IDF
- Treinamento com scikit-learn
- Avaliação de accuracy, precision, recall e F1-score
- Matriz de confusão
- Persistência versionada do pipeline
- API de inferência com FastAPI
- Revisão humana para previsões incertas
- Testes automatizados e Docker

## Stack proposta

Python, scikit-learn, FastAPI, Pydantic, pytest e Docker.

## Competências

Machine Learning, NLP, Model Evaluation, Feature Engineering, Model Serving e MLOps.

## Critérios de aceite planejados

- Separação treino/validação/teste evita duplicatas e vazamento; TF-IDF é ajustado só no treino
- Relatório inclui suporte por classe, macro e weighted F1, accuracy, precision, recall e matriz de confusão
- Pipeline persistido mantém comportamento no serving e registra versões e seed
- Limiar de revisão é escolhido na validação; score não é chamado de probabilidade sem calibração
- Artefatos só são carregados de fontes confiáveis e inputs inválidos são testados

## Categorias e dados

Categorias iniciais: `pagamento`, `entrega`, `cancelamento`, `reembolso`, `cadastro`, `outros`. Dataset ainda não selecionado. Usar dados públicos licenciados ou sintéticos explicitamente identificados, sem dados pessoais reais. Validar distribuição, ambiguidade e representatividade; dados sintéticos não comprovam desempenho em produção.

## Evidências e demonstração

Ainda indisponíveis. Quando existirem, adicionar links para código, testes, execução reproduzível, arquitetura efetiva, demo e resultados com limitações. Atualizar o status somente com evidências verificáveis.

## Sequência de implementação

Definir contrato e dados → construir caminho mínimo → testar falhas → avaliar → empacotar → documentar evidências. Ver [roadmap](../learning-roadmap.md).
