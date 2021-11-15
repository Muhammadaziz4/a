def findthreelargestelems(a):
    first = a[0]
    second = a[0]
    third = a[0]
    for i in range(len(a)):
        if a[i] > first:
            third=second
            second=first
            first=a[i]
        elif a[i] > second:
            third=second
            second=a[i]
        elif a[i]>third:
            third=[i]
        ans = first+second+third
    return ans
a = [11,12,9,8,15,34,45,678,55,7,16] 
print(findthreelargestelems(a))       