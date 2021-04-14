from delta import delta
from generator import generator
from fibbonacci import fib
# 2
def calculate_delta(a=3, b=4, c=1):
    return delta(a, b, c)


# 6
def longest_sequence(string):
    start_index = 0
    start_index_tmp = 0
    seq_len = 1
    seq_len_tmp = 1
    for i in range(1, len(string)):
        x = string[i]
        y = string[i-1]
        if string[i] == string[i - 1]:
            seq_len_tmp += 1
            if seq_len_tmp > seq_len:
                seq_len = seq_len_tmp
                start_index = start_index_tmp
        else:
            start_index_tmp = i
            seq_len_tmp = 1
    print(start_index, seq_len)


# 7
print(fib(17))
