def Findtwoadjacentelementswhosesumisminimal():
    array = [2,5,1,6,89,34]
    array.sort()
    return sum(array[0:2])

print(Findtwoadjacentelementswhosesumisminimal())