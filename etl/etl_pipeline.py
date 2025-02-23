from etl.base_extract import Get
from etl.transforms.ipca_transform import transform
from etl.load_data import load

class ETLPipeline():
    def __init__(self):
        self.get = Get()
        self.transform = transform(self.get.dataframes)
<<<<<<< HEAD
        self.load = load(self.transform.dataframes)
=======
        self.Load = load(self.transform.dataTratado)
>>>>>>> aa86d4b (so falta conexao com banco)

    def runPipeline(self):
        self.get.loadAllMethods()
        self.transform.transformar()
<<<<<<< HEAD
        
=======
        self.Load.insert_data()
>>>>>>> aa86d4b (so falta conexao com banco)


pipeline = ETLPipeline()
pipeline.runPipeline()
