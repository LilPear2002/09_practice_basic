
def binary_to_decimal(binary_list):
    decimal = 0
    for i in range(len(binary_list)):
        decimal += binary_list[i] * (2 ** (len(binary_list) - 1 - i))
    return decimal


def binary_to_decimal2(binary_list):
    num_char = ''.join(map(str, binary_list))
    decimal = int(num_char, 2)
    return decimal