x = [1,1,2,3,3,4,4,5,5,6,6,7,7]
st = 0 
end = len(x)-1
while(st<=end):
    mid = st +(end-st)//2
    if mid == 0 and x[0] != x[1]:
        print(x[0])
        break
    if mid == len(x)-1 and x[len(x)-1] != x[len(x)-2]:
        print(x[len(x)-1])
        break
    if x[mid] != x[mid-1] and x[mid] != x[mid+1]:
        print(x[mid])
        break
        
    if mid%2==0:
        if x[mid] == x[mid-1]:
            end = mid -1
        else:
            st = mid+1
    else:
        if x[mid] == x[mid-1]:
            st = mid+1
        else:
            end = mid -1
    
            