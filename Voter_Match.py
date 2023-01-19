import pandas as pd
import numpy as np

class District:
    def __init__(self, num):
        self.txt = f'District_{num}.txt'
        self.df = self.create_df()
    def create_df(self):
        data = pd.read_csv(self.txt, sep=',')
        usable = ['LAST_NAME','FIRST_NAME', 'DATE_OF_BIRTH',\
            'RESIDENTIAL_CITY', 'RESIDENTIAL_STATE', 'RESIDENTIAL_ZIP','SOS_VOTERID']
        data = data[usable]
        data['birth_year']=data['DATE_OF_BIRTH'].str.split('-').str[0]
        final_usable = ['LAST_NAME', 'FIRST_NAME', 'RESIDENTIAL_ZIP', 'RESIDENTIAL_CITY',\
            'birth_year','SOS_VOTERID']
        District = data[final_usable]
        return District.apply(lambda x: x.astype(str).str.lower())

class Search_List:
    def __init__(self, csv,num_districts):
        self.csv = csv
        self.df = self.create_df()
        self.row_indices = self.df.index.values.tolist()
        self.num_districts = num_districts
        self.districts = self.create_districts()
         
    def create_df(self):
        Search =  pd.read_csv(self.csv)
        Search = Search.dropna()        
        Search['RESIDENTIAL_ZIP']=Search['zip'].astype(int)
        Search['birth_year']=Search['birth_year'].astype(int)
        new = Search["name"].str.split(" ", expand = True)        
        Search["FIRST_NAME"]= new[0]         
        Search['LAST_NAME'] = Search['name'].str.split().str[-1]
        Search['RESIDENTIAL_CITY']=Search['city']
        Search['ID']=None        
        usable_csv = ['LAST_NAME', 'FIRST_NAME', 'RESIDENTIAL_ZIP', 'RESIDENTIAL_CITY', 'birth_year','ID']
        Final_Search = Search[usable_csv]        
        return Final_Search.apply(lambda x: x.astype(str).str.lower())
    def create_districts(self):
        Districts = []
        for i in range(1,self.num_districts+1):
            Districts.append(District(i).df)
        print(Districts)    
        return Districts



Search = Search_List("voter_data.csv",4)
Search_df = Search.df

# This is the amount of rows to search through
# print(Search.shape[0])
Indices = Search.row_indices
Current = Indices[0]

First_Search = Search_df.loc[Current].to_list()
# This is the ID you're looking for
print(First_Search)

L_name = First_Search[0]

# print(District.loc[District['RESIDENTIAL_ZIP']==Zip])

current = 0
ID = None
for district in Search.districts:
    
    New = district.loc[district['LAST_NAME']==L_name]
    D = {}

    if len(New.values.tolist())>0:
        
        for name in New.values.tolist():
            count = 0
            compare = name[:4]
            id = name[5]
            for i in range(4):
                if First_Search[i]==compare[i]:
                    count+=1
            D[id]=count         

    max_value = max(D, key=D.get)
    if D[max_value]>current:

        current = D[max_value]
        ID =int(max_value[2:])
print(current)
print(ID)

# Now finally insert the ID at the CURRENT index in the df


