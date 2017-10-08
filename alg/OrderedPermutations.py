def next_perm(arr):
    k = last_ordered_pair(arr)
    if k == -1:
        return k
    j = rightmost_gt(arr, k)
    arr[k], arr[j] = arr[j], arr[k]
    arr[k+1:] = arr[:k:-1]  # reverse from k+1th item onwards
    return arr


def rightmost_gt(arr, index):
    j = len(arr)

    for x in reversed(arr):
        j = j - 1
        if x > arr[index]:
            return j
    return 0


def last_ordered_pair(arr):
    for j in range(len(arr)-2, -1, -1):
        if arr[j] < arr[j+1]:
            return j
    return -1


def main():
    arr = []  # set up a test list [0,1,..,8]
    for x in range(10):
        arr.append(x)
    s = ""
    i = 0
    while s != -1:
        s = next_perm(arr)
        i = i + 1
        if i == 1000000:
            print(str(i) + "th permutation = " + str(s))
            break


if __name__ == '__main__':
    main()
