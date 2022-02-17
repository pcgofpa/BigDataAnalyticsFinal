import csv
from matplotlib import pyplot as plt
import pandas as pd

fin = "Data_GOV.csv"
fout = "DataOut.csv"

data = pd.read_csv(fin, usecols=['StateAbbr', 'CountyName', 'TotalPopulation', 'CASTHMA_CrudePrev', 'CSMOKING_CrudePrev'])
data.rename(columns={'StateAbbr': 'state', 'CountyName': 'cname', 'TotalPopulation': 'population',
                     'CASTHMA_CrudePrev': 'asthma', 'CSMOKING_CrudePrev': 'smoking'}, inplace=True)
data['county'] = data['cname'] + ' ' + data['state']
data.set_index('county', inplace=True)
data.drop(columns=['state', 'cname'], inplace=True)
#print(data)
data.to_csv(fout, encoding='utf-8')
