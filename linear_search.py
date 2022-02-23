def linear_search(a,b):
   
    for i in range (len(a)):
        if a[i]==b:
            return i
    return -1
    
    
l=[66,8,9,78,92]
n=int(input())

print(linear_search(l,n))
