from random import randint, choice


def generator():
    ans = ''
    n = int(input('How many characters'))
    possible_chars = ''
    for i in range(n):
        possible_chars += input('Select a character for generator')

    for i in range(randint(1, 100)):
        ans += choice(possible_chars)

    repeating = set(elem for elem in ans if ans.count(elem) > 1)
    print(ans)
    if len(repeating) == 0:
        ans += ans[-1]
    print(ans)
    return ans

