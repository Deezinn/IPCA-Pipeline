from base_extract import get as extract


class ETLPipeline:
    def __init__(self,extract):
        self.extract = extract()
        # self.transform = transform
        # self.load = load

    def runPipeline(self):
        self.extract()
