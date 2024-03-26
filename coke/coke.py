
amtdue=50
totamt=0
print("Amount Due: 50")

while(True):

    ia=int(input("Insert Coin: "))
    if (ia == 25 or ia==10 or ia==5) :
        totamt=totamt+ia
        amtdue=amtdue-ia
        if (amtdue>=0):
            print("Amount Due:",amtdue)
        if(totamt>=50):
            print(f"Change Owed: {totamt-50}")
            break

    else:
        print(f"Amount Due: {amtdue}")






