from etl.base_extract import get
import pandas as pd
import json

class EtlIpca:
    def __init__(self):
        self.df = None


    def load(self):
        get()

    def transform(self,link):
        data = pd.read_json(link)
        self.df = pd.DataFrame(data)
        self.df.to_csv('data/teste.csv', sep=',', index=False, encoding='utf-8', mode='a')

    def loadAllMethods(self,link):
            self.transform(link)

etlIpca = EtlIpca()
etlIpca.loadAllMethods('https://apisidra.ibge.gov.br/values/t/118/n1/all/v/all/p/all/d/v306%202')
