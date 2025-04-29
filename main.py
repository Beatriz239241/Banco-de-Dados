import pandas as pd 
from sqlalchemy import create_engine

# Nome: Renata Maria Bartholomeu e Beatriz Mari Galvao
# RA: 28316595 / RA: 28307019

# EXTRACT
url = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"
df = pd.read_csv(url)

# TRANSFORM
df = df[df['Country']=='Brazil'].dropna()
df['Toatal Cases'] = df['Confirmed'].cumsum()
print(df.head())

# LOAD
engine = create_engine('sqlite:///covid_data.sqlite')
df.to_sql('brasil_covid', engine, if_exists='replace', index=False)
