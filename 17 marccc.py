def main():
    lista = []

    wynik = 0

    ilosc = int(input("Podaj ilość elementów: "))

    for i in range(ilosc):

        x = int(input("Podaj wartość elementu: "))
        lista.append(x)

        if x % 2 == 0:
            print (x)
        else:
            continue

main()