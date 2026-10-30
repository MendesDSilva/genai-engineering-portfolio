# AI Customer Service

[Portfólio](../../README.pt-BR.md) · [Arquitetura](../architecture/ecosystem.md) · [Contratos](../architecture/integration-contracts.md)

Status: **Planned**. Repositório independente previsto: `genai-customer-service`. Nenhuma funcionalidade foi implementada neste hub.

## Problema de negócio

Automatizar solicitações simples, classificar mensagens e encaminhar atendimentos complexos para analistas humanos.

## Funcionalidades previstas

- Recebimento de mensagens e validação com Pydantic
- Classificação automática via serviço independente
- Integração com assistente RAG quando houver necessidade documental
- Agente LangGraph com ferramentas autorizadas
- Automação assíncrona com n8n
- Transferência para humanos, atribuição e reatribuição de chamados
- Histórico de conversas e logs de auditoria
- Dashboard de indicadores e painel de analistas com interface proposta em Lovable

## Stack proposta

Python, FastAPI, Pydantic, LangGraph, n8n, PostgreSQL, Docker e Lovable.

## Competências

AI Agents, Tool Calling, Human-in-the-Loop, API Integration, Workflow Automation, Software Architecture e Observability.

## Critérios de aceite planejados

- Mensagem validada produz registro persistente e request ID
- Fluxos de resposta direta, RAG e transferência humana têm testes de integração
- Ferramentas sensíveis exigem autorização e aprovação; duplicatas não repetem efeitos
- Atribuições concorrentes são controladas e auditadas
- Dashboard apresenta apenas métricas efetivamente coletadas

## Segurança e operação

Separar respostas informativas de ações com efeito externo. Aplicar limites de passos, ferramentas permitidas, validação de argumentos e aprovação humana para ações sensíveis. Não armazenar conteúdo pessoal desnecessário nos logs; definir retenção e controle de acesso antes de receber dados reais.

## Evidências e demonstração

Ainda indisponíveis. Quando existirem, adicionar links para código, testes, execução reproduzível, arquitetura efetiva, demo e resultados com limitações. Atualizar o status somente com evidências verificáveis.

## Sequência de implementação

Definir contrato e dados → construir caminho mínimo → testar falhas → avaliar → empacotar → documentar evidências. Ver [roadmap](../learning-roadmap.md).
