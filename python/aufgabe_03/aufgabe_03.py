Zahlen = []

print('Gib nacheinander Zahlen ein, welche sortiert werden sollen.')
print('Mit dem Befehl "sortieren" werden die Zahlen sortiert.')

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




