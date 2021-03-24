ile=10
lista=[]
for i in range(0, 10):
    liczba = int(input("Podaj liczbę: "))
    lista.append(liczba)
print(lista)
if liczba%2==0:
    continue
else:
    print("nieparzysta")
