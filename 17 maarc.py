def maksimum_of():
    a=int(input("Podaj pierwsza liczbe: "))
    print (a)
    b=int(input("Podaj druga liczbe: "))
    print (b)
    c=int(input("Podaj trzecię liczbe: "))
    print (c)
    if a>b and a>c:
        print ("Największa liczba to: ",a)
    elif b>a and b>c:
        print("Największa liczba to liczba: ", b)
    else:
        print("Największa liczba to liczba: ", c)
maksimum_of()