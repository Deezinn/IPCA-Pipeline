import pandas as pd
import json
import os
import requests
from etl.base_extract import Get


class transform(Get):
    def __init__(self, dataframes=None):
        super().__init__()
        self.dataframes = dataframes
        self.colunas = [
            'Nivel Territorial Codigo', 'Nivel Territorial', 'Unidade de Medida Codigo', 'Unidade de Medida',
            'Valor', 'Brasil Codigo', 'Pais', 'Variavel Codigo', 'Variavel', 'Mes Codigo', 'Mes'
        ]
        self.mesesNumeros = {
            'janeiro ': '1', 'fevereiro ': '2', 'março ': '3', 'abril ': '4', 'maio ': '5', 'junho ': '6',
            'julho ': '7', 'agosto ': '8', 'setembro ': '9', 'outubro ': '10', 'novembro ': '11', 'dezembro ': '12'
        }
        self.colunasRemovidas = ['Nivel Territorial Codigo', 'Unidade de Medida Codigo', 'Brasil Codigo', 'Mes Codigo', 'Variavel Codigo']
        self.dataTratado = []

    def transformar(self):
        for i, datasets in enumerate(self.dataframes):
            datasets.columns = datasets.iloc[0]
            datasets = datasets[1:].reset_index(drop=True)
            datasets.columns = self.colunas
            datasets.drop(columns=self.colunasRemovidas, inplace=True)
            datasets['Ano'] = datasets['Mes'].str[-4:]
            datasets['Mes'] = datasets['Mes'].str[:-5].map(self.mesesNumeros).fillna(datasets['Mes'])
            datasets['Data'] = datasets['Ano'] + '-' + datasets['Mes'] + '-01'
            datasets.drop(columns=['Ano', 'Mes'], inplace=True)
            self.dataframes[i] = datasets
            df = pd.DataFrame(self.dataframes[i])
            print(df)
