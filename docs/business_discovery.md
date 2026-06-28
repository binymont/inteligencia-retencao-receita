# Business Discovery

## 1. Contexto do Cliente

O cliente é um e-commerce em crescimento rápido, com operação digital consolidada, mas ainda em transição para uma arquitetura de dados moderna e escalável. A empresa atua em um mercado competitivo e busca aumentar a eficiência de aquisição de clientes, otimizar retenção e melhorar a margem de receita através da inteligência de dados.

O momento atual é caracterizado por aumento de volume transacional, maior complexidade de canais de marketing e a necessidade de suportar decisões estratégicas com informações confiáveis e de baixo atrito operacional.

## 2. Desafios do Negócio

- Dados inconsistentes entre áreas
  - As equipes de Marketing, Produto, Financeiro e Operações utilizam fontes distintas para os mesmos indicadores, gerando divergências em métricas críticas como receita, pedidos, investimento e retorno.

- Falta de uma única fonte da verdade
  - Não existe um repositório unificado de dados que sirva como referência oficial para transações, clientes e jornada de compra.

- Baixa confiança nos indicadores
  - Relatórios são produzidos manualmente e com lógica descentralizada, resultando em baixa confiabilidade dos dashboards e atrasos na tomada de decisão.

- Dificuldade para identificar canais de aquisição eficientes
  - As equipes não conseguem comparar de forma precisa o desempenho de canais, campanhas e fontes de tráfego, impedindo otimização de investimento.

- Churn detectado apenas quando a receita cai
  - A percepção de perda de clientes e queda de receita é reativa, o que reduz a capacidade de agir antes que o impacto financeiro se materialize.

- Alto índice de cancelamentos e devoluções
  - Cancelamentos e devoluções têm efeito significativo sobre receita e fluxo de caixa, mas não são monitorados de forma integrada com as métricas de vendas e comportamento do cliente.

## 3. Objetivos Estratégicos

O cliente espera obter:

- Visibilidade única e alinhada de receita, retenção, churn e desempenho de marketing.
- Capacidade de análise em tempo quase real para suportar decisões de Growth e operação.
- Base de dados confiável para mensurar retorno de investimento e identificar oportunidades de melhoria.
- Maior previsibilidade de receita e redução de perdas por cancelamentos e devoluções.
- Melhoria na governança de dados e valor de decisão para os níveis executivo e operacional.

## 4. Stakeholders

- Head of Growth
  - Utilizará a plataforma para priorizar canais de aquisição, alocar verba de marketing e validar hipóteses de expansão.

- Marketing
  - Acompanhará performance de campanhas, ROAS e eficiência de investimento por fonte de tráfego.

- Financeiro
  - Validará receitas, cancelamentos, devoluções e a consistência dos resultados financeiros com a contabilidade.

- Produto
  - Avaliará a jornada de compra, comportamentos dos clientes e oportunidades de retenção via melhorias de experiência.

- Diretoria
  - Receberá relatórios executivos alinhados à estratégia de receita e retenção, com visibilidade clara de riscos e oportunidades.

- Analytics
  - Construirá e manterá a plataforma, garantindo qualidade de dados, modelagem dimensional e entrega de insights acionáveis.

## 5. Perguntas de Negócio

A plataforma deverá responder perguntas como:

- Qual canal gera maior ROI?
- Quais campanhas possuem maior ROAS?
- Quais clientes apresentam maior Lifetime Value?
- Quais regiões apresentam maior taxa de cancelamento?
- Quais segmentos apresentam maior churn?

## 6. Objetivos da Solução

A plataforma resolverá os problemas identificados ao:

- Consolidar dados transacionais, de marketing e financeiros em uma única fonte de verdade.
- Estabelecer um fluxo de dados end-to-end que suporte ingestão, limpeza, transformação e validação.
- Fornecer métricas padronizadas de receita, churn, retenção, cancelamento e devolução.
- Permitir análise comparativa entre canais, campanhas e cohortes de clientes.
- Suportar visualização de dados confiável e governada para as equipes de estratégia e operação.

## 7. Critérios de Sucesso

Os critérios de sucesso para o projeto incluem:

- Existência de um repositório único e governado para dados de pedidos, clientes e marketing.
- Consistência comprovada entre relatórios de receita e as principais áreas do negócio.
- Redução do tempo de entrega de relatórios analíticos críticos.
- Disponibilização de indicadores de churn e cancelamento em uma camada analítica estabelecida.
- Capacidade de gerar respostas a perguntas-chave de negócio de forma estruturada.

## 8. Escopo

A entrega incluirá:

- Mapeamento e integração das principais fontes de dados de e-commerce, marketing e financeiro.
- Construção de uma arquitetura de dados moderna, baseada em camadas medallion.
- Definição de modelos dimensionais para receita, clientes, pedidos e canais.
- Estabelecimento de pipelines de ingestão, transformação e validação de dados.
- Implementação de métricas de retenção, churn, cancelamentos e devoluções.
- Documentação da solução e governança de dados.

## 9. Fora do Escopo

Não estão incluídos nesta entrega:

- Desenvolvimento de aplicações de front-end ou dashboards finais.
- Integração de sistemas externos não identificados no alinhamento inicial.
- Implementação de inteligência artificial ou modelos preditivos avançados.
- Serviços de consultoria contínua além da fase inicial de descoberta e implementação.

## 10. Próximos Passos

- Conduzir workshops de alinhamento com as áreas de Marketing, Financeiro, Produto e Growth.
- Validar fontes de dados e os requisitos de modelagem dimensional.
- Definir a arquitetura técnica final e o plano de governança de dados.
- Iniciar o desenvolvimento dos pipelines de dados e da camada de modelagem.
- Estabelecer rota de entrega incremental com checkpoints de qualidade e aceitação.
