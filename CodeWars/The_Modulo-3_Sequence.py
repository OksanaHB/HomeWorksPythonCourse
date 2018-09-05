def sequence(n):
    sequence=[0,1,1,2,0,2,2,1]
    return sequence[n-1] if n<9 else sequence[n%8-1]