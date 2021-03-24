def can_be_card_number(user_input):
    if not len(user_input) in [13,15,16]:
        return False
    if not user_input.isdigit():
        return False
    return True

def is_Visa(card_number):
    if card_number [0] == '4' and len(card_number) in [13,16]:
        return True
    else:
        return False

def is_Mastercard(card_number):
    if (51<= int(card_number[0:2])<=55 or 2221<=int(card_number[0:4])<=2720) and len(card_number) ==16:
        return True
    else:
        return False

def is_AmericanExpress(card_number):
    if (int(card_number[0:2])==34 or int(card_number[0:2])==37) and len(card_number) == 15:
        return True
    else:
        return False

user_input=input("Give me your card number: ").replace(' ','')

if can_be_card_number(user_input):

        if is_Visa(user_input):
            print("Visa card")
        elif is_Mastercard(user_input):
            print("Master Card")
        elif is_AmericanExpress(user_input):
            print("AmericanExpress")
        else:
            print("Inna karta")
else:
    print("It isn't card number.")

can_be_card_number(user_input)