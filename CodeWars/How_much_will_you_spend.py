def getTotal(costs, items, tax):
    getTotal=0
    for a in items:
        if a in costs:   getTotal+=costs[a]
    return round(getTotal*(1+tax),2)