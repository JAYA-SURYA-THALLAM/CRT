def quick_sort(arr):
    if len(arr)<=1:
        return arr
    left=[]
    right=[]
    equal=[]
    pvt=arr[-1]
    for i in arr:
        if(i<pvt):
            left.append(i)
        elif(i>pvt):
            right.append(i)
        else:
            equal.append(i)
    print("pivot:",pvt)
    #partitioning the array into three list
    print("left sub array",left)                
    print("right sub array",right)                
    print("equal array",equal)
    return quick_sort(left)+quick_sort(right)+equal
arr=[23,63,44,57,12,45,36]
sorted_arr=quick_sort(arr)
print(sorted_arr)              