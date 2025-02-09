from requests import Request, Session
import json
import os
import pandas as pd
import psycopg2

caminho_json = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ibge.json"))

def get():
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

    except ValueError:
        print(f'O link não foi encontrado no arquivo JSON.')
        return

    s = Session()
    try:
        for i in range(len(links)):
            req = Request("GET", links[i])
            prepped = s.prepare_request(req)
            resp = s.send(prepped)
            print(f"O retorno da api {nomeLinks[i]} foi: {resp.status_code}")
            with open(caminho_json, "r", encoding='utf-8') as file:
                dados = json.load(file)
                dados_json = pd.read_json(links[i])
                df = pd.DataFrame(dados_json)
                df.to_csv(f'../data/{nomeLinks[i]}.csv', sep=',', decimal=';', encoding='utf-8', index=False)
                print(f'Baixou {nomeLinks[i]}')
    except Exception as e:
        print('Deu problema na requisição', e)
    s.close()

