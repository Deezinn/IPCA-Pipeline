from etl.base_extract import get
import pandas as pd
import json
import os

caminho_json = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../ibge.json"))

class EtlIpca:

    def __init__(self):
        self.df = None
        self.ipcaFormatado = None
        # self.data = None

    def load(self):
        """Aqui ficará a requisição http (get), ela retornará um status code
        """
        # get()

    def transform(self):
        """Aqui ficará o tratamento da api especifica para IPCA
        """
        try:
            with open(caminho_json, "r", encoding="utf-8") as file:
                dados = json.load(file) # depois aplicar a variavel data da classe
                nomeLinks = list(dados['links'].keys())
                links = list(dados['links'].values())

                for i in range(len(dados['links'])):
                    self.df = pd.read_json(links[i])
                    self.ipcaFormatado = pd.DataFrame(self.df)
                    self.ipcaFormatado.to_csv(f'data/{nomeLinks[i]}.csv', sep=',', decimal=';', encoding='utf-8', index=False)

        except KeyError as e:
            print('Erro de ausencia da chave no ibge.json', e)
        except ValueError as e:
            print('Erro no valor no json, esta associado a links', e)

    def loadAllMethods(self):
        self.load()
        self.transform()


etlIpca = EtlIpca()
etlIpca.loadAllMethods()
