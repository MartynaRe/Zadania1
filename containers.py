# 1
def hike():
    items = ['backpack', 'food', 'water', 'phone', 'stick']
    items.sort()
    print(items)


# 2
def odd():
    ans = []
    n = 10
    for i in range(n):
        ans.append(int(input('Give number')))

    for i in range(n):
        if ans[i] % 2 == 1:
            print(ans[i])


# 3
def are_the_same_edges(list):
    if list[0] == list[-1]:
        print('yes')


# 4
def are_the_same_middle(list):
    if list[int(len(list) / 2)] == list[int(len(list) / 2) - 1]:
        print('yes')


# 5
def personal_data():
    data = [
        ['Max', 'Krzysztof', 'Bob'],
        ['Verstappen', 'Krawczyk', 'Ross'],
        ['F1 Driver', 'musician', 'artist']
    ]
    for j in range(len(data)):
        ans = ''
        for i in range(len(data[0])):
            ans += f'{data[i][j]} '
        print(ans)


# 1
def pet():
    my_pet = 'cat', 'alley cat', 'Bazyl'
    animal, race, name = my_pet
    print(f'I have an {race} and the {animal}\'s name is {name}.')


# 2
def contains_multiple():
    my_tuple = 3, 2, 1, 0, -1, 2, 3, 7
    printed = []
    for elem in my_tuple:
        if my_tuple.count(elem) > 1 and printed.count(elem) == 0:
            print(elem)
            printed.append(elem)


# 3
def index():
    numbers = 1, 2, 3, 4, 5
    try:
        print(numbers.index(int(input('What element?'))))
    except ValueError as e:
        print('No such element!')


# 1
def tuple_to_set():
    my_tuple = 1, 1, 1, 2, 3, 4, 4
    my_set = set(my_tuple)
    print(my_set)


# 2
def list_vs_set():
    L_test = [1, 2, 3, 4]
    T_test = 1, 2, 3, 4
    S_test = {1, 2, 3, 4}
    """
    Set:
    - odwoływanie się do indeksów, sortowanie, count
    Tuple:
    - jakiekolwiek próby zmiany wartości
    """


# 3
def tuples_to_set():
    tuple_0 = 1, 3, 5, 7, 9, 11
    tuple_1 = 2, 4, 6
    my_list = []
    for i in range(len(tuple_0)):
        if i % 2 == 0:
            my_list.append(tuple_0[i])
    for i in range(len(tuple_1)):
        if i % 2 == 1:
            my_list.append(tuple_1[i])
    my_set = set(my_list)
    print(my_set)


# 4
def divide_and_reverse(list=[1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]):
    original_len = len(list)
    sublist_len = int(original_len / 3)
    list_0 = []
    list_1 = []
    list_2 = []
    for i in range(sublist_len):
        list_0.append(list[0 + i])
        list_1.append(list[sublist_len + i])
        list_2.append(list[2 * sublist_len + i])
    list_0.reverse()
    list_1.reverse()
    list_2.reverse()
    print(list_0, list_1, list_2)


# 5
def discard_vs_remove():
    set = {1, 2, 3, 4}
    set.discard(3)
    print(set)
    set.remove(3)
    print(set)
    # remove raises an error if element to be removed is not present
