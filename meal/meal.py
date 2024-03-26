def main():
    time=input("What time is it? ")
    i=convert(time)
    if (i>=7 and i<=8):
        print("breakfast time")
    elif(i>=12 and i<=13):
        print("lunch time")
    elif(i>=18 and i<=19):
        print("dinner time")
    else:
        print("no")



def convert(time):

    hours,minutes=time.split(":")
    hours= float(hours) + (float(minutes) / 60)
    return hours



if __name__ == "__main__":
    main()