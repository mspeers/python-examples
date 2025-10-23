

from re import sub

'''
Tip Calculator

Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.

    Prices will be given in the format: "$N.NN".
    Custom tip percents will be given in this format: "25%".
    Return amounts in the same "$N.NN" format, rounded to two decimal places.

For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].
'''

def calculate_tips(meal_price, custom_tip):
    results = []

    percets = [0.15,0.20]
    # custom Tip
    
    custom_tip = float(sub(r'[^\d.]', '', custom_tip)) /100

    print (custom_tip)
    price =float(sub(r'[^\d.]', '', meal_price))

    percets.append(custom_tip)
    for cur_percet in percets:
        percet_new = round(price * cur_percet,2)
        results.append("$"+"{:.2f}".format(percet_new))

    

    return results

if __name__ == "__main__":
    print(calculate_tips("$10.00", "25%"))
    print(calculate_tips("$89.67", "26%"))
    print(calculate_tips("$19.85", "9%"))


