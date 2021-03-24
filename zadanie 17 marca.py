
def rocznik(age,oryginal):
    if age>=25 and oryginal:
        print("Gratulacje!Twój samochód ",{car['brand']}," może być zarejestrowany jako zabytek!")
    elif age<25:
        print("Twój  {car['brand']} jest jeszcze zbyt młody.")
    elif not oryginal:
        print("Twój samochód nie ma 75% oryginalnych części.")

car = {
    'brand': 'renault',
    'model': 'megan',
    'year': 1993,
    'oryginal': True
}

print(car)

car_age = 2021-car["year"]
rocznik(car_age,car['oryginal'])