# return pair sum == target
#brute force O(n^2)
def pair_sum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == target:
                return arr[i], arr[j]
            
def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
            
def optimal_pair_sum(arr, target):
    arr.sort() # O(nlogn)
    left = 0
    right = len(arr)-1
    while left < right: # O(n)
        currSum = arr[left] + arr[right]
        if currSum == target:
            return arr[left], arr[right]
        elif currSum < target:
            left += 1
        else:
            right -= 1
            
print(pair_sum([1,2,3,4,5], 8))