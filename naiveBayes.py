from parseData import parseData

# def parse(files, fields): 
#     tables =[]
#     for file in files:
#         tables.append(parseData(file,fields))        
#     return tables

class naiveBayes:
    def __init__(self) -> None: 
        pass


    def classify(self,files,fields): 
        for file in files:
            tables= parseData(file, fields)
        
        # for i,field in enumerate(fields):
        #     for category in tables[i]:
                

        # for cat1 in fields[0]:
        #     for cat2 in fields[1]: 
        #         for cat3 in fields[2]: 
                    
                    