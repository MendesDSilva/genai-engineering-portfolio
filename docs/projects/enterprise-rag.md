# Enterprise RAG Assistant

[Portfólio](../../README.pt-BR.md) · [Arquitetura](../architecture/ecosystem.md) · [Contratos](../architecture/integration-contracts.md)

Status: **Planned**. Repositório independente previsto: `genai-enterprise-rag`. Nenhuma funcionalidade foi implementada neste hub.

## Problema de negócio

Permitir consultas a documentos corporativos com referências verificáveis e abstenção quando a evidência for insuficiente.

## Funcionalidades previstas

- Ingestão de documentos autorizados
- Extração e limpeza de texto
- Chunking com metadados de origem
- Geração de embeddings
- Indexação em PostgreSQL com pgvector
- Busca semântica e recuperação de contexto
- Geração de respostas com API de LLM
- Referências às fontes autorizadas
- Avaliação de qualidade e perguntas sem evidência suficiente

## Stack proposta

Python, FastAPI, PostgreSQL, pgvector, LLM API, pytest e Docker.

## Competências

LLMs, NLP, Embeddings, Vector Databases, Retrieval-Augmented Generation, Evaluation e Responsible AI.

## Critérios de aceite planejados

- Ingestão é reproduzível e atualizações não duplicam documentos
- Respostas incluem referências que apontam para trechos autorizados
- Perguntas sem evidência acionam abstenção explícita
- Avaliação registra recall@k, relevância, fidelidade às fontes, latência e custo quando medidos
- Testes cobrem autorização, documentos malformados e instruções maliciosas no contexto

## Dados e avaliação

Corpus ainda não selecionado. Registrar permissões, licença, versão de documento, estratégia de chunking e modelo de embeddings. Construir conjunto de perguntas com fontes esperadas, incluindo casos sem resposta. Separar ajuste e avaliação final; usar revisão humana e registrar limitações de qualquer avaliação por LLM.

## Evidências e demonstração

Ainda indisponíveis. Quando existirem, adicionar links para código, testes, execução reproduzível, arquitetura efetiva, demo e resultados com limitações. Atualizar o status somente com evidências verificáveis.

## Sequência de implementação

Definir contrato e dados → construir caminho mínimo → testar falhas → avaliar → empacotar → documentar evidências. Ver [roadmap](../learning-roadmap.md).
