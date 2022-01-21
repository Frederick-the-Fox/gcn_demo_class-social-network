n = int(input('请输入要转换进制的数值：'))
# x = 2  # 转换为二进制，所以这里取x=2
b = []  # 存储余数
while True:  # 一直循环，商为0时利用break退出循环
    s = n // 2  # 商
    y = n % 2  # 余数
    b = b + [y]  # 每一个余数存储到b中
    print (b)
    if s == 0:
        break  # 余数为0时结束循环
    n = s
b.reverse()  # 使b中的元素反向排列
b = [ str(i) for i in b ]
print ('该数字转换为二进制后是：')
for i in b:
    print (i, " ", end="")
print(" ")