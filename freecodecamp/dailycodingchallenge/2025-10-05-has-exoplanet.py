

import math

def has_exoplanet(readings):
    readings_val = []
    for read in readings:
        # print(read.upper())
        read_val = ord(read.upper()) -48
        # print("char:"+str(read_val))
        if read_val > 10:
            read_val -= 7
        # print("char second:"+str(read_val))
        readings_val.append(read_val)
    
    avg = sum(readings_val) / (len(readings_val))
    avg_80 = avg * 0.8

    for read in readings_val:
        print("read:"+ str(read)+", Avg:"+str(avg)+ ", Avg 80%:"+str(avg_80))
        if avg_80 >= read:
            return True
    return False
  
if __name__ == "__main__":
    print(has_exoplanet("665544554"))
    print(has_exoplanet("FGFFCFFGG"))
    # print( has_exoplanet("MONOPLONOMONPLNOMPNOMP"))
    # print(has_exoplanet("FREECODECAMP") )


