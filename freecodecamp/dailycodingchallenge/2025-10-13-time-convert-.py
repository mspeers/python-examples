

import re

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


