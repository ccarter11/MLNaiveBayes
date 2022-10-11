from parseData import parseData

class naiveBayes:

    def __init__(self,files) -> None: 
        self.files= files
        pass

    def parse(self, fields): 
        for file in self.files:
         tables = parseData(fields)


    def classify(self): 
        