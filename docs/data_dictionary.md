# Data Dictionary

## Estrutura de Dados

### orders
- `order_id`: Identificador único do pedido.
- `customer_id`: Identificador do cliente.
- `order_date`: Data do pedido.
- `order_amount`: Valor bruto do pedido.
- `order_status`: Status do pedido, incluindo cancelamentos e devoluções.

### customers
- `customer_id`: Identificador único do cliente.
- `customer_name`: Nome do cliente.
- `email`: E-mail de contato.
- `customer_since`: Data de cadastro.
- `customer_status`: Estado atual do cliente.

### marketing_spend
- `campaign_id`: Identificador da campanha.
- `channel`: Canal de aquisição.
- `spend_date`: Data do investimento.
- `spend_amount`: Valor investido.
