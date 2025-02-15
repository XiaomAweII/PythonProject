x = 10

if x > 5:
    print("x大于5")

if x > 5:
    print("x>5")
else:
    print("x<=5")

if x > 10:
    print("x大于10")
elif x == 5:
    print("x等于5")
else:
    print("x大于10且不等于5")

a = 10
b = 20
result = a + b
answer = int(input(f"请输入{a}+{b}的结果："))
if result == answer:
    print("回答正确！")
else:
    print("回答错误。")
