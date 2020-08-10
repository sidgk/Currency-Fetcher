def sdiff(arr,l):
    #l = len(arr)
    arr = sorted(arr)
    diff = 10**20
    for i in range(l-1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]
    return diff
arr = [1, 5, 3, 19, 18, 25,18.05] 
l = len(arr) 
print("Minimum difference is " + str(sdiff(arr, l)))