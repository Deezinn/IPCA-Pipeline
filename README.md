# ETL para Inserção de Dados do IPCA no PostgreSQL

## Descrição

Este projeto realiza o processo de ETL (Extract, Transform, Load) para importar dados sobre o IPCA (Índice de Preços ao Consumidor Amplo) e inseri-los em um banco de dados PostgreSQL.

## Fluxo do Processo

1. **Extração**: Os dados do IPCA são coletados de uma fonte confiável (exemplo: API do IBGE).
2. **Transformação**: Os dados extraídos passam por limpeza e padronização, garantindo a consistência antes da carga.
3. **Carga**: Os dados tratados são inseridos no banco de dados PostgreSQL para análises e visualizações futuras.

## Tecnologias Utilizadas

- **Python**: Para automação do processo ETL
- **Pandas**: Para manipulação e tratamento de dados
- **Psycopg2**: Para conexão com o banco de dados PostgreSQL
- **PostgreSQL**: Para armazenamento dos dados transformados
