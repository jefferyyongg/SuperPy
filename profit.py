import pandas as pd
import calendar


def prof(args):
    bf = pd.read_csv("bought.csv", parse_dates=["buy_date"])
    sf = pd.read_csv("sold.csv", parse_dates=["sell_date"])

    if len(args) <= 7:
        bf.set_index("buy_date", inplace=True)
        sf.set_index("sell_date", inplace=True)

        bought_sum = bf.loc[args[:7], "price"].sum()
        sold_sum = sf.loc[args[:7], "sell_price"].sum()

        print("profit from", calendar.month_name[int(
            args[5:7])] + ":", sold_sum - bought_sum)
    else:
        bought_sum = bf.loc[bf["buy_date"] == args, "price"].sum()
        sold_sum = sf.loc[sf["sell_date"] == args, "sell_price"].sum()

        print("profit from", args + ":", sold_sum - bought_sum)
