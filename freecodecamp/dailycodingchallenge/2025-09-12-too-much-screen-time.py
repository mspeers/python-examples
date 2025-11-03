

'''
Screen Time

Given an input array of seven integers, representing a week's time, where each integer is the amount of hours spent on your phone that day, determine if it is too much screen time based on these constraints:

    If any single day has 10 hours or more, it's too much.
    If the average of any three days in a row is greater than or equal to 8 hours, it?s too much.
    If the average of the seven days is greater than or equal to 6 hours, it's too much.
'''
def too_much_screen_time(hours):
    
    hours_sum = 0
    hours_three_days_sum = 0
    for index, hour in enumerate(hours):
        hours_three_days_sum += hour
        hours_sum += hour
        
        if hour >= 10:
            return True
        if index >= 3:
            
            hours_three_days_sum -= hours[index-3] 
            # print(f"{hours_three_days_sum /3 }, {hours_three_days_sum}, {hours[index-3]}")
            if (hours_three_days_sum /3 ) >= 8:
                return True

    if (hours_sum/len(hours)) >= 6:
        return True


    return False

if __name__ == "__main__":
    print(too_much_screen_time([1, 2, 3, 10, 2, 1, 0]))
'''
1. too_much_screen_time([1, 2, 3, 4, 5, 6, 7]) should return False.
Passed: 2. too_much_screen_time([7, 8, 8, 4, 2, 2, 3]) should return False.
Passed: 3. too_much_screen_time([5, 6, 6, 6, 6, 6, 6]) should return False.
Passed: 4. too_much_screen_time([1, 2, 3, 11, 1, 3, 4]) should return True.
Passed: 5. too_much_screen_time([1, 2, 3, 10, 2, 1, 0]) should return True.
Passed: 6. too_much_screen_time([3, 3, 5, 8, 8, 9, 4]) should return True.
Passed: 7. too_much_screen_time([3, 9, 4, 8, 5, 7, 6]) should return True.
'''



