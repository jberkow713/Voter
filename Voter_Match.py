import pandas as pd
import numpy as np

class District:
    def __init__(self, num):
        self.txt = f'District_{num}.txt'
        self.df = self.create_df()
    def create_df(self):
        data = pd.read_csv('District_1.txt', sep=',')
        usable = ['LAST_NAME','FIRST_NAME', 'DATE_OF_BIRTH',\
            'RESIDENTIAL_CITY', 'RESIDENTIAL_STATE', 'RESIDENTIAL_ZIP','SOS_VOTERID']
        data = data[usable]
        data['birth_year']=data['DATE_OF_BIRTH'].str.split('-').str[0]
        final_usable = ['LAST_NAME', 'FIRST_NAME', 'RESIDENTIAL_ZIP', 'RESIDENTIAL_CITY',\
            'birth_year','SOS_VOTERID']
        District = data[final_usable]
        return District.apply(lambda x: x.astype(str).str.lower())

class Search_List:
    def __init__(self, csv):
        self.csv = csv
        self.df = self.create_df()
    def create_df(self):
        Search =  pd.read_csv(self.csv)
        Search = Search.dropna()        
        Search['RESIDENTIAL_ZIP']=Search['zip'].astype(int)
        Search['birth_year']=Search['birth_year'].astype(int)
        new = Search["name"].str.split(" ", expand = True)        
        Search["FIRST_NAME"]= new[0]         
        Search['LAST_NAME'] = Search['name'].str.split().str[-1]
        Search['RESIDENTIAL_CITY']=Search['city']        
        usable_csv = ['LAST_NAME', 'FIRST_NAME', 'RESIDENTIAL_ZIP', 'RESIDENTIAL_CITY', 'birth_year']
        Final_Search = Search[usable_csv]        
        return Final_Search.apply(lambda x: x.astype(str).str.lower())




D_1 = District(1).df
Search = Search_List("voter_data.csv").df
print(Search)


# print(len(Final_Search))
First_Search = Search.loc[4].to_list()
L_name = First_Search[0]
F_name = First_Search[1]

Zip = First_Search[2]
City = First_Search[3]
Year = First_Search[4]
print(L_name,F_name,Year,Zip)


# print(District.loc[District['RESIDENTIAL_ZIP']==Zip])
print(D_1.loc[((D_1['LAST_NAME'] == L_name) & (D_1['FIRST_NAME'] == F_name)) & \
    (D_1['birth_year'] == Year) ])

# print(District_Search)
# print(Final_Search)

