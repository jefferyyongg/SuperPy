# Imports
import argparse
import csv
import datetime

from bought import bought
from sold import sold
from inventory import inv
from set_date import set_date
from revenue import rev
from profit import prof
from graph import graph

# DONE
# PARSER FUNCTIONALITY
# BUY FUNCTIONALITY
# SELL FUNCTIONALITY
# SET_DATE FUNCTIONALITY
# INVENTORY FUNCTIONALITY
# FINISH REVENUE & REPORT FUNCTIONALITY
# ALL FUNCTIONS HAVE TO WORK WITH FILTERING WITH DATETIME BY MONTH
# ADD 2 ADDITIONAL FEATURES (MATPLOTLIB, Pandas)

# STILL TO DO:


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="parser")

advancetime = parser.add_argument("-a", "--advancetime", type=int,
                                  help="advances time by x amount of days (enter 0 to reset date)")

inventory = subparser.add_parser(
    "inventory", help="-t/--today for today's date or -y/--yesterday for yesterday's date")
inventory.add_argument("-t", "--today", action="store_true", required=False)
inventory.add_argument("-y", "--yesterday",
                       action="store_true", required=False)

# Sub commandline to buy product
buy = subparser.add_parser("buy")
buy.add_argument("-n", "--name", required="true",
                 type=str, help="Name of Product")
buy.add_argument("-p", "--price", required="true",
                 type=float, help="Price of Product")
buy.add_argument("-e", "--exp", required="true",
                 type=str, help="Expiration Date")

# Sub commandline to sell product
sell = subparser.add_parser("sell")
sell.add_argument("-n", "--name", required="true",
                  type=str, help="Name of Product")
sell.add_argument("-s", "--sellprice", required="true",
                  type=str, help="Product Sell Price")

revenue = subparser.add_parser(
    "revenue", help="-d/--date to filter by date (yyyy-mm) or -t/--today for today's date or -s/--stats for graph")
revenue.add_argument("-d", "--date", type=str,
                     help="input date as following (yyyy-mm)")
revenue.add_argument("-t", "--today", action="store_true", required=False)
revenue.add_argument("-y", "--yesterday", action="store_true", required=False)
revenue.add_argument("-s", "--stats", type=str,
                     required=False, help="show graph for following dates (yyyy-mm)")

profit = subparser.add_parser(
    "profit", help="-d/--date to filter by date (yyyy-mm) or -y/--yesterday for yesterday's date")
profit.add_argument("-d", "--date", type=str,
                    help="input date as following (yyyy-mm)")
profit.add_argument("-t", "--today", action="store_true", required=False)
profit.add_argument("-y", "--yesterday", action="store_true", required=False)

args = parser.parse_args()


def main():
    if args.advancetime or args.advancetime == 0:
        set_date(args.advancetime)

    if args.parser == "buy":
        bought(args)
    elif args.parser == "sell":
        sold(args)

    if args.parser == "inventory" and args.today:
        set_date("today")
        inv()
    elif args.parser == "inventory" and args.yesterday:
        set_date("yesterday")
        inv()
    elif args.parser == "inventory":
        inv()

    if args.parser == "revenue" and args.date:
        rev(args.date)
    elif args.parser == "revenue" and args.today:
        rev(str(datetime.datetime.now().date()))
    elif args.parser == "revenue" and args.yesterday:
        rev(str((datetime.datetime.now() - datetime.timedelta(days=1)).date()))
    elif args.parser == "revenue" and args.stats:
        graph(args.stats)
    elif args.parser == "revenue":
        rev(str(datetime.datetime.now().date()))

    if args.parser == "profit" and args.date:
        prof(args.date)
    elif args.parser == "profit" and args.today:
        prof(str(datetime.datetime.now().date()))
    elif args.parser == "profit" and args.yesterday:
        prof(str((datetime.datetime.now() - datetime.timedelta(days=1)).date()))
    elif args.parser == "profit":
        prof(str(datetime.datetime.now().date()))


if __name__ == "__main__":
    main()
