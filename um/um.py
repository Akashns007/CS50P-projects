import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    txt = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    if txt:
        return len(txt)
    else:
        return 0


if __name__ == "__main__":
    main()
