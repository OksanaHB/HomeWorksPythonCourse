def box(n):
    if n > 1:
        return ['-' * n] + ['-' + ' ' * (n - 2) + '-'] * (n - 2) + ['-' * n] 
    else:
        return '-'