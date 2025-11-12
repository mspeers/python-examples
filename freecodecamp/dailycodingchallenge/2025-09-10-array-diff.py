'''
Array Diff

Given two arrays with strings values, return a new array containing all the values that appear in only one of the arrays.

    The returned array should be sorted in alphabetical order.

'''
def array_diff(arr1, arr2):

    results = []
    rigth_left = [items for items in arr2 if items not in arr1]
    if len(rigth_left) > 0:
        results += rigth_left
    left_rigth = [items for items in arr1 if items not in arr2]   
    if len(left_rigth) > 0:
        results += left_rigth
    
    return sorted(results)

if __name__ == "__main__":
    print(array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]))


'''
1. array_diff(["apple", "banana"], ["apple", "banana", "cherry"]) should return ["cherry"].
2. array_diff(["apple", "banana", "cherry"], ["apple", "banana"]) should return ["cherry"].
3. array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]) should return ["eight", "four", "six", "two"].
4. array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]) should return ["five", "one", "seven", "three"].
5. array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]) should return ["freeCodeCamp", "rocks"].
'''


