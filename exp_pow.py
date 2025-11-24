n = 5
x = 2
# def exp_pow(x:int, n:int) -> int:
#     if n == 0:
#         return 1
#     elif n < 0:
#         x = 1/x
#         n = -n
#     if n % 2 == 0:
#         return exp_pow(x*x, n//2)
#     else:
#         return x * exp_pow(x*x, (n-1)//2)
    
def binExp(x,n):
    ans = 1
    while n>0:
        if n%2 == 1:
            ans = ans*x
        x = x*x
        n = n//2
    return ans
print(binExp(x,n))
# print(exp_pow(x,n))