import pandas as pd
from etl.base_extract import Get

class transform(Get):
    def __init__(self, dataframes=None):
        super().__init__()
        self.dataframes = dataframes
        self.colunas = [
            'Nivel_Territorial_Codigo', 'Nivel_Territorial', 'Unidade_de_Medida_Codigo', 'Unidade_de_Medida',
            'Valor', 'Brasil_Codigo', 'Pais', 'Variavel_Codigo', 'Variavel', 'Mes_Codigo', 'Mes'
        ]
        self.mesesNumeros = {
            'janeiro ': '1', 'fevereiro ': '2', 'março ': '3', 'abril ': '4', 'maio ': '5', 'junho ': '6',
            'julho ': '7', 'agosto ': '8', 'setembro ': '9', 'outubro ': '10', 'novembro ': '11', 'dezembro ': '12'
        }
        self.colunasRemovidas = ['Nivel_Territorial_Codigo', 'Unidade_de_Medida_Codigo', 'Brasil_Codigo', 'Mes_Codigo', 'Variavel_Codigo']
        self.dataTratado = []

    def transformar(self):
        for i, datasets in enumerate(self.dataframes):
            datasets.columns = datasets.iloc[0]
            datasets = datasets[1:].reset_index(drop=True)
            datasets.columns = self.colunas
            datasets.drop(columns=self.colunasRemovidas, inplace=True)
            datasets['Ano'] = datasets['Mes'].str[-4:]
            datasets['Mes'] = datasets['Mes'].str[-15:-4].map(self.mesesNumeros).fillna(datasets['Mes'])
            datasets['Data'] = datasets['Ano'] + '-' + datasets['Mes'] + '-01'
            datasets['Data'] = pd.to_datetime(datasets['Data'])
            datasets.drop(columns=['Ano', 'Mes'], inplace=True)
            datasets['Valor'] = pd.to_numeric(datasets['Valor'], errors='coerce')
            datasets['Valor'] = datasets['Valor'].fillna(0)
            self.dataframes[i] = datasets
