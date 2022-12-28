import csv
import datetime
import pandas as pd


def bought(args):

    date = pd.read_csv("date.csv").columns[0]

    with open("bought.csv", 'r') as csv_file:
        bought_data = list(csv.reader(csv_file))

        data = [int(bought_data[-1][0]) + 1, args.name, 1, args.price,
                args.exp, date]

        with open("bought.csv", 'w', newline="") as write_file:
            writer = csv.writer(write_file)

            for line in bought_data:
                # for every item if name == args.name AND exp/buy_date == exp/buy_date.args add 1 to amount
                if line[1] == args.name and line[4] == args.exp and line[5] == date:
                    print("add 1 to amount")
                    line[2] = int(line[2]) + 1

                    # rerender bought csv file
                    for d in bought_data:
                        writer.writerow(d)
                    return

            # else add new item and rerender csv file
            for item in bought_data:
                writer.writerow(item)
            writer.writerow(data)
