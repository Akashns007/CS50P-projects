import inflect

p=inflect.engine()
l=[]
i=0
while(True):
    try:
        name=input("Name: ")
        l.append(name)
    except EOFError:
        print()
        break

print("Adieu, adieu, to",p.join(l))
