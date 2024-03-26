import random
while(True):
    try:
        n=int(input("Level: "))
        if n>0:
            r=random.randint(1,n)
            while(True):
                g=int(input("Guess: "))
                if g<r:
                    print("Too small!")
                elif g>r:
                    print("Too large!")
                elif g==r:
                    print("Just right!")
                    exit()
    except ValueError:
                    ...
    else:
        continue

