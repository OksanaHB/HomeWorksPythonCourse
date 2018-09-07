def fibonachi(n):
    if n==1:
       return 0
    elif n==2:
        return 1
    return fibonachi(n-2)+fibonachi(n-1)
   
n=int(input())
print(fibonachi(n))