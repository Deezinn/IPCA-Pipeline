from base_extract import Get
from transforms.ipca_transform import transform
from load_data import load

class ETLPipeline():
    def __init__(self):
        self.get = Get()
        self.get.loadAllMethods()
        self.transform = transform(self.get.dataframes)
        self.load = transform(self.transform.dataframes)

    def runPipeline(self):
        self.transform.transformar()
        print(self.transform.dataframes)

pipeline = ETLPipeline()
pipeline.runPipeline()
