import random

def main():
    level=get_level()
    s=generate_integer(level)
    print(f"Score: {s}")


def get_level():
    while(True):
        try:
            l=input("Level: ")
            if l not in ["1","2","3"]:
                continue
            else:
                return l
        except [ValueError,NameError]:
            continue

def generate_integer(level):
    flag=0
    score=0
    for i in range(10):
        if level=="1":
            x=random.randint(0b,9)
            y=random.randint(0,9)
            sum=x+y
        elif level=="2":
            x=random.randint(10,99)
            y=random.randint(10,99)
            sum=x+y
        else:
            x=random.randint(100,999)
            y=random.randint(100,999)
            sum=x+y
        for _ in range(3):
            try:
                print(x,"+",y,"= ", end="")
                su=input()
                if su==str(x+y):
                    score+=1
                    break
                else:
                    print("EEE")
                    if _==2:
                        print(x,"+",y,"=",sum)
                    continue
            except ValueError:
                continue


    return score


if __name__ == "__main__":
    main()