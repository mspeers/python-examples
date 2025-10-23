

import math

def send_message(route):
    if type(route) != list:
        return -1
    total = 0
    count = 0
    trans_delay = .5

    for distances in route:
        total += distances
        count += 1

    # The first value in the array is the distance from your location to the first satellite.
    # Each subsequent value, except for the last, is the distance to the next satellite.
    # The last value in the array is the distance from the previous satellite to your home planet.
    # The message travels at 300,000 km/s.
    # Each satellite the message passes through adds a 0.5 second transmission delay.
    # Return a number rounded to 4 decimal places, with trailing zeros removed
    avg =  total
    print("Math:"+str(avg))
    print("(total:"+str(total)+ "/count:"+str(count)+") / 3000000") 
    number = (avg) / 300000
    number = round(number, 4)
    total_delay = (trans_delay * (count -1))
    print("Delay "+str(total_delay))
    number += total_delay
    return number

if __name__ == "__main__":
    print(send_message([300000, 300000]))


