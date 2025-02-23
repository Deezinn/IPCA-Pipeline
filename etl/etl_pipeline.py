from etl.base_extract import Get
from etl.transforms.ipca_transform import transform
from etl.load_data import load

class ETLPipeline():
    def __init__(self):
        self.get = Get()
        self.transform = transform(self.get.dataframes)
        self.load = load(self.transform.dataframes)

    def runPipeline(self):
        self.get.loadAllMethods()
        self.transform.transformar()
        


pipeline = ETLPipeline()
pipeline.runPipeline()
