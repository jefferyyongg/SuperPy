# Imports
import datetime
import csv
import argparse
# Importing pandas for better overview
import pandas as pd

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Top commandline
parser = argparse.ArgumentParser()
parser.add_argument("--advancetime", type=int,
                    help="advance time by x days", default=0)

subparser = parser.add_subparsers(dest="command")

# Sub commandline to add product
buy = subparser.add_parser("buy")
buy.add_argument("--name", type=str, required=True, help="Name of Product")
buy.add_argument("--price", type=float, required=True, help="Price of Product")
buy.add_argument("--exp", type=str, required=True, help="Expiration Date")

# Sub commandline to sell product
sell = subparser.add_parser("sell")
sell.add_argument("--name", type=str, required=True, help="Name of Product")
sell.add_argument("--sellprice", type=str,
                  required=True, help="Product Sell Price")

# Sub commandline to report
report = subparser.add_parser("report")
report.add_argument("--inventory",
                    action="store_true", required=True, help="Show Inventory")
report.add_argument("--now", action="store_true", help="Inventory now")
report.add_argument("--yesterday", action="store_true",
                    help="Inventory yesterday")

args = parser.parse_args()

# TO DO: STRUCTURE TIME OBJECT IN SEPERATE CSV FILE

# AttributeError: 'str' object has no attribute 'strftime'

# Advance date


def set_date(args):
    date = datetime.date.today() + datetime.timedelta(days=args)
    date = datetime.datetime.strftime(date, '%m-%d-%y')

    with open("datetime.csv", "w", newline="") as write_file:
        writer = csv.writer(write_file)
        writer.writerow(
            [date])
    return date

# Get current date from csv file


def get_date():
    with open("datetime.csv", "r") as read_file:
        reader = list(csv.reader(read_file))
        return datetime.datetime.strptime(reader[0][0], '%m-%d-%y').date()


tday = get_date().strftime(
    '%m-%d-%y') if args.advancetime == 0 else set_date(args.advancetime)

# Show inventory function


def show_inventory(args):
    df = pd.read_csv("bought.csv")

    if isinstance(args, datetime.date):
        args = args.strftime('%m-%d-%y')

    print(df[df.buy_date <= args])

# Buy item function(data_list = empty list for checking duplicates)


def buy_item(name, price, exp_date, data_list=[]):

    with open("bought.csv", "r") as read_file:
        # Convert to list for easier accessibility
        data = list(csv.reader(read_file))

        # Appending bought.csv names to empty list
        for line in data[1:]:
            data_list.append(line[1])

        # Appending new item to list if name not in list else adding +1 to existing items amount
        if name not in data_list:
            data.append([len(data), name, 1, price, exp_date, tday])
        else:
            data[data_list.index(
                name) + 1][2] = int(data[data_list.index(name) + 1][2]) + 1

    # Rewriting old file with new updated content
    with open("bought.csv", "w", newline="") as write_file:
        writer = csv.writer(write_file)
        writer.writerows(data)


# Sell item function
def sell_item(name, sellprice, data_list=[]):

    with open("bought.csv", "r") as read_file:

        # Convert to list for easier accessibility
        data = list(csv.reader(read_file))

        # Appending bought.csv names to empty list
        for line in data[0:]:
            data_list.append(line[1])

        with open("sold.csv", "r") as read_sold:
            sold_data = list(csv.reader(read_sold))

            # if name is in bought.csv and amount is higher then 1, remove 1 from amount and add line to sold.csv
            for line in data[1:]:
                if line[1] == name and int(line[2]) > 1:
                    data[data_list.index(
                        name)][2] = int(data[data_list.index(name)][2]) - 1

                    sold_data.append([len(sold_data), name, sellprice, tday])
                # else if name is in bought.csv and amount is equal to 1 remove line from bought.csv and add line to sold.csv
                elif line[1] == name and int(line[2]) == 1:
                    data.pop(int(line[0]))

                    sold_data.append([len(sold_data), name, sellprice, tday])

            # rewrite updated list to csv files
            with open("bought.csv", "w", newline="") as write_file:
                bought_writer = csv.writer(write_file)
                bought_writer.writerows(data)

            with open("sold.csv", "w", newline="") as write_sold:
                writer = csv.writer(write_sold)
                writer.writerows(sold_data)


if args.command == "buy":
    buy_item(args.name, args.price, args.exp)
elif args.command == "sell":
    sell_item(args.name, args.sellprice)
elif args.command == "report" and args.inventory and args.now:
    show_inventory(tday)
elif args.command == "report" and args.inventory and args.yesterday:
    show_inventory(get_date() - datetime.timedelta(days=1))
