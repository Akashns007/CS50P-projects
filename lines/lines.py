import sys

if len(sys.argv)==2:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    try:
        with open(sys.argv[1]) as file:
            n=0
            for line in file:
                if not line.lstrip().startswith("#") and line.lstrip()!='':
                    n+=1
        print(n)
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments")





