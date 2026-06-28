# Dimensional Model

## Visão Geral

Este projeto utiliza um modelo dimensional simples para suportar análises de receita e retenção.

## Dimensões

- `dim_customer`: informações do cliente.
- `dim_date`: dimensão de data para pedidos e investimento.
- `dim_marketing_channel`: canais de aquisição.

## Fatos

- `fact_order`: pedidos e métricas de receita.
- `fact_marketing_spend`: investimento em marketing por canal.

## Observações

O modelo garante simplicidade para relatórios e compatibilidade com ferramentas como Power BI.
