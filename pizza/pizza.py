import sys
from tabulate import tabulate
import csv

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

menu=[]

try:
    with open(sys.argv[1],"r")as file:
        reader=csv.reader(file)
        for type,small,large in reader:
            menu.append({"type" : type ,"small" : small , "large" : large})

    table=[]
    for row in menu[1:]:
        table.append(row.values())
    header=[menu[0]["type"],menu[0]["small"],menu[0]["large"]]
    print(header)
    print(table)
    print(tabulate(table,header, tablefmt="grid"))



except FileNotFoundError:
    sys.exit("File does not exist")


