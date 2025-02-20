from requests import Request, Session
import json
import os
import pandas as pd
import psycopg2

caminho_json = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ibge.json"))

class get:
    def __init__(self):
        self.links = None
        self.nomeLinks = None

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
        s = Session()
        try:
            for i in range(len(self.links)):
                req = Request("GET", self.links[i])
                prepped = s.prepare_request(req)
                resp = s.send(prepped)
                print(f"O retorno da api {self.nomeLinks[i]} foi: {resp.status_code}")
        except Exception as e:
            print('Deu problema na requisição', e)
        s.close()

    def loadAllMethods(self):
        self.load_json()
        self.fetch_data()
        

