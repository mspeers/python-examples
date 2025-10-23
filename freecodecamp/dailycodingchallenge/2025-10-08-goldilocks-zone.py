

import math

def goldilocks_zone(mass):

    # Find the luminosity of the star by raising its mass to the power of 3.5.
    raising_mase = pow(mass, 3.5)
    print("Debug: Raising Mase:"+str(raising_mase))
    # The start of the zone is 0.95 times the square root of its luminosity.
    zone_start = math.sqrt(raising_mase) * 0.95 
    
    # The end of the zone is 1.37 times the square root of its luminosity.
    zone_end = math.sqrt(raising_mase) * 1.37   
    print ("Debug: Zone start:"+str(zone_start)+", end:"+str(zone_end))
    # Return the distances rounded to two decimal places.
    zone_start = round(zone_start, 2)
    zone_end = round(zone_end, 2)

    return [zone_start,zone_end]


if __name__ == "__main__":
    for item in ([1, [0.95, 1.37]],
                [0.5,[0.28, 0.41]]):
        result = goldilocks_zone(item[0])
        print (result)


