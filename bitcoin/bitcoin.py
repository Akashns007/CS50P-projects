import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        n=float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    request=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data=request.json()
    price=data["bpi"]["USD"]["rate"]
    price=float(price.replace(",",""))
    price=float(price*n)
    print(f"${price:,.4f}")

