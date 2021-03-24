import random

food = ["pizza", "spaghetti", "burger", "pasta", "apple", "sandwich", "candy", "cake", "banana", "mango"]
animals = ["horse", "cat", "dog", "bird", "cow", "monkey", "tiger", "chicken", "pig", "whale"]
sports = ["running", "basketball", "volleyball", "skating", "skiing", "swimming", "jogging", "gymnastics", "cycling", "yoga"]


print("Welcome in game Wisielec!")

category = input("Choose category: food, animals or sports:  ")

if category == "food":
    codeword = random.choice(food)
elif category == "animals":
    codeword = random.choice(animals)
elif category == "sports":
    codeword = random.choice(sports)


codeword_len = len(codeword)
tablica = list(codeword)
chances = 5

print("Codeword has", codeword_len, "letters. You've got", chances,"chances.")


for i in range(codeword_len):
    tablica[i] = '_'

while chances > 0:

    print(" ".join(tablica))

    choice = input("Are you guessing whole codeword or just a letter? Type -'codeword' or 'letter':   ")

    if choice == "letter":
        letter = input("Type a letter: ")
    elif choice == "codeword":
        users_codeword = input("Guess the codeword:   ")
    else:
        print("Choose if you want to guess codeword or letter.")

    if choice == "letter" and letter in codeword:
        for i in range(codeword_len):
            if (codeword[i] == letter):
                    tablica[i] = letter
        if ''.join(map(str,tablica)) == codeword:

            print("You've got", chances, " chances left.")
            print(" ")
            print(' '.join(tablica))
            print(" ")
            print("You won!")
            break
    elif choice == "codeword" and users_codeword == codeword:
        print("Congrats!")
        break

    elif choice == "codeword" and users_codeword != codeword:
            print("Try again!")
    else:
        chances = chances - 1
        print("Try again. You've got",chances, "chances.")


else:
    print("You lost this game.")