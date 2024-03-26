from pyfiglet import Figlet
import sys
import random
figlet=Figlet()
a=figlet.getFonts()
sys.argv[2]
if len(sys.argv)==1:
    figlet.setFont(font=random.choice(a))
elif len(sys.argv)==3 :
    if ((sys.argv[1]=="-f" or sys.argv[1]=="--font") and sys.argv[2] in a):
        f=sys.argv[2]
        figlet.setFont(font=f)
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

s=input("Input: ")

print(figlet.renderText(s))