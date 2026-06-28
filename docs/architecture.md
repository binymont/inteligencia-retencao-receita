# Arquitetura do Projeto

## Visão Geral

A arquitetura do projeto segue o padrão Medallion para garantir maturidade dos dados, confiabilidade e separação clara de responsabilidades.

## Camadas

- Raw: dados brutos, normalmente ingestão direta de arquivos CSV ou objetos de data lake. Não há transformações.
- Bronze: dados ingeridos e persistidos com esquema mínimo, permitindo reconciliação e auditabilidade.
- Silver: dados limpos, padronizados e integrados, com regras de negócio aplicadas para análise.
- Gold: modelos analíticos prontos para consumo por dashboards e relatórios gerenciais.
- Dashboard: visualizações e KPIs para a equipe de negócios.

## Por que o Medallion?

1. Separação de preocupações.
2. Qualidade incremental e validação em cada etapa.
3. Facilidade de debugar e reprocessar dados.
4. Boa base para escalabilidade e múltiplas fontes.

## Escalabilidade

- PySpark permite processamento distribuído com milhares de nós.
- Arquitetura de camadas facilita incrementalidade e particionamento.
- Organização de código modular permite adicionar novas fontes sem quebrar pipelines existentes.
