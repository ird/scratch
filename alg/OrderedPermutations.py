def next_perm(arr):
    k = last_ordered_pair(arr)
    if k == -1:
        return k
    j = rightmost_gt(arr,k)
    arr[k], arr[j] = arr[j], arr[k]
    arr[k+1:] = reversed(arr[k+1:])
    return arr

def rightmost_gt(arr, index):
    j = len(arr);

    for x in reversed(arr):
        j = j - 1
        if x > arr[index]:
            return j
    return 0

def last_ordered_pair(arr):
    for j in range(len(arr)-2,-1,-1):
        if arr[j] < arr[j+1]:
            return j
    return -1

def main():
    arr = [] # set up a test list [0,1,..,8]
    for x in range(6):
        arr.append(x)
    s = ""
    while s != -1:
        s = next_perm(arr)
        print(s)

if __name__ == '__main__':
    main()
