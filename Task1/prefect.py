import pandas as pd
from prefect import task, flow

@task
def df_site():
    df = pd.read_csv("original.csv")
    return df

@flow
def process_data():
    res = df_site()
    res['domain_of_url'] = res['url'].map(lambda x: str(x).partition("://")[2].partition("/")[0])
    res.to_csv('norm.csv')
    return res

if __name__ == "__main__":
    process_data()