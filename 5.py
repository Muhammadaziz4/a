def printnumleesthannum (number,list):
    for elem in list:
        if elem < number:print(elem)


def inputnumstolist():
    list = []
    n = int(input('Enter how many numbers should be there in the list: '))
    for v in range(n):
        num = float(input(f'Enter {v+1} number:'))
        list.append(num)
    return list
printnumleesthannum(30,inputnumstolist())