

import re
'''
Weekday Finder

Given a string date in the format YYYY-MM-DD, return the day of the week.

Valid return days are:

    "Sunday"
    "Monday"
    "Tuesday"
    "Wednesday"
    "Thursday"
    "Friday"
    "Saturday"

Be sure to ignore time zones.
Formal: (Year Code + Month Code + Century Code + Date Number - Leap Year Code) mod 7

Year: (YY + (YY div 4)) mod 7

'''
def get_weekday(date_string):

    day_of_week_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    date_groups = re.search("(\d{4})-(\d{2})-(\d{2})", date_string)
    year_str, mon_str, day_str = date_groups.groups()
    year, mon, day = int(year_str), int(mon_str), int(day_str)
    print (f"year:{year}, mon:{mon}, day:{day}")

    # month
    mon_values = {  1:0, #January 
                    2:3, #Feb
                    3:3, 
                    4:6,
                    5:1,
                    6:4,
                    7:6,
                    8:2,
                    9:5,
                    10:0,
                    11:3,
                    12:5
    }
    print (f"day:{day}")

    # use last year before March
    year -= mon < 3

    # find leap years stuff  
    leap = int(year / 4) - int(year / 100) + int(year / 400)

    print(f"Leap years:{year}(year) + {leap}(leap) + {mon_values[mon]}(month) + {day}(day)")
    
    main_math = ( year + leap + mon_values[mon] + day)

    cur_years = (main_math % 7)

    print(f"cur_years:{cur_years}({day_of_week_names[cur_years-1]})")

    return day_of_week_names[cur_years-1]

'''
1. get_weekday("2025-11-06") should return Thursday.
2. get_weekday("1999-12-31") should return Friday.
3. get_weekday("1111-11-11") should return Saturday.
4. get_weekday("2112-12-21") should return Wednesday.
5. get_weekday("2345-10-01") should return Monday.
'''    


if __name__ == "__main__":
    print(get_weekday("2025-11-06"))
    print(get_weekday("1999-12-31"))



