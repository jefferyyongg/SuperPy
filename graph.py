import pandas as pd
import matplotlib.pyplot as plt
import calendar


def graph(args):
    sf = pd.read_csv("sold.csv", parse_dates=["sell_date"])

    sf.set_index("sell_date", inplace=True)
    rv = list(sf.loc[args[:7], "sell_price"])
    dates = list(sf.loc[args[:7], "sell_price"].index)
    data = sorted([list(x) for x in zip(dates, rv)])

    pltx = []
    plty = []

    for x in data:
        pltx.append(x[0])
        plty.append(x[1])

    plt.title("Revenue from " + calendar.month_name[int(args[-2:])])
    plt.xlabel("Days")
    plt.ylabel("Revenue")

    plt.plot_date(pltx, plty, linestyle="solid")
    plt.gcf().autofmt_xdate()
    plt.show()
