m=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date=input("Date: ").title().lstrip(" ").rstrip(" ")
        if "/" in date:
            month,day,year=date.split("/")
        elif "," in date:
            date=date.replace(",","")
            month,day,year=date.split(" ")
            if month in m:
                month=m.index(month)+1
        month=int(month)
        day=int(day)
        if month<=12 and day<=31:
            break
        else:
            continue
    except ValueError:
        continue
    except NameError:
        continue



print(f"{year}-{month:02}-{day:02}")
