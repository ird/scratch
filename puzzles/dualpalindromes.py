# Project Euler #39
# "Find the sum of all numbers, less than one million,
# which are palindromic in base 10 and base 2."


def double_drome(maximum):
    # determine the length of the binary number of 1 million
    z = len(str(bin(maximum))) - 2  # not counting the '0b'
    bdromes = []
    # generate all the palindromic binary numbers up to the max
    for i in range(1, 2**(int(z/2))):
        lhs = bin(i)
        rhs = bin(i)[::-1][0:-2]
        # create 3 palindromes from the binary string of length z/2
        t = [int(lhs+rhs, 2), int(lhs+"0"+rhs, 2), int(lhs+"1"+rhs, 2)]
        # add them to the main list if they are below the max
        if t[0] > maximum:
            # print("Maximum reached at i="+str(i))
            break  # t[1] and t[2] are > than t[0]
        for x in t:
            if x < maximum:
                bdromes.append(x)
    result = [1]
    # test all items in base 10
    for x in bdromes:
        if isdrome(x):
            result.append(x)
    return result


def isdrome(n):
    s = str(n)
    end = len(s)-1
    for (i, x) in enumerate(s):
        if i >= end/2:
            break
        if x == s[end-i]:
            i = i + 1
            continue
        return False
    return True


print(isdrome(55855))
print(isdrome(100000))
print(double_drome(1000000))
