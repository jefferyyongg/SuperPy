import pandas as pd
import calendar


def rev(args):
    sf = pd.read_csv("sold.csv", parse_dates=["sell_date"])
    sf.set_index("sell_date", inplace=True)
    print("Revenue", calendar.month_name[int(
        args[-2:])] + ":", sf.loc[args[:7], "sell_price"].sum())
