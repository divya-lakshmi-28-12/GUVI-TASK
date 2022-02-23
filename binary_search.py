def binary_search(l,n, low, high):


    while low <= high:

        mid = low + (high - low)//2

        if l[mid] == n:
            return mid

        elif l[mid] < n:
            low = mid + 1

        else:
            high = mid - 1

    return -1


l= [4,11,36,76,89,100,198,206,300]
n=int(input())

print(binary_search(l, n, 0, len(l)-1))

