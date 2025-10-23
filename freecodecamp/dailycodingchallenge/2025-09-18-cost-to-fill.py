
'''
Fill The Tank

Given the size of a fuel tank, the current fuel level, and the price per gallon, return the cost to fill the tank all the way.

    tankSize is the total capacity of the tank in gallons.
    fuelLevel is the current amount of fuel in the tank in gallons.
    pricePerGallon is the cost of one gallon of fuel.
    The returned value should be rounded to two decimal places in the format: "$d.dd".
'''
def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    add_fuel = tank_size - fuel_level
    cost_fuel = add_fuel * price_per_gallon
    return f"${cost_fuel:.2f}"



if __name__ == "__main__":
    print(cost_to_fill(20, 0, 4.00))


# Unit tests 
import unittest

'''
1. cost_to_fill(20, 0, 4.00) should return "$80.00".
2. cost_to_fill(15, 10, 3.50) should return "$17.50".
3. cost_to_fill(18, 9, 3.25) should return "$29.25".
4. cost_to_fill(12, 12, 4.99) should return "$0.00".
5. cost_to_fill(15, 9.5, 3.98) should return "$21.89".
'''
class TestSlug(unittest.TestCase):
    def test_sample(self):
        results = [ ((20, 0, 4.00),"$80.00"),
                    ((15, 10, 3.50),"$17.50"),
                    ((18, 9, 3.25),"$29.25"),
                    ((12, 12, 4.99),"$0.00"),
                    ((15, 9.5, 3.98), "$21.89")
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(cost_to_fill(*test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
