


'''
Missing Socks

Given an integer representing the number of pairs of socks you started with, and another integer representing how many wash cycles you have gone through, return the number of complete pairs of socks you currently have using the following constraints:

    Every 2 wash cycles, you lose a single sock.
    Every 3 wash cycles, you find a single missing sock.
    Every 5 wash cycles, a single sock is worn out and must be thrown away.
    Every 10 wash cycles, you buy a pair of socks.
    You can never have less than zero total socks.
    Rules can overlap. For example, on wash cycle 10, you will lose a single sock, throw away a single sock, and buy a new pair of socks.
    Return the number of complete pairs of socks.
'''
def sock_pairs(pairs, cycles):
    while cycles >= 0:
        print ("Start c:"+str(cycles)+"p:"+str(pairs))
        if (cycles >= 2):
            print("Remove One")
            pairs -= .5
        if (cycles >= 3):
            print("Add One sock")
            pairs += .5
        if (cycles >= 5):
            print("Add One sock")
            pairs -= 1
        if (cycles >= 10):
            print("Add Buy one")
            pairs += 1
        cycles -= 10
        if (cycles >= 0):
            pairs -= 1
        print ("c:"+str(cycles)+"p:"+str(pairs))
    if (pairs < 0):
        return 0
    return int(pairs)

if __name__ == "__main__":
    print(str(sock_pairs(5, 11)))
    print(str(sock_pairs(6, 25)))


