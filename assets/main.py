import requests
import pandas as pd
import json

uri = 'https://api.football-data.org/v4/competitions/CL'
headers = { 'X-Auth-Token': 'd7447b0785204361b17856542f0402ea' }

response = requests.get(uri, headers=headers)


data = response.json()['matches']

df = pd.json_normalize(data)

df.to_csv('./assets/data.csv')
  
  
