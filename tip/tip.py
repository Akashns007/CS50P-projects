def main():
    #taking the inputs
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    #calculating the tip
    tip = dollars * percent
    #printing the out put
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #removing the doller symbol
    d=d.lstrip("$")
    #retuening the float value of d
    return float(d)



def percent_to_float(p):
    #removing the percentage symbol
    p=p.rstrip("%")
    #converting to float
    p=float(p)
    # returning

    return p/100



main()