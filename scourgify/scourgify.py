import csv
import sys

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")

if not (sys.argv[2].endswith(".csv") and sys.argv[1].endswith(".csv")):
    sys.exit("not a csv file")

try:
    with open(sys.argv[1]) as file:
        reader=csv.DictReader(file)
        with open(sys.argv[2],'w') as output:
            writer=csv.DictWriter(output, fieldnames=["first","last","house"])
            writer.writeheader()
            for row in reader:
                row['first']=row.pop("name")
                lname,fname=row['first'].split(", ")
                row["first"]=fname
                row["last"]=lname
                writer.writerow(row)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.agrv[1]}")










