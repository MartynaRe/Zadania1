# 2
def bigger_than(a, b):
    if a + b > 100:
        print(a + b)
    else:
        print('Koniec')


# 4
string = ''


def is_longer(string):
    if len(string) > 5 and 'a' in string:
        ans = string.replace('a', 'z')
        print(ans)


# 6
def guess(number):
    hidden_number = 10
    if number == hidden_number:
        print('gratulacje')
    else:
        print('pudlo!')


# 8
def sort():
    a = input('Give the first number')
    b = input('Give the second number')
    c = input('Give the third number')
    if a > c:
        if a > b:
            if b > c:
                print(a, b, c)
            else:
                print(a, c, b)
        else:
            print(b, a, c)
    elif b > c:
        print(b, c, a)
    elif b > a:
        print(c, b, a)
    else:
        print(c, a, b)


# 2
def ingredients():
    ingredient_list = ['bread', 'butter', 'ham', 'cheese', 'radish']
    for ingredient in ingredient_list:
        print('Add ' + ingredient)
    print('eat')


# 4
def factorial(n):
    val = 1
    ans = ''
    if n == 0 or n == 1:
        ans += f'{n}! = 1'
    elif n > 8:
        print('Error, n has to be <=8')
        return None
    else:
        ans += f'{n}!=1'
        for i in range(2, n + 1):
            ans += f'*{i}'
            val *= i
    ans += f'={str(val)}'
    print(ans)

# 2
def game():
    secret_num = 5
    guessed = False
    while not guessed:
        if secret_num == int(input('Take a guess!')):
            guessed = True
            print('correct!')
