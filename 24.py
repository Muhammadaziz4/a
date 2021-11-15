elements = [10,20,30,10,40,20]
def findequalnumbersinarray(elem):
    n = []
    for e in elem:
        if not e not in  n:
            n.append(e)
    return n
print(findequalnumbersinarray(elements))
    