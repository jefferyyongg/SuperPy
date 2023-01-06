# SuperPy Report

### CSV files

The bought.csv and sold.csv files are used to keep track of products and sales. The bought.csv file is used to store information about products that have been added to the inventory, including a unique product id number and the expiration date of the product. This file is also used to generate inventory reports for a specific date and to identify expired products. When a product is sold using the sell parser, the system checks the bought.csv file to confirm that the product is available and not expired. If the product is valid, it is added to the sold.csv file and removed from the bought.csv file. If multiple items of the same product are in stock, the first item listed in the bought.csv file will be selected.

### Use of pandas

I used pandas throughout my whole application, not only because it's easy to use but also because it allows for a lot of functionality with just a few lines of code. as shown in the example below.

Retrieving the users inventory and filtering by date

```
bf = pd.read_csv("bought.csv")
df = pd.read_csv("date.csv")

items = bf.loc[bf["buy_date"] <= df.columns[0]]
```

# Datetime

I have to check multiple times what the type was of the date. String, datetime.datetime object or datetime.date object. I have chosen to pass a datetime.date object to my functions that uses the dates arguments of subparsers. Because other wise you convert the dates over and over. This way it was more clear for my what to expect and where/when to convert. And you need a datetime.date object for the best date comparison.

```
if args.parser == "revenue" and args.date:
    rev(args.date)
elif args.parser == "revenue" and args.today:
    rev(str(datetime.datetime.now().date()))
elif args.parser == "revenue" and args.yesterday:
    rev(str((datetime.datetime.now() - datetime.timedelta(days=1)).date()))
```
