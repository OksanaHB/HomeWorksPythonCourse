def fibonachi(n):
    """ recurcive function por calculate fobonachi number """
    if n==1:
       return 0
    elif n==2:
        return 1
    return fibonachi(n-2)+fibonachi(n-1)
   
fibonachi_dict = {0:0, 1:1}
def fibonachi_faster(n):
    """faster version recurcive function por calculate fobonachi number """
    if not n in fibonachi_dict:
        fibonachi_dict[n] = fibonachi_faster(n-1) + fibonachi_faster(n-2)
    return fibonachi_dict[n]