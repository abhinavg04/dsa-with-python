def max_sum_subarray(arr):
    n = len(arr)
    max_sum = float('-inf')
    for i in range(n):
        currSum = 0
        for j in range(i,n):
            # max_sum = max(max_sum,sum(arr[i:j+1])) dont need to add sum again for all subarray
            currSum += arr[j]
            max_sum = max(max_sum,currSum)
    return max_sum

print(max_sum_subarray([-2,1,-3,4,-1,2,1,-5,4]))

def kadans(arr):
    n = len(arr)
    max_sum = float('-inf')
    currSum = 0
    for i in range(n):
        currSum += arr[i]
        max_sum = max(max_sum,currSum)
        if currSum < 0:
            currSum = 0
    return max_sum

print(kadans([-2,1,-3,4,-1,2,1,-5,4]))