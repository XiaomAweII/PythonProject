# 顺序结构从上往下依次执行，通常为赋值&计算

print("5+3=", 5 + 3)
print("5-3=", 5 - 3)
print("5*3=", 5 * 3)
print("5/3=", 5 / 3)
print("5//3=", 5 // 3)
print("5%3=", 5 % 3)
print("5**3=", 5 ** 3)

print("----------------------------")

a = 1
b = 3.14
c = '123'
d = "这也是字符串"
e = '''这也是字符串'''
print("a的数据类型是：", type(a))
print("b的数据类型是：", type(b))
print("c的数据类型是：", type(c))
print("d的数据类型是：", type(d))
print("e的数据类型是：", type(e))

print("----------------------------")

num = 42
print("十进制", num, "转二进制", bin(num))
print("十进制", num, "转八进制", oct(num))
print("十进制", num, "转十六进制", hex(num))
print("二进制101010转十进制", int("101010", 2))
print("八进制1234567转十进制", int("1234567", 8))
print("十六进制1234567转十进制", int("1234567", 16))

print("----------------------------")

num_str = input("请输入小数：")
print("num_str = ", num_str, "格式是：", type(num_str))
num_float = float(num_str)
print("num_float = ", num_float, "格式是：", type(num_float))

print("----------------------------")

name = "James"
age = 38
print("My name is %s and I'm %d years old!" % (name, age))
print("My name is {} and I'm {} years old!".format(name, age))
print("My name is {name} and I'm {age} years old!}")

print("----------------------------")

number = 12.3456
print("%.2f" % number)
print("{:.2f}".format(number))
print(f"{number:.2f}")
