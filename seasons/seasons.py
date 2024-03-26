from datetime import date
import sys
import re
import inflect


def main():
    p = inflect.engine()
    try:
        year, month, day = birthday_check(input("Date of Birth: "))
    except:
        sys.exit("Invalid Date")
    dob = date(int(year), int(month), int(day))
    dot = date.today()
    diff = dot - dob
    tot_min = diff.days*24*60     #diff.days to access the output in number of days
    num_to_words = p.number_to_words(tot_min, andword="")
    print(num_to_words.capitalize() + " minutes")



def birthday_check(bd):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", bd):
        try:
            year, month, day = bd.split("-")

        except:
            sys.exit("Invalid Date")
        return year,month,day
    else:
        return None


if __name__ == "__main__":
    main()
