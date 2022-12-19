import csv
import datetime


def write_date(date):
    with open("date.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([date])


def set_date(args):
    with open("date.csv", "r") as csv_file:
        reader = list(csv.reader(csv_file))

        if isinstance(args, int):
            if args == 0:
                write_date(str(datetime.datetime.now().date()))
                print("Date reset to:", datetime.datetime.now().date())
            else:
                date = str(datetime.datetime.strptime(
                    reader[0][0], "%Y-%m-%d").date() + datetime.timedelta(days=args))
                write_date(date)
                print("Date set to: ", date)

        elif args == "today":
            write_date(str(datetime.datetime.now().date()))
        elif args == "yesterday":
            write_date(
                str((datetime.datetime.now() - datetime.timedelta(days=1)).date()))
