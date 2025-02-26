import psycopg2
import pandas as pd
from psycopg2.extras import execute_values
from config.database import database_info
from etl.transforms.ipca_transform import transform

class load(transform):
    def __init__(self, dataframes=None):
        super().__init__()
        self.dataframes = dataframes
        self.nomeTabelas = ['IPCA118_d', 'IPCA1737_nI', 'IPCA1737_vM', 'IPCA1737_a3m',
                            'IPCA1737_a6m', 'IPCA1737_vAA', 'IPCA1737_v12m']


    def create_tables(self, cur):
        """Cria as tabelas se não existirem."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS {} (
            id SERIAL PRIMARY KEY,
            Nivel_Territorial TEXT,
            Unidade_de_Medida TEXT,
            Valor NUMERIC,
            Pais TEXT,
            Variavel TEXT,
            Data DATE
        );
        """
        for tabela in self.nomeTabelas:
            cur.execute(create_table_query.format(tabela))
            print(f"Tabela {tabela} verificada/criada.")

    def insert_data(self):
        conn = psycopg2.connect(
            host=database_info['host'],
            port=database_info['port'],
            user=database_info['user'],
            password=database_info['password'],
            dbname=database_info['dbname'],
        )
        print('Conectou ao banco')

        cur = conn.cursor()
        self.create_tables(cur)

        for tabela, df in zip(self.nomeTabelas, self.dataframes):
            if not df.empty:
                colunas = ', '.join(df.columns)
                query = f'INSERT INTO {tabela} ({colunas}) VALUES %s'
                values = [tuple(row) for row in df.itertuples(index=False, name=None)]
                execute_values(cur, query, values)
                print(f'Dados inseridos na tabela {tabela}')

        conn.commit()
        cur.close()
        conn.close()
        print('Desconectou do banco')
