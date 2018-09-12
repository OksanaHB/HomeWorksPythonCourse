def fibonachi(n):
    if n==1:
       return 0
    elif n==2:
        return 1
    return fibonachi(n-2)+fibonachi(n-1)
   
fibonachi_dict = {0:0, 1:1}
def fibonachi_memo(n):
    if not n in fibonachi_dict:
        fibonachi_dict[n] = fibm(n-1) + fibm(n-2)
    return fibonachi_dict[n]