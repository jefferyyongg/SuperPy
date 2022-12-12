import pandas as pd
import datetime


def inv():
    bf = pd.read_csv("bought.csv")
    df = pd.read_csv("date.csv")
    print(bf.loc[bf["buy_date"] <= df.columns[0]])
