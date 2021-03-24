def minimum_of():
    a=int(input("Podaj pierwsza liczbe: "))
    print (a)
    b=int(input("Podaj druga liczbe: "))
    print (b)
    c=int(input("Podaj trzecię liczbe: "))
    print (c)
    if a<b and a<c:
        print ("Najmniejsza liczba to: ",a)
    elif b<a and b<c:
        print("Najmniejsza liczba to liczba: ", b)
    else:
        print("Najmniejsza liczba to liczba: ", c)
minimum_of()