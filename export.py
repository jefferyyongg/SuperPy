import pandas as pd


def export():
    bf = pd.read_csv("bought.csv")
    df = pd.read_csv("date.csv")
    fl = bf.loc[bf["exp"] <= df.columns[0]]
    fl.to_csv("expired.csv")
    print("Exported all expired products to expired.csv")
