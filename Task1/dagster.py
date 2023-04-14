import pandas as pd
from dagster import asset

@asset
def df_site() -> None: 
    df = pd.read_csv("original.csv")
    df['domain_of_url'] = df['url'].map(lambda x: str(x).partition("://")[2].partition("/")[0])
    df.to_csv('norm.csv')