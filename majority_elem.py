#floor n/2 times most frequent element in array

def majority_elem(arr):
    for i in arr:
        if arr.count(i) > len(arr)//2:
            return i

#moores voting algorithm
def moor(arr):
    for i in arr:
        count = 0
        candidate = None
        if count == 0:
            candidate = i
        if candidate == i:
            count += 1
        else:
            count -= 1
    return candidate
print(moor([3,2,3]))
        
print(majority_elem([3,2,3]))