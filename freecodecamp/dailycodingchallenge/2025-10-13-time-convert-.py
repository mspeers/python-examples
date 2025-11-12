

import re
'''
24 to 12

Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

    The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".

'''
def to_12(time):
    print("start")
    time_values = re.search(r"(\d{2})(\d{2})",time)
    if not time_values:
        print ("Invalided Time format (HHMM):"+time)
    print(time_values)
    hour = int(time_values.group(1))
    mins = int(time_values.group(2))
    zone = "AM"
    if (hour > 12):
        zone = "PM"
        hour -= 12
    elif (hour == 0):
        hour = 12
    print("hour:"+str(hour) + ", mins:"+str(mins))
 
    result = f"{hour}:{mins:02d} {zone}"

    return result

if __name__ == "__main__":
    print(to_12("0900"))


'''
1. to_12("1124") should return "11:24 AM".
2. to_12("0900") should return "9:00 AM".
3. to_12("1455") should return "2:55 PM".
4. to_12("2346") should return "11:46 PM".
5. to_12("0030") should return "12:30 AM".'''