epoch=5
for epoch_i in range(epoch):
    print("----------")
    print(f"正在处理第{epoch_i+1}个epoch的数据")
    print(f"第{epoch_i+1}个数据处理完毕")

optimizes = ["SGD", "Adan", "Momentum", "Adagrad"]
for optimizer_i in optimizes:
    print("正在使用 ", optimizer_i, " 优化器")

img_list = ["img_1.png", "img_2.png", "img_3.png", "img_4.png", "img_5.png"]
for index, img_i in enumerate(img_list):
    print(f"正在处理第{index + 1}张图片：", img_i)

command = ""
while command != "end":
    command = input("请输入命令：")
    print("正在执行命令：", command)

# 这是一个数字列表，用来查找数字"5"
numbers = [1, 3, 4, 2, 5, 6, 7, 8]
found = False

# 机器人开始逐个查看数字"5"
for number in numbers:
    print(f"正在查看数字{number}")
    if number == 5:
        found = True
        print(f"机器人找到了数字{number}!")
        break  # 找到数字5后立即退出循环

if not found:
    print("机器人没有找到数字5。")

# 这是一个数字列表，我们要跳过数字"5"的处理
numbers = [1, 3, 4, 2, 5, 6, 7, 8]

for number in numbers:
    print(f"正在查看数字{number}")
    if number == 5:
        continue  # 如果是数字5，跳过后续处理，直接进入下一次循环
    print(f"机器人找到了数字{number}!")

a=10
b=20
result=a+b
while True:
    answer=int(input(f"请输入{a}+{b}的结果："))
    if result==answer:
        print("回答正确！")
        break
    else:
        print("回答错误。")
