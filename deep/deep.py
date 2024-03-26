ans=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
if (ans=="42"):
    print("yes")
elif(ans=="forty-two"):
    print("yes")
elif(ans=="forty two"):
    print("yes")
elif(ans=="Forty two"):
    print("yes")
else:
    print("no")