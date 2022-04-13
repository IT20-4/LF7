Zahlen = []

while True :
    x = input('>')
    if x == '' :
        print('Dies ist keine gültige Eingabe.')
    elif x == 'sortieren' :
        Zahlen.sort()
        print(Zahlen)
    else :
        x = int(x)
        Zahlen.append(x)




