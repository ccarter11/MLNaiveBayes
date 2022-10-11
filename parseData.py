import pandas as pd 
#read data and make tables
def normalizeAge(age): 
    age = age//10 
    return age 

def parseData(file,fields): 
    suffix = file.split(".")
    suffix = suffix[1]
    if suffix== ".xlsx":
        dataframe = pd.read_excel(file)
    elif suffix ==".csv":
        dataframe = pd.read_csv(file)
    else: 
        print("File type not supported. Please use .xlsx or .csv")
        return 
    tables=[]
    for i in range(len(fields)): 
        tables.append({})

    print(dataframe.columns)
    for i in range(dataframe.shape[0]):
        for i,field in enumerate(fields): #County, Worst Crime Display,
            curr = dataframe.iloc[i][field] 
            if field == "Age": 
                curr= normalizeAge(curr)
            if curr in tables[i]: #if the category 
                tables[i][field]+=1
            else: 
                tables[i][field] = 1
    return tables 
    # dataframe2 = pd.read_csv("CrimeStatistics.csv" ,low_memory=False)
    # print(dataframe2.head())

    #iloc to locate row/ columns'
    #for each race for each count for each crime

    