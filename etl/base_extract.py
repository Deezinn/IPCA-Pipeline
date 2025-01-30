from requests import Request, Session
import json
from abc import ABC, abstractmethod

def get():

    caminho_json = "../ibge.json"

    try:
        with open(caminho_json, "r", encoding="utf-8") as file:
            dados = json.load(file)
            nomeLinks = list(dados['links'].keys())
            links = list(dados['links'].values())

    except FileNotFoundError:
        print(f'Arquivo {caminho_json} não encontrado.')
        return

    except KeyError:
        print(f'Chave dos Links não encontrada no arquivo JSON.')
        return

    s = Session()

    for i in range(len(links)):
        req = Request("GET", links[i])
        prepped = s.prepare_request(req)
        resp = s.send(prepped)
        print(f"O retorno da api {nomeLinks[i]} foi: {resp.status_code}")

    s.close()

get()



