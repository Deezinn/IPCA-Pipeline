from base_extract import get
from transforms.ipca_transform import transform

class ETLPipeline():
    def __init__(self):
        self.get = get()
        self.transform = transform()

    def runPipeline(self):
        self.get.loadAllMethods()
        self.transform.loadAllMethods()



pipeline = ETLPipeline()
pipeline.runPipeline()
