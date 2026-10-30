# Preparação para entrevistas

[Portfólio](../README.pt-BR.md) · [Competências](competencies/skills-matrix.md)

## Apresentação técnica

Explicar o problema de negócio, o usuário, o fluxo mínimo, a arquitetura e as limitações. Distinguir experiência prévia, proposta documentada e implementação demonstrável. Enquanto os projetos estiverem Planned, usar linguagem de intenção: “planejo avaliar”, “a arquitetura proposta”.

## Perguntas para praticar

| Tema | Pergunta | Evidência futura para sustentar a resposta |
| --- | --- | --- |
| ML | Por que TF-IDF antes de um LLM? Como evitar vazamento? | Baseline, split e análise de erros |
| Avaliação | Como lidar com desbalanceamento e incerteza? | Métricas por classe e limiar escolhido na validação |
| RAG | Como escolher chunking e medir recuperação? | Conjunto de perguntas e recall@k |
| Responsible AI | Quando abster ou encaminhar para humanos? | Casos sem evidência e revisão auditada |
| Agentes | Como impedir ferramentas indevidas e loops? | Allowlist, limites e testes de autorização |
| Integração | O que ocorre quando n8n repete um callback? | Testes de idempotência e recuperação |
| Segurança | Como impedir acesso a documentos de outro usuário? | Escopo derivado no servidor e testes negativos |
| Operação | Como investigar um timeout entre serviços? | Request ID, logs sem dados sensíveis e métricas |

## Roteiro de demonstração futuro

Mostrar entrada válida, classificação, consulta documental quando necessária, resposta com fontes e caso de transferência humana. Demonstrar uma falha controlada e os testes correspondentes. Preparar instruções locais sem chaves reais ou dependência de um deploy público.

Não há resultados para apresentar ainda. Nunca inventar métricas, participação profissional ou experiências comportamentais; usar situações reais e explicitar a contribuição individual.
