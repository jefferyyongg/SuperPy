import pandas as pd
import calendar


def rev(args):
    sf = pd.read_csv("sold.csv", parse_dates=["sell_date"])

    if len(args) <= 7:
        sf.set_index("sell_date", inplace=True)

        print("Revenue from", calendar.month_name[int(
            args[5:7])] + ":", sf.loc[args[:7], "sell_price"].sum())
    else:
        print("Revenue from", args + ":",
              sf.loc[sf["sell_date"] == args, "sell_price"].sum())
