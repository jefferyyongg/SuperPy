import csv
import datetime
import pandas as pd


def bought(args):

    with open("bought.csv", 'r') as csv_file:
        bought_data = list(csv.reader(csv_file))

        data = [int(bought_data[-1][0]) + 1, args.name, 1, args.price,
                args.exp, pd.read_csv("date.csv").columns[0]]

        with open("bought.csv", 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)

            # if item name already exists in list then add 1 to amount
            if (any(args.name in x for x in bought_data)):
                for line in bought_data:
                    if line[1] == args.name:
                        line[2] = int(line[2]) + 1

                        for line in bought_data:
                            writer.writerow(line)

            else:
                for line in bought_data:
                    writer.writerow(line)
                writer.writerow(data)
