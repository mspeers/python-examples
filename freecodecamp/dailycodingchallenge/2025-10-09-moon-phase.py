

from datetime import datetime

def moon_phase(date_string):

    date_format = "%Y-%m-%d"

    d0 = datetime.strptime("2000-01-05", date_format)
    d1 = datetime.strptime(date_string, date_format)
    delta = d1 - d0
    rem_days = delta.days % 28

    moon_name = "New"
    match rem_days:
        case rem_days if 8 <= rem_days <=  14:
            moon_name = "Waxing"
        case rem_days if 15 <= rem_days <=  21:
            moon_name = "Full"
        case rem_days if 22 <= rem_days <=  29:
            moon_name = "Waning"

    return moon_name

if __name__ == "__main__":
    print (moon_phase("2014-10-15"))


