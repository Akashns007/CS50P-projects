d={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
try:
    total=0
    while(True):
        item = input("Item: \n").title()
        if item in d.keys():
            total=total+d.get(item)
            print(f"Total: ${'%.2f'%total}")
        else:
            continue
except EOFError:
    pass
except KeyError:
    pass