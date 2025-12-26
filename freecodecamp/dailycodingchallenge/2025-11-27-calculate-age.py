

'''
What's My Age Again?

Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

    Assume all birthdays are valid dates before November 27th, 2025.
    Return the age as an integer.
    Be sure to account for whether the person has already had their birthday in 2025.

'''


def calculate_age(birthday):
    year, mon, day = birthday.split('-')
    result = 2025 - int(year)
    if int(mon) - 11 > 0:
        result -= 1
    elif int(mon) - 11 == 0 and int(day) - 27 >0:
        result -= 1



    return result


if __name__ == "__main__":
    print(calculate_age("1994-12-14"))



