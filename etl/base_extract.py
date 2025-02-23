import requests
import json
import os
import pandas as pd

caminho_json = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ibge.json"))

class Get:
    def __init__(self):
        self.links = None
        self.nomeLinks = None
        self.dataframes = []
        self.dataJson = None
        self.dataTratado = None
    def load_json(self):
        try:
            with open(caminho_json, "r", encoding="utf-8") as file:
                dados = json.load(file)
                self.nomeLinks = list(dados['links'].keys())
                self.links = list(dados['links'].values())

        except FileNotFoundError:
            print(f'Arquivo {caminho_json} não encontrado.')
        except KeyError:
            print(f'Chave dos Links não encontrada no arquivo JSON.')
        except ValueError:
            print(f'O link não foi encontrado no arquivo JSON.')
    def fetch_data(self):
        try:
            for links in self.links:
                response = requests.get(links)
                response.raise_for_status()
                self.dataJson = response.json()
                self.dataTratado = pd.json_normalize(self.dataJson)
                self.dataframes.append(self.dataTratado)
        except Exception as e:
            print('Deu problema na requisição', e)
        except requests.exceptions.HTTPError as err:
            print(f"Erro HTTP: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Erro na requisição: {err}")
    def loadAllMethods(self):
        self.load_json()
        self.fetch_data()
