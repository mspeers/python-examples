

''' 
Space Week Day 7: Launch Fuel

For the final day of Space Week, you will be given the mass in kilograms (kg) of a payload you want to send to orbit. Determine the amount of fuel needed to send your payload to orbit using the following rules:

    Rockets require 1 kg of fuel per 5 kg of mass they must lift.
    Fuel itself has mass. So when you add fuel, the mass to lift goes up, which requires more fuel, which increases the mass, and so on.
    To calculate the total fuel needed: start with the payload mass, calculate the fuel needed for that, add that fuel to the total mass, and calculate again. Repeat this process until the additional fuel required is less than 1 kg, then stop.
    Ignore the mass of the rocket itself. Only compute fuel needed to lift the payload and its own fuel.

For example, given a payload mass of 50 kg, you would need 10 kg of fuel to lift it (payload / 5), which increases the total mass to 60 kg, which needs 12 kg to lift (2 additional kg), which increases the total mass to 62 kg, which needs 12.4 kg to lift - 0.4 additional kg - which is less 1 additional kg, so we stop here. The total mass to lift is 62.4 kg, 50 of which is the initial payload and 12.4 of fuel.

    Return the amount of fuel needed rounded to one decimal place.
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

# Unit tests 
import unittest

'''
1. launch_fuel(50) should return 12.4.
2. launch_fuel(500) should return 124.8.
3. launch_fuel(243) should return 60.7.
4. launch_fuel(11000) should return 2749.8.
5. launch_fuel(6214) should return 1553.4.
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ (50, 12.4),
                    (500, 124.8),
                    (243, 60.7),
                    (11000, 2749.8),
                    (6214, 1553.4),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(launch_fuel(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")
