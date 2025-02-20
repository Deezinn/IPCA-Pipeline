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

        except Exception as e:
            print('Deu problema na requisição', e)
        s.close()

    def loadAllMethods(self):
        self.transform()
