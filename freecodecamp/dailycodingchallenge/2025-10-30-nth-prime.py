


# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

'''
Nth Prime

A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers are 2, 3, 5, 7, and 11.

Given a positive integer n, return the nth prime number. For example, given 5 return the 5th prime number: 11.
'''
def nth_prime(n):
    count = 0  # Count of prime numbers found
    num = 1  # Starting number to check
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num


'''
1. nth_prime(5) should return 11.
2. nth_prime(10) should return 29.
3. nth_prime(16) should return 53.
4. nth_prime(99) should return 523.
5. nth_prime(1000) should return 7919.
'''



