

'''
Thermostat Adjuster 2

Given the current temperature of a room in Fahrenheit and a target temperature in Celsius, return a string indicating how to adjust the room temperature based on these constraints:

    Return "Heat: X degrees Fahrenheit" if the current temperature is below the target. With X being the number of degrees in Fahrenheit to heat the room to reach the target, rounded to 1 decimal place.
    Return "Cool: X degrees Fahrenheit" if the current temperature is above the target. With X being the number of degrees in Fahrenheit to cool the room to reach the target, rounded to 1 decimal place.
    Return "Hold" if the current temperature is equal to the target.

To convert Celsius to Fahrenheit, multiply the Celsius temperature by 1.8 and add 32 to the result (F = (C * 1.8) + 32).
'''

def adjust_thermostat(current_f, target_c):
    results = ["Heat","Cool","Hold"]
    degress_f_msg = "degrees Fahrenheit"
    result_msg = ""
    
    adjuster = 0

    # Change current f to c
    step1 = current_f - 32
    current_c = 0
    current_c_f = 0
    if (step1 != 0):
        # print ("Not Zero")
        current_c_f = step1 / 1.8
          
    current_c = current_c_f
    print(f"current_c: {current_c}, current_c_f:{current_c_f} target_c:{target_c}, current_f:{current_f}, step1:{step1}")
    
    adjuster = round((target_c - current_c) * 1.8,1)

    if (adjuster > 0 ):
        result_msg += results[0]
    elif (adjuster < 0):
        result_msg += results[1]
    
    if (adjuster == 0):
        return results[2]

    return f"{result_msg}: {abs(adjuster)} {degress_f_msg}"


    


if __name__ == "__main__":
    print(adjust_thermostat(32, 0))
    print(adjust_thermostat(70, 25))
    print(adjust_thermostat(72, 18))


