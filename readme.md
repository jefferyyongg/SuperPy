# SuperPy

### The Assignment:

A large supermarket chain has asked you to write a command-line tool that is able to keep track of their inventory: they want to call it SuperPy. The core functionality is about keeping track and producing reports on various kinds of data:

Which products the supermarket offers;

- How many of each type of product the supermarket holds currently;
- How much each product was bought for, and what its expiry date is;
- How much each product was sold for or if it expired, the fact that it did;
- All data must be saved in CSV files.

There are three important modules from the standard library you must use for this:

- csv -- CSV File Reading and Writing
- argparse -- Parser for command-line options, arguments and subcommands
- datetime -- Basic date and time types
  This is SuperPy's user guide. SuperPy let's you manage your supermarket's inventory by purchasing and selling products, and generating inventory, expired product and revenue/profit reports.

### Third party libraries that you should install

# PrettyTable

```
pip install prettytable
```

# Matplotlib

```
pip install install matplotlib
```

### Command Usage:

# Helper

At the start of a new SuperPy session you should run this command for helper instructions:

```
python main.py -h
```

# Advance_time

With the "-a" or "--advancetime" command you can modify the current date. Use a positive value for dates in the future, a negative value for dates in the past.

To shift the date 1 day forward

```
python main.py -a 1
```

To shift the day 1 day backwards

```
python main.py -a -1
```

To reset the date to today's actual date

```
python main.py -a 0
```

### Buy

By default the buying date is set to the current day. To use another date for buying you can use the "advance_time" command to change the current date as seen in section #Advance_time.

With the buy command you can add a product to the stock.
Submit the productname, the price for which it is bought and the expiration date:

```
python main.py buy -n Kwark -p 1 -e (yyyy-mm-dd)
```

### Sell

To sell a product enter the productname and the sellprice for which it is sold:

```
python main.py sell -n Kwark -s 5
```

### Inventory

Prints all products in stock.
To print the inventory for the current day:

```
python main.py inventory
```

Use "-t" or "-y" to print the inventory for today or yesterday:

```
python main.py inventory -t/-y
```

# export

To export a report of expired products. By default it uses the current day as date.
To export the inventory for the current day:

```
python main.py inventory -e/--expired
```

### Revenue

Prints a revenue report. By default it uses the current day as date.
To print the revenue of the current day.

```
python main.py revenue
```

Use "-d" or "--date" to print the revenue for another date (yyyy-mm-dd) or (yyyy-mm) for monthly revenue.

```
python main.py revenue -d  2022-12-15
```

To print a graph for monthly revenue use -s/--stats (yyyy-mm)

```
python main.py revenue -s  2022-12
```

### Profit

Prints a profit report. By default it uses the current day as date.
To print the profit of the current day.

```
python main.py profit
```

Use "-d" or "--date" to print the profit for another date (yyyy-mm-dd) or (yyyy-mm) for monthly profit.

```
python main.py profit -d  2022-12-28
```
