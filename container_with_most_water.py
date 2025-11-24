x = [1,8,6,2,5,4,8,3,7]

n = len(x)
i_index = 0
j_index = 0
max_area = 0
for i in range(n):
    for j in range(i+1,n):
        area = min(x[i],x[j])* (j-i)
        if area > max_area:
            max_area = area
            i_index = i
            j_index = j


print(max_area,i_index,j_index)

#two pointer approach
def max_area_two_pointer(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

