

''' launch_fuel Space Week Day 7: Launch Fuel
For the final day of Space Week, you will be given the mass in kilograms (kg) of a payload you want to send to orbit. Determine the amount of fuel needed to send your payload to orbit using the following rules:
'''
def launch_fuel(payload):

    # Rockets require 1 kg of fuel per 5 kg of mass they must lift.
    fuel = payload / 5
    # Fuel itself has mass. So when you add fuel, the mass to lift goes up, which requires more fuel, which increases the mass, and so on.
    total_fuel_mass = (fuel) /5 
    current_fuel_mass = total_fuel_mass
    while  current_fuel_mass > 1:  # This is the condition
        current_fuel_mass = current_fuel_mass / 5 
        if current_fuel_mass > 1:
            print(f"Current fuel mass adding: { current_fuel_mass}")
            total_fuel_mass += current_fuel_mass 
    total_fuel_mass = round(total_fuel_mass, 1)
    # To calculate the total fuel needed: start with the payload mass, calculate the fuel needed for that, add that fuel to the total mass, and calculate again. Repeat this process until the additional fuel required is less than 1 kg, then stop
    total_mass = payload + fuel + total_fuel_mass

    print("Total Mass:"+ str(total_mass)+ ", payload:"+ str(payload) + ", fuel:" + str(fuel)+ ", total fuel mass:"+ str(total_fuel_mass))


    total_fuel = (payload  + fuel + total_fuel_mass) /5.0
    print (total_fuel)
    total_fuel = round(total_fuel, 1)
    # Ignore the mass of the rocket itself. Only compute fuel neede


    return total_fuel

if __name__ == "__main__":
    print(launch_fuel(243))


