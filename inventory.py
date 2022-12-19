import pandas as pd
from prettytable import PrettyTable

table = PrettyTable()


def inv():
    bf = pd.read_csv("bought.csv")
    df = pd.read_csv("date.csv")

    table.field_names = list(bf.columns[:])

    items = bf.loc[bf["buy_date"] <= df.columns[0]]
    for line in items.iterrows():
        table.add_row(list(line[1][:]))

    print(table)
