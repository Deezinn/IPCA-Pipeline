import pandas as pd
import json
import os
from requests import Request, Session
import requests

caminho_json = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../ibge.json"))

class transform:

    def __init__(self):
        self.df = None
        self.ipcaFormatado = None
        self.data = None
        self.links = None
        self.nomeLinks = None
        self.colunas = ['Nivel Territorial Codigo', 'Nivel Territorial', 'Unidade de Medida Codigo','Unidade de Medida', 'Valor', 'Brasil Codigo', 'Pais', 'Variavel Codigo', 'Variavel', 'Mes Codigo', 'Mes']
        self.mesesNumeros = {'janeiro ': '1', 'fevereiro ': '2', 'março ':'3' , 'abril ': '4', 'maio ': '5', 'junho ': '6','julho ': '7', 'agosto ': '8', 'setembro ': '9', 'outubro ': '10', 'novembro ': '11','dezembro ': '12'}

    def transform(self):
        with open(caminho_json, "r", encoding="utf-8") as file:
            dados = json.load(file)
            self.nomeLinks = list(dados['links'].keys())
            self.links = list(dados['links'].values())

        s = Session()
        try:
            for links in self.links:
                response = requests.get(links)
                response.raise_for_status()
                self.data = response.json()
                self.dataframe = pd.json_normalize(self.data)
                self.dataframe.columns = self.dataframe.iloc[0]
                self.dataframe = self.dataframe[1:].reset_index(drop=True)
                self.dataframe.columns = self.colunas
                self.dataframe.drop(columns= ['Nivel Territorial Codigo', 'Unidade de Medida Codigo','Brasil Codigo', 'Mes Codigo', 'Variavel Codigo'])

                self.dataframe['Ano'] = self.dataframe['Mes'].str[-4:]

                meses_df = self.dataframe['Mes'].str[-15:-4]


                for i, mes in enumerate(meses_df):
                    for chave, valor in self.mesesNumeros.items():
                        if chave in mes:
                            self.dataframe.loc[i, 'Mes'] = valor
                            break

                self.dataframe['Data'] = self.dataframe['Ano'] + '-' + self.dataframe['Mes'] + '-' + '1'
                del self.dataframe['Ano']
                del self.dataframe['Mes']
                print(self.dataframe)

                
        except Exception as e:
            print('Deu problema na requisição', e)
        s.close()

    def loadAllMethods(self):
        self.transform()
