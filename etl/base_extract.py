from requests import Request, Session
import json
import os


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

    for i in range(len(links)):
        req = Request("GET", links[i])

        try:
            prepped = s.prepare_request(req)
            resp = s.send(prepped)
            print(f"O retorno da api {nomeLinks[i]} foi: {resp.status_code}")
        except Exception as e:
            print(f"Erro ao fazer a requisição: {nomeLinks[i]}: {e}")

    s.close()

