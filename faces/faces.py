def main():
    #Taking the Input
    sentence=input()
    #Printing the output
    print(convert(sentence))


def convert(s):
    #replacing the emoticons with the emojis
    s=s.replace(":)","🙂").replace(":(","🙁")
    #returning the the sentence
    return s

#closing the main function
main()