arr= [40,30,10,20]
m = 2
def is_possible(arr, m, mid):
    painter = 1
    time = 0
    for i in range(len(arr)):
        if arr[i] > mid:
            return False
        if arr[i] + time <= mid:
            time += arr[i]
        else:
            painter += 1
            time = arr[i]
    return True if painter <= m else False

def painters_partition(arr, m):
    n = len(arr)
    st = max(arr)
    end = sum(arr)
    ans = -1
    while st <= end:
        mid = st + (end - st)//2
        if is_possible(arr, m, mid):
            ans = mid
            end = mid - 1
        else:
            st = mid + 1
    return ans

print(painters_partition(arr, m))