

'''
BuzzFizz

Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is correct if:

    Numbers that are multiples of 3 are replaced with "Fizz"
    Numbers that are multiples of 5 are replaced with "Buzz"
    Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
    All other numbers remain as integers in ascending order, starting from 1.
    The array must start at 1 and have no missing or extra elements.

'''

def is_fizz_buzz(a):
    result = True

    for index, item in enumerate(a):
        
        print(f"index:{index+1} item:{item}")
        if (index+1) % 3 == 0:
            if (index+1) % 5 == 0 :
                print("test")
                if item == "FizzBuzz":
                   continue 
            if item == "Fizz":
                continue
            return False
        elif (index+1) % 5 == 0:
            if item == "Buzz":
                print(f"Found Buzz")
                continue
        elif str(index+1) == str(item):
            print("Same Number")
            continue
        else:
            print(f"index {index+1}, item:{item}")
        return False

    return result


'''
1. fizz_buzz(2) should return [1, 2].
2. fizz_buzz(4) should return [1, 2, "Fizz", 4].
3. fizz_buzz(8) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8].
4. fizz_buzz(20) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"].
5. fizz_buzz(50) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"].
'''
if __name__ == "__main__":
    print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]))



