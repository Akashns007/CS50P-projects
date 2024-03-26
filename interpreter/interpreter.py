x,y,z=input("expression: ").split(" ")
x=float(x)
z=float(z)
match y:
    case "+" :
        res=x+z
        print(res)
    case "/" :
        res=x/z
        print(res)
    case "*" :
        res=x*z
        print(res)
    case "-" :
        res=x-z
        print(res)
    case _:
        exit
