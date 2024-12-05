def hex_to_binary(hex_number):
    # 移除前缀'0x'
    hex_number = hex_number.replace('0x', '')
    # 将十六进制数转换为整数
    decimal = int(hex_number, 16)
    # 将整数转换为二进制，并去掉前缀'0b'
    binary = bin(decimal)[2:]
    # 确保二进制数至少有8位，如果不足8位，则在前面补零
    binary = binary.zfill(8)
    return binary


# 获取用户输入的16进制数
hex_number = input()

# 打印转换后的二进制数 
print(hex_to_binary(hex_number))
print(type(hex_to_binary(hex_number)))