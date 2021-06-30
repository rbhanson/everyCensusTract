#This program is designed to pull Census variables for every tract in the U.S.
#This program is a workaround for limitations of the Census API.

import requests, pandas as pd, os, glob

#Census variables to look up

variables = 'DP03_0062E'

statesFIPs = ['01','02','04','05','06','08','09','10','12','13','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','44','45','46','47','48','49','50','51','53','54','55','56']

callPart1 = 'https://api.census.gov/data/2019/acs/acs5/profile?get=GEO_ID,'

callPart2 = ',NAME&for=TRACT:*&in=state:'

callPart3 = '&key=PUTYOURKEYHERE'

path = r'C:\Users\ryan.hanson\OneDrive - City of Memphis\Desktop\Playground\censusFiles\state'

for x in range(len(statesFIPs)):
    url = callPart1 + variables + callPart2 + statesFIPs[x] +callPart3
    df = pd.read_json(url)
    df.head(10)
    df.to_csv(path + statesFIPs[x]+ '.csv', header=None, index=False)
    #r = requests.get(url)
    #print(r)
    #print(url)

os.chdir(r'C:\Users\ryan.hanson\OneDrive - City of Memphis\Desktop\Playground\censusFiles')
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
