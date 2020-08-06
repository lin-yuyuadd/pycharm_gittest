import math
print('函数的多种参数传递:')


def func0(a, b, c=3, *c1, **d):
    print(a, b, c, c1, d)


func0(1, b=2)
func0(1, 2, 3, 4, 4, 4)
func0(1, 2, 3, 4, 4, 4, d=5, e=6)
print('*' * 40)

print('内置函数(BIF)示例:')
a = 3.14
b = int(a)  # int为内置函数,转换数据类型
print(b)
print('*' * 40)

print('递归函数示例(计算阶乘):')


def func1(a):
    if a == 0:
        return 1
    return a * func1(a - 1)


print(func1(5))
print('*' * 40)

print('匿名函数示例:')
G = lambda x, y: x + y;  # 将匿名函数传递给G
print(G(4, 5))
print('*' * 40)

print('高级数据类型常用方法示例(列表)')
list1 = [1, 2, 3, 4]
list1.append(1)
list1.remove(1)
list1.pop(0)
print(list1)
print('*' * 40)

print('列表推导式示例')
list2 = [x for x in range(10)]
print(list2)
print('*' * 40)

print('生成器示例')


def func2():
    yield 1
    yield 2
    yield 3


# for i in range(3):
#     print(next(func2()))
myG = func2()  # 必须赋值给一个变量不然直接调用生成器会一直使用新的生成器一直输出1
print(next(myG))
print(next(myG))
print(next(myG))
print('*' * 40)

print('切片示例')
list3 = [x for x in range(10)]
print(list3[:5])  # 左切片
print(list3[5:])  # 右切片
print(list3[3:5])  # 取中间
print('*' * 40)

print('控制和跳转语句示例')
cnt = 0
# 使用break退出无限循环
while True:
    cnt += 1
    if cnt == 10:
        break
# 输出奇数
for x in range(10):
    if x % 2 == 0:
        continue
    else:
        print(x)

print('*' * 40)
