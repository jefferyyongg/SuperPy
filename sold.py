import csv
import pandas as pd


def rerender_bought(data):
    with open("bought.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in data:
            writer.writerow(line)


def update_sold(args, sold_item):
    with open("sold.csv", 'r') as csv_readfile:
        sold_data = list(csv.reader(csv_readfile))
        data = [len(sold_data), sold_item[0],
                args.sellprice, pd.read_csv("date.csv").columns[0]]
        with open("sold.csv", 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for line in sold_data:
                writer.writerow(line)
            writer.writerow(data)


def sold(args):

    df = pd.read_csv("date.csv")
    name_list = []

    with open("bought.csv", 'r') as csv_file:
        bought_data = list(csv.reader(csv_file))

        for line in bought_data:
            name_list.append(line[1])

        if (any(args.name in x for x in bought_data)):
            for line in bought_data:
                if line[1] == args.name and line[4] < df.columns[0]:
                    print("This product has expired, please try again")
                    return

                if line[1] == args.name and line[2] != "1":
                    sold_item = bought_data[name_list.index(args.name)]
                    line[2] = int(line[2]) - 1
                    rerender_bought(bought_data)
                    update_sold(args, sold_item)

                elif line[1] == args.name and line[2] == "1":
                    sold_item = bought_data[name_list.index(args.name)]
                    bought_data.pop(name_list.index(args.name))
                    rerender_bought(bought_data)
                    update_sold(args, sold_item)

        else:
            print("Sorry, Item not in stock.")
            return
