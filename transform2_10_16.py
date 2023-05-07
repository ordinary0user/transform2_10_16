
#10_to_2
def dec_to_bin(num):
    answer = bin(num).replace("0b", "")
    return answer

#2_to_10
def bin_to_dec(num):
    answer = int(num,2)
    return answer

#10_to_16
def dec_to_hex(num):
    answer = hex(num).replace("0x","")
    return answer
#16 to 10
def hex_to_dec(num):
    answer = int(num,16)
    return answer

#2 to 16
def bin_to_hex(num):
    dec = bin_to_dec(num)
    answer = dec_to_hex(dec)
    return answer

#16 to 2
def hex_to_bin(num):
    dec = hex_to_dec(num)
    answer = dec_to_bin(dec)
    return answer

#转换函数
def transform(num_str):
    if num_str.startswith("0b"):
        # 判断是否为二进制输入
        print("十进制：", bin_to_dec(num_str))
        print("十六进制", bin_to_hex(num_str))
    elif num_str.startswith("0x"):
        # 判断是否为十六进制输入
        print("二进制：", hex_to_bin(num_str))
        print("十进制：", hex_to_dec(num_str))
    else:
        # 判断是否为十进制输入
        num = int(num_str)
        print("二进制：", dec_to_bin(num))
        print("十六进制：", dec_to_hex(num))

if __name__ == '__main__':

    while True:
        print("输入转换数字（二进制请加“0b”，十六进制请加“0x”）：")
        num_str = input()
        #转换函数
        transform(num_str)