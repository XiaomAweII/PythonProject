# 等号赋值

# 基本赋值
x = 10
print("x=", x)

# 同一个值给多个变量
x = y = z = 10
print("x=", x, "y=", y, "z=", z)

# 多重赋值
x, y, z = 1, 2, 3
print("x=", x, "y=", y, "z=", z)

# 使用下划线的赋值
x, _, y = 1, 2, 3
print("x=", x, "y=", y)

# 特殊含义的字符还是可以用作变量名，只不过使用之后原有的特殊含义便失去了作用
# false = 10
# x=false
# print(x)

# 数字开头的变量名是不允许的
# 4word=1
# print(4word)

