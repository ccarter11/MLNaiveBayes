import pandas as pd


def main(): 
  
    fields=["Race","State","Worst Crime Display"]
    tables=[]
    for i in range(len(fields)): 
        tables.append({})
    dataframe = pd.read_excel('publicspreadsheet.xlsx')
    dataframe2 = pd.read_csv("CrimeStatistics.csv" ,low_memory=False)
    numExonerated = dataframe.shape[0]
    numConvicted = dataframe2.shape[0]
  
    for i in range(numExonerated):
       
        for j,field in enumerate(fields): 
            curr = dataframe.iloc[i][field] 

            if curr in tables[j]: #if the category 
                tables[j][curr]+=1
            else: 
                tables[j][curr] = 1
    tables[2]['Stalking/Harassing']=tables[2]['Stalking']+tables[2]['Harassment'] #combine harassment/stalking
    tables[0]['Other']+=tables[0]['Hispanic']
    print('done ',numExonerated)
    fields2 = ["MONRACE" , "DISTRICT" , "OFFGUIDE" ]
    tables2 = [{},{},{}]
    StateMap = { 
        '0':"Maine", '1': 'Massachusetts', '2':'New Hampshire' , '3':'Rhode Island',
        '5':'Connecticut', '6':'New York','7':'New York','08':'New York',
        '9':'New York','10':'Vermont','11':'Delaware','12':'New Jersey', '13':'Pennsylvania',
        '14':'Pennyslvania','15':'Pennsylvania','16':'Maryland','17':'North Carolina','18':'North Carolina',
        '19':'North Carolina','20':'South Carolina','22':'Virginia','23':'Virginia','24':'West Virginia',
        '25':'West Virginia','26':'Alabama','27':'Alabama','28':'Alabama','29':'Florida','30':'Florida',
        '31':'Florida','32':'Georgia','33':'Georgia','34':'Georgia','35':'Louisiana','36':'Louisiana','37':'Mississippi',
        '38':'Mississippi','39':'Texas','40':'Texas','41':'Texas','42':'Texas','43':'Kentucky','44':'Kentucky','45':'Michigan',
        '46':'Michigan','47':'Ohio','48':'Ohio','49':'Tennessee','50':'Tennessee','51':'Tennessee','52':'Illinois','53':'Illinois',
        '54':'Illinois','55':'Indiana','57':'Wisconsin','58':'Wisconsin','60':'Arkansas','61':'Arkansas','62':'Iowa','63':'Iowa',
        '64':'Minnesota','65':'Missori','66':'Missouri','67':'Nebraska','68':'North Dakota','69':'South Dakota','70':'Arizona',
        '71':'California','72':'California','73':'California','74':'California','75':'Hawaii','76':'Idaho',
        '77':'Montana','78':'Nevada','79':'Oregon','80':'Washington','81':'Washington','82':'Colorado','83':'Kansas',
        '84':'New Mexico','85':'Oklahoma','86':'Oklahoma','87':'Oklahoma','88':'Utah','89':'Wyoming','90':'District of Columbia',
        '95':'Alaska','96':'Louisiana'
    }
    CrimeMap={
        '22':'Murder','20':'Manslaughter','19':'Kidnapping','27':'Sexual Assault','4':'Assault','3':'Arson',
        '9':'Drug Possession or Sale','10':'Drug Possession or Sale','13':'Weapon Possession or Sale','6':'Burglary/Unlawful Entry',
        '26':'Robbery','16':'Fraud','5':'Bribery','17':'Immigration','28':'Stalking/Harassing'
    }
    RaceMap={
        '1':'White','2':'Black','3':'Native American','4':'Asian','9':'Native American','10':'Native American','7':'Other','5':'Other'
    }
    for i in range(numConvicted):
        for j,field in enumerate(fields2): #County, Worst Crime Display,
            curr = dataframe2.iloc[i][field] 
            if field == "DISTRICT":
                if str(curr) in StateMap:
                    curr= StateMap[str(curr)]
                else: 
                    pass
            elif field == "MONRACE":
                if str(curr) in RaceMap:
                    curr = RaceMap[str(curr)]
                else:
                    pass 
            else:
                if str(curr) in CrimeMap:
                    curr = CrimeMap[str(curr)]
                else:
                    pass
            if curr in tables2[j]: #if the category 
                tables2[j][curr]+=1
            else: 
                tables2[j][curr] = 1
    print(tables[2]['Murder'],tables2[2]['Murder'])
    max=0
    maxcats =''
    page =''
    for cat1 in tables[0]:
        if cat1 not in tables2[0]:
            continue
        for cat2 in tables[1]: 
            if cat2 not in tables2[1]:
                continue
            for cat3 in tables[2]:
                if cat3 not in tables2[2]:
                    continue
                numNEx = numConvicted-numExonerated
               
                pEC = (tables[0][cat1]/numExonerated)* (tables[1][cat2]/numExonerated)*(tables[2][cat3]/numExonerated)*(numExonerated/numConvicted) #prob of exonerated given categories 
                pNC = ((tables2[0][cat1]-tables[0][cat1])/numNEx)*((tables2[1][cat2]-tables[1][cat2])/numNEx)*((tables2[2][cat3]-tables[2][cat3])/numNEx)*(numNEx/numConvicted) #prob of not exonerated given categories
                if pNC <0:#more ppl exonerated than convicted so no chance of no exoneration
                    pNC=0
                probEx = pEC/(pEC+pNC) #normalize between 0 and 1
                
                print(cat1,cat2,cat3,probEx)
                line = cat1+' ' +cat2+' '+cat3+': '+str(probEx)+'\n'
                page+= line
                if abs(probEx)>max and probEx<1:
                    max = abs(probEx) 
                    maxcats = 'best: '+cat1+' '+ cat2+' '+cat3+': '+str(max)
               

    print('best',maxcats)
    page+=maxcats
    with open('results.txt','w') as f:
        f.write(page)
    f.close()
if __name__ == "__main__":
    main()