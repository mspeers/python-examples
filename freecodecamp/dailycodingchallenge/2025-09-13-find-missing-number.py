


'''
Missing Numbers

Given an array of integers from 1 to n, inclusive, return an array of all the missing integers between 1 and n (where n is the largest number in the given array).

    The given array may be unsorted and may contain duplicates.
    The returned array should be in ascending order.
    If no integers are missing, return an empty array.
'''
def find_missing_numbers(arr):
    arr_min = None
    arr_max = None
    arr_sort = sorted(arr)
    if (len(arr)<=0):
        return None
    arr_min = arr_sort[0]
    arr_max = arr_sort[-1]
    
    full = range(arr_min, arr_max)

    filtered_list = [item for item in full if item not in arr]

    return filtered_list

if __name__ == "__main__":
    print(find_missing_numbers([3, 1, 4, 1, 5, 9]))

'''
1. find_missing_numbers([1, 3, 5]) should return [2, 4].
Passed: 2. find_missing_numbers([1, 2, 3, 4, 5]) should return [].
Passed: 3. find_missing_numbers([1, 10]) should return [2, 3, 4, 5, 6, 7, 8, 9].
Passed: 4. find_missing_numbers([10, 1, 10, 1, 10, 1]) should return [2, 3, 4, 5, 6, 7, 8, 9].
Passed: 5. find_missing_numbers([3, 1, 4, 1, 5, 9]) should return [2, 6, 7, 8].
Passed: 6. find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4]) should return [11].
'''



