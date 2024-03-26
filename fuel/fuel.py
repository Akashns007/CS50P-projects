def main():
    fraction=input("Fraction: ")
    percentage=convert(fraction)
    print(gauge(percentage))


def convert(fraction):
     while True:

        try:
            x,z=fraction.split("/")
            x=int(x)
            z=int(z)
            f=x/z
            if f<=1:
                p= int(f*100)
                return p
            else:
                fraction=input("Fraction: ")
                pass

        except (ValueError,ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage<=1:
        return "E"
    elif(percentage>=99):
        return "F"
    else:
        return str(percentage)+"%"

if __name__ == "__main__":
    main()



