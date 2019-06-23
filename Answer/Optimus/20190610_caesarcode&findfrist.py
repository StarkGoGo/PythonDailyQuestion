# 恺撒密码是古罗马恺撒大帝用来对军事情报进行加解密的算法，它采用了替换方法对信息中的
# 每一个英文字符循环替换为字母表序列中该字符后面的第三个字符，即，字母表的对应关系如下：‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
# 原文：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
# 密文：D E F G H I J K L M N O P Q R S T U V W X Y Z A B C‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
# 对于原文字符P，其密文字符C满足如下条件：C=(P+3) mod 26‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
# 上述是凯撒密码的加密方法，解密方法反之，即：P=(C-3) mod 26‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
# 假设用户可能使用的输入包含大小写字母a~zA~Z、空格和特殊符号，请编写一个程序，
# 对输入字符串进行恺撒密码加密，直接输出结果，其中空格不用进行加密处理。使用input()获得输入。
strings = input("请输入需要加密的内容：")
encrypted_strings = []
for string in strings:
    if string == chr(32):
        encrypted_strings.append(string)  # 空格不加密
    else:
        ascii_num = ord(string) - 64 + 3
        if ascii_num == 26:
            encrypted_strings.append(chr(26 + 64))
        else:
            encrypted_strings.append(chr(ascii_num % 26 + 64))
print('{}'.format(''.join(encrypted_strings)))


# 请实现一个函数用来找出字符串中第1个只出现1次的字符。
# 例如，
# 当从字符串中只读出前两个字符"go"时，第1个只出现次的字符是"g"。
# 当从该字符串中读出前六个字符"google"时，第1个只出现1次的字符是“l”。
def first_one_first_time(strings):
    lettet_count = {}
    for letter in strings:
        lettet_count[letter] = lettet_count.get(letter,0) + 1
    for letter in strings:
        if lettet_count[letter] == 1:
            return letter
        else:
            continue


if __name__ == '__main__':
    strings = input("输入需要检查的字符串：")
    letter = first_one_first_time(strings)
    print(letter)