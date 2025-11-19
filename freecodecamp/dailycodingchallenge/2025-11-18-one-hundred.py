


'''
100 Characters

Welcome to the 100th Daily Coding Challenge!

Given a string, repeat its characters until the result is exactly 100 characters long. If your repetitions go over 100 characters, trim the extra so it's exactly 100.
'''
def one_hundred(chars, size=100):
    loops_num =   size / len(chars)
    leftover = size % len(chars)
    #  print(f"loops_num:{loops_num}, len:{len(chars)}")
    results = chars * int(loops_num)
    results += chars[:leftover]

    print(f"results len:{len(results)}, leftover:{leftover}")
    return results



'''
1. one_hundred("One hundred ") should return "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One ".
2. one_hundred("freeCodeCamp ") should return "freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC".
3. one_hundred("daily challenges ") should return "daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge".
4. one_hundred("!") should return "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".
'''

if __name__ == "__main__":
    print(one_hundred("daily challenges "))



