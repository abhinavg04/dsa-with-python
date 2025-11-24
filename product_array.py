def product_arr(arr):
    n = len(arr)
    new_arr = [1]*n
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= arr[j]
        new_arr[i] = prod
    return new_arr

print(product_arr([1,2,3,4]))