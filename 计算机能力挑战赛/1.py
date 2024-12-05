def shift_char(c, shift, encrypt=True):
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        if encrypt:
            return chr((ord(c) - base + shift) % 26 + base)
        else:
            return chr((ord(c) - base - shift) % 26 + base)
    return c

def process_string(s, operation):
    result = []
    for i, c in enumerate(s):
        shift = i + 1
        if operation == 1:
            result.append(shift_char(c, shift, True))
        elif operation == 0:
            result.append(shift_char(c, shift, False))
    return ''.join(result)

input_str, operation = input().split()
operation = int(operation)

output_str = process_string(input_str, operation)
print(output_str)