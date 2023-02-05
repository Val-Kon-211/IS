import pandas as pd
from dagster import asset

@asset
def df_site() -> None: 
    df = pd.read_csv("original.csv")
    print(df)
    df['domain_of_url'] = df['url'].map(lambda x: str(x).partition("://")[2].partition("/")[0])
    print(df)
    df.to_csv('norm.csv')