def main():
    lista = []

    wynik = 0

    ilosc = int(input("Podaj ilość elementów: "))

    for i in range(ilosc):

        x = int(input("Podaj wartość elementu: "))
        lista.append(x)

    for i in range(ilosc):
        wynik = wynik + lista[i]

    print("Suma wartości elementów listy to: ",wynik)
main()