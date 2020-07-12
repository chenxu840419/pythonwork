"""
Day_01
快捷键：
移动到本行开头：home 键
移动到本行末尾：end 键
注释代码：ctrl + /
复制行：ctrl + d
选择列：鼠标左键 + alt
移动行：shift + alt + 上下箭头
智能提示：ctrl + space
整理格式（如空格等）ctrl + alt + L
多行同时缩进： 选择多行之后按tab
多行同时取消缩进： 选择多行之后按shift + tab
重命名多个相同变量： shift + F6

注释：
1.单行注释：以#号开头
2.多行注释：三引号开头，三引号结尾。

函数
表示一个功能，函数定义者是提供功能的人，函数调用者是使用功能的人
print(数据）作用：蒋括号中的内容显示在工作台
input（“需要显示的内容”）作用：蒋用户输入的内容赋值给变量

变量：
定义：关联对象的标识符
命名：必须是字母或下划线开头，后跟字母，数字，下划线等
      不能使用python 关键字（蓝色字），否则发生语法错误
建议命名：字母小写，多个单词以下划线隔开。
          class_name
赋值：创建一个变量或改变一个变量绑定的数据。
语法：变量名 = 数据
变量名1，变量名2 = 数据1，数据2

看教程：www.runoob.com
看文档：docs.python.org/zh-cn/3/
逛社区：www.pythontab.com
"""

"""
Day02
del 语句
语法：del变量名1，变量名2
作用：用于删除变量，同时解除与对象的关联关系。如果可能则释放对象。
自动化内存管理的引用计数：每个对象记录被变量绑定（引用）的数量，当为0时被销毁。

核心数据类型
在python中变量

空值变量 None
表示不存在的特殊对象
作用：
用来占位
变量解除绑定
"""
# #整数
# #--十进制
# num01 = 18
# print(num01)
# #--二进制  0 1 10 11 100 101 110......
# num02 = 0b11
# print(num02)
# #--八进制  0 1...7 10 11 12.......
# num03 = 0o10
# print(num03)
# #--十六进制   0--9   a(10) --f(15) 10.....19...1a....1f
# num03 = 0xf
# print(num03)
#
# #小整数对象池 CPython中整数-5至256，永远存在小整数地址可重复使用
# a = 100
# b = 100
# c = 500
# d = 500
# #id函数：返回变量存储的对象地址
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# #备注：在交互式中，两个500不是一个对象

# #浮点数float
# # 小数（包含正数，复数，0.0）
# # 字面值：
# # -- 小数：1.0   2.5
# # -- 科学计数法：e/E  (正负号)   指数
# #    1.23e-2(等同于0.0123)
# #    1.23456e5(等同于123456.0)
# #2. 浮点数（小数）
# f01 = 1.0
# f02 = 1.234e2
# f03 = 1.234e-3
# print(f01)
# print(f02)
# print(f03)

# #3. 字符串str 用来本事文本信息的字
# s01 = "唐僧"
# s02 = "10"
# s03 = "1.5"
# print("10"+"2")
# print(10+2)
#
# #复数 complex
# 有实部和虚部组成的数字
# 虚部是以j 或J 结尾。
# 字面值：1j    1+1j   1-1j

# c01 = 1j
# c02 = 5 + 1j
# print(c01)
# print(c02)

# #5. 布尔bool
# 用来表示真和假的类型
# True 表述真(条件满足或成立),本质是1
# False 表示假(条件不满足或不成立),本质是0

# b01 = True  # 真的   对的    成立的    满足条件的
# b02 = False  # 假的   错的    不成立的  不满足条件的
# b03 = 1 > 2
# print(b03)
#
# #数据类型转换
# #str_score = input("请输入成绩:")
# #input函数的结构就是str, 如果需要做数学运算，必须转化成数字。
# print(type(str_score))
# float_score = float(str_score)
# int_score = int(str_score)
# str_score = str(str_score)
#
# #结果都为true
# b04 = bool("true")
# b05 = bool("false")
# b06 = bool("....")
# print(b04)
# print(b05)
# print(b06)
#
# #结果为false，只有
# b07 = bool(0)
# b08 = bool(0.0)
# b09 = bool(None)
# print(b07)
# print(b08)
# print(b09)
#
# i01 = int("1")       #如果需要转换数据类型，填入数据类型要与目标数据类型一致

#算术运算符
# num01 = 5
# num02 = 2.1
# print(num01 + num02)
# # %作用1：判断一个数能否被另外一个数整除
# print(num01 % 2 == 0)
# #作用2：获取各位
# print(687 % 10)


# 逻辑运算符    与and  或or   非not
# （重点判断    假     真      反
# 身份运算符    判断ID 是否一样
# and   表示并且关系   一假俱假
# or    表示或者关系   一真俱真
# not   表示取反
# not true    #返回  false
# not false   #返回  true
# not 100（相当于 not bool(100)     #返回  false


#  放学了   and   作业完成了   =两条豆满足=>   回家
# print(true and true)   #true
# print(false and false) #false
# print(true and false)   #false
# print(false and true)   #false
#
# print(1 > 2 and 5 > 3)   #false
# #  放学了   or   作业完成了   =其中有一条满足=>   回家
# print(true or true)   #true
# print(false or false) #false
# print(true or false)   #true
# print(false or true)   #true
#
# print(1 >2 or 5 < 3 or 10 > 2)   #true

#短路逻辑    一旦结果确定， 后面的表达式不再运行
#如果第一个条件不满足    则不在考虑第二个条件
# print(1 > 2 and input("前输入：") == "a")
# #如果第一个条件满足    则不再考虑第二个条件
# print(1 < 2 or input("前输入：") == "a")

# 建议（启发）：尽量将耗时的判断放在后面。（因为很可能部再执行）

#身份运算符  ----判断两变量是否指的是同一个变量

# num01 = 800
# num02 = 900
# num03 = num01
# print(num01 is num02) == print(id(num01) == id(num02))    #false
# print(num01 is num03)  #true

"""
行
物理行：程序员编写代码的行
逻辑行：python解释器需要执行的指令
建议一个逻辑行在一个物理行上
如果一个物理行中使用多个逻辑行，需要使用分号; 隔开  #一般不这么用
如果逻辑行太长，可以使用隐式换行或显式换行
--隐式换行：所有括号的内容换行，称为隐式换行
  括号包括：()   []   {}  三种
--显式换行：通过折行符\ （反斜杠）换行，必须放在一行的

"""
# # 两个物理行   两个逻辑行
# print("你好")
# print(1 + 2)
# # 一个物理行    两个逻辑行
# print("你好");print(1 + 2)
# #三个物理行   一个逻辑行
# x = 1+2+(3+
#          4+
#          5)
# #两个物理行   一个逻辑行
# x = 1+2+3+\
#     4+5

"""
选择语句

"""
# sex = input("请输入性别：")
# if sex == "男":
#     print("您好先生！")
# elif sex == "女":
#     print("您好女士！")
# else:
#     print("性别未知")

"""
调试：让程序在指定的行中断，然后逐语句执行，我们审查陈旭运行过程，以及变量等是否正确
#1， 在可能出错的行，加入断点。（在行数旁边的位置点一下)
#2.  开始调试a;t + shift + f9
#3.  民众断电后（断点行是蓝色的），逐语句执行f7
#....(判断执行过程，以及变量的取值）。。。。。
4.   停止调试ctrl + f2


"""

"""
if 语句的真值表达式
if 100:
    print("真值")
等同于
if bool(100):
    print("真值")
"""


"""
条件表达式
语法：
变量 = 结果1  if 条件  else 结果2
作用：
根据条件（true/false) 来决定返回结果1还是结果2。

"""
# #中规中矩的表达方式：
# sex = None
# if input("请输入性别：") == "男":
#     sex = 0
# else:
#     sex = 1
# #变量表达式的方法：
# sex = 0 if input("请输入性别：") == "男" else 1
# print(sex)

"""
循环语句---while
while 条件:
    执行代码
    if 推出条件1：
        break
"""
# #死循环：条件永远满足的循环
# while true:
#     str_usd = input("请输入美元")
#     float_usd = float(str_usd)
#     rmb = float_usd*6.708
#     print(rmb)
#
# while true:
#     str_usd = input("请输入美元")
#     float_usd = float(str_usd)
#     rmb = float_usd*6.708
#     print(rmb)
#     if input("按E键则退出") == "e":
#         break  #退出循环


"""
for 语句
作用：
    用来遍历可迭代对象的数据元素。
    可迭代对象是指能一次获取数据元素的对象，例如：容器类型。
语法：
    for 变量列表 In 可迭代对象:
        语句块 1 
    else:
        语句块 2
说明：
else子句可以省略。
循环体内用break终止

range() 函数
作用：
    用来创建一个生成一系列的可迭代对象（也叫整数序列生成器）
语法：
    range(开始值, 结束值, 间隔)
说明：
    -- 此函数返回的可迭代对象可以用for 去取其中的元素。
    -- 返回的数字不包含结束值。
    -- 开始点默认为 0
    -- 间隔默认值为 1
需熟练正序，倒叙，跳着 生成数字
for 循环比while， 更适合做预定次数的循环。
"""
# for element in "我爱python":
#     print(element)
# #range() 函数：整数生成器
# for element in range(1, 5, 1):  # range 里 ：1 2 3 4
#     print(element)
#
# for element in range(1, 6, 2):  # range 里 ：1  3  5
#     print(element)
#
# for element in range(6):  # range 里 ：0  1  2  3  4  5
#     print(element)

# for element in range(5, -1, -1):  # range 里 ：5  4  3  2  1  0
#     print(element)


"""
跳转语句
break 语句：
作用：
1 跳出循环体，后面的代码不再执行。
2 可以让while语句的else 不分离不执行

continue 语句
作用：跳过本次，继续下一次循环。

"""
# sum = 0
# for item in range(1,100):
#     #如果满足条件  则  累加
#     if item % 3 == 0:
#         sum += item
#     #如果不满足条件  则  跳过
#     if item % 3 != 0:
#        continue # 跳过
#        sum += item

"""
rond(float , 2)   # 保留两位小数


"""

"""
str 编码
字符  -->  编码值
print(ord("天")
编码值  -->  字符
print(chr("97")
"""
# name = "悟空"
# name = "孙悟空"
# print(name)    #不是将字符串“悟空”改编为“孙悟空”，
#                #而是创建了字符串“孙悟空”将name的内容改变成"孙悟空“的地址。


"""
   字符串字面值
"""
#单引号和双引号功能相同，都不支持换行
# str01 = "大家好"
# str01 = '大家好'
# 三引号：可见即所得
# str01 = '''大
# 家
# 好
# '''
# # str01 = """大家好"""
# str02 = '我爱"python"。'
# str02 = "我爱'python'。"
# print(str02)

#转义符:改变原始含义的特殊字符
#如果字符串内部需要包含多种（但/双/三)引号，使用转义符。
# str03 = "我爱\"python\""
# print(str03)
#
# #\n  换行
# str04 = "大家好,\n我是CX。"
# print(str04)
# #\t 水平制表格 tab 键
# str04 = "大家好,\t我是CX。"
# print(str04)


# str04 = "C:\\Users\\cx\\Documents\\Python"    #路径需要在\ 前加转义符\
# print(str04)
#
# str04 = r"C:\Users\cx\Documents\Python"       #原始字符串：取消转义

"""
字符串格式化
1 定义：生成一定格式的字符串。
2 语法：字符串%(变量)
        "我的名字是%s,年龄是%s" % (name , age)
3 类型码：%s 字符串      %d 整数      %f 浮点数
4 格式： %[- + 0 宽度 .精度]类型码
- : 左对齐(默认是右对齐)
+ : 显示正号
0 ：左侧空白位置补零
宽度 ： 整个数据输出的宽度
精度 ： 保留小数点后多少位
"""
# # 格式化字符串
# name = "CX"
# age = 32
# msg01 = "我的名字是："+name+",年龄是："+str(age)+"."   #字符串拼接的写法
# #格式化字符串
# msg02 = "我的名字是：%s,年龄是：%d." % (name , age)
# print(msg01)
# print(msg02)
# #宽度是5 右对齐
# str05 = "整数是：%5d."%(32)  #整数是:32.。
# print(str05)
# #宽度是5 左对齐
# str06 = "整数是：%-5d."%(32)  #整数是：32
# print(str06)
# #宽度是2 不足两位使用0填充       02:00    01:59     00:03
# str07 = "时间是：%02d"%(2)  #整数是：02
# print(str07)
# str08 = "小数:%.2f"%(1.23556)    #小数: 1.23
# print(str08)
#  round(1.234,2)   是改变数值
# num = 1.234
# num = round(num,2)
# print(num)


"""
算数运算符
+: 用于拼接两个容器
+=：用原容器与右侧容器拼接，并重新绑定变量。
*：重复生成容器的元素
*=：用原容器生成重复元素
> >= < <= == != : 从左到右依次比较两个容器中元素，一但不同则返回比较结果。
"""
# str01 = "悟空"
# str02 = "八戒"
# str03 = str01 + str02
# str01 += str02
# print(str01)
# #容器可以与数字相乘
# print(str02 * 2)  # "八戒八戒"
# str02 *= 2
# print(str02)
# # 字符串比较的是编码值
# print("Abc" > "aac")


"""
成员运算符
语法：
    数据 in 序列
    数据 not in 序列
作用：
    如果在指定的序列中找到值，返回bool类型。
"""

# str03 = "猥琐发育，别浪"
# print("猥琐" in str03)


"""
索引 index
1 作用：访问容器
2 语法: 容器[整数]
3 说明:
  正向索引从0开始，第二个索引为1， 最后一个为len(s)-1   #len(s)-1 表示字符串长度-1
  方向索引是从-1开始，-1代表最后一个，-2代表倒数第二个,一次类推， -len(s)

"""
# str04 = "abcde"
# print(str04[0])
# print(str04[len(str04)-1])
# print(str04[-1])
# #索引不能越界
# # print(str04[5])   #indexerror


"""
切片slice
1 作用：从容器中取出相应的元素重新组成一个容器。
2 语法：容器[ (开始索引) : (结束索引)(:(步长))]
        小括号()括起的部分代表可省略
3 说明：
  结束索引不包含该位置元素
  步长是切片每次获取完当元素后移动的偏移量
切片积十越界，也不会错误
"""
# c
# print(str04[0:3])  #abc
# print(str04[0:3:2])  #ac
# print(str04[::]) #abcde
# print(str04[::-1]) #edcba
# print(str04[-2:-5:-1]) #bcd
# print(str04[1:1]) #空
# print(str04[3:1]) #空
# print(str04[3:1:-1]) #dc
# print(str04[-2:]) # de
# print(str04[-2:1]) # 空
# print(str04[1:10]) # bcde    切片积十越界

"""
内建函数
len() 返回序列的长度
max() 返回序列的最大值元素
min() 返回序列的最小值元素
sum() 返回序列中所有元素的和（元素必须是数值类型）

"""

"""
列表: 由一系列变量组成的可变序列容器。
基本操作:
1 创建列表：[]   list(可迭代对象）
2 添加元素： 列表名称.append(元素)
            列表名称.insert(索引，元素)
3 获取元素：索引
4 删除元素： 列表名称.remove(元素)
            del 列表名称[索引]
            del 列表名称[切片]
5 修改元素：列表名称[索引] = 元素
            列表名称[切片] = 元素
6 查询元素：列表名称[索引]
            列表名称[切片]
7 定位：索引    切片

列表扩容原理：
1. 创建新的列表（更大的列表）
2. 拷贝原有元素
3. 替换列表的地址   #变量中纯的实际上是表头的地址，表头里纯的是表身的地址，扩容的时候扩的是表身。
"""
# #1. 创建空列表
# list01 = []
# list01 = list()

# #2.  创建具有默认值的列表 [元素1，元素2，。。。。]   list(可迭代对象)
# list02 = [1, True, 1.2]
# print(list02)       #[1, True, 1.2]
# list02 = list("abcd")
# print(list02)   #['a', 'b', 'c', 'd']
# list02 = list(range(5))
# print(list02) # [0, 1, 2, 3, 4]

# #3. 添加元素
# #append  在末尾追加
# list02 = list("12345")
# list02.append("q")
# list02.append("t")
# print(list02)
# #insert  插入（索引，元素）
# list02.insert(1 , "x")
# print(list02)

# #4. remove 删除元素
# list02 = list("12345")
# print(list02)
# list02.remove(2)
# print(list02)
# #删除指定索引的元素
# del list02[1]
# print(list02)

# #5. 获取元素（索引， 切片）
# #获取前三个元素
# list02 = list("12345")
# print(list02[:3])
# print(list02)
# #修改前元素
# list02[:3] = ["a","b","c"]
# list02[:3] = ["a","b","c","d","e"]
# list02[:3] = ["a"]
# print(list02)
# del list02[:3]
# print(list02)

# #6. 遍历元素
# list02 = list("12345")
# #正向
# for i in range(len(list02)):
#     print(list02[i])            #1  2  3  4  5
# #跳着
# for i in range(0,len(list02),2):
#         print(list02[i])   #1  3  5
# #倒着
# for i in range(len(list02)-1,-1,-1):
#         print(list02[i])   #5  4  3  2  1

"""
列表 VS 字符串

1. 列表和字符串都是序列，元素之间有先后顺序关系。
2. 字符串是不可变的序列，列表是可变的序列。
3. 字符串中每个元素只能存储字符，而列别哦可以存储任意类型
4.列表和字符串都是可迭代对象。
5. 函数：
    将多个字符串拼接为一个。
    result = "连接符".join(列表)
    
    将一个字符串拆分为多个。
    列表 = "a-b-c-d".split("分隔符")
"""
"""
内存图
内存变化分析

"""
#
list01 = [1,2]
#将列表地址赋值给list02
list02 = list01
#将数据100 的地址赋值给list01里第一个元素所存储的地址
list01[0] = 100
print(list02[0])    #  100

list01 = [1,2]
#将列表地址赋值给list02
list02 = list01
#改变的是列表的第一个元素
list01 = [100]
print(list02[0])   #1

list01 = [1,2]
#将列表新列表的地址赋值给list02（注意list01[:]是一个新建的，复制了list01列表里所有元素的新列表）
list02 = list01[:]
#改变的是列表的第一个元素
list01[0] = 100
print(list02[0])   #

"""
浅拷贝
深拷贝
"""
list01 = [1,2]
#将列表中元素赋值一份
#list02 = list01[:]
#将列表中元素复制一份
list02 = list01.copy()
list01[0] = 100
print(list02[0])  #1

#浅拷贝
import copy
list01 = [1,[2,3]]
#将列表中元素赋值一份（只拷贝一层）
list02 = copy.copy(list01)
list01[1][0] = 200
print(list02[1][0])   #200

#深拷贝
import copy
list01 = [1,[2,3]]
#将列表中元素及其关联的所有对象全部拷贝一份
list02 = copy.deepcopy(list01)
list01[1][0] = 200
print(list02[1][0])   # 2

"""
列表推导式
语法：[对变量的操作 for 变量名 in 可迭代对象]
"""
list01 = [3,5,6,7,9]
#需求：创建新列表，每个元素是list01中的元素的平方
list02 = []
for item in list01:
    list02.append(item ** 2)
print(list02)
#列表推导式写法
list03 = [item ** 2 for item in list01]
print(list03)

list01 = [3,5,6,7,9]
#需求：创建新列表，如果元素是偶数，则将每个元素是list01中的元素的平方
list02 = []
for item in list01:
    if item % 2 == 0:
        list02.append(item ** 2)
print(list02)
#列表推导式写法
list03 = [item ** 2 for item in list01 if item % 2 == 0]
print(list03)

"""
元组 tuple 
定义：
有一系列变量组成的不可变序列容器
不可变是指一旦创建，不可以添加/删除/更改
作用：
元组与列表都恶意存储一系列变量，由于列表会预留内存空间，所以可以增加元素。
元组会按需分配内存，所以如果标量数量固定，建议使用元组，因为通常占用空间更小。
应用：
变量交换的本质就是创建援助：x, y = y, x
格式化字符串本质就是创建援助："姓名：%s, 年龄：%d" % ("tarena", 15)
"""
# #1. 创建空元组
# t01 = ()
# t02 = tuple()
#
# #2. 创建具有默认值的元组
# t01 = (1, 2, 3)
# t01 = tuple("abcd")
# t01 = (1, 2, [4, 5])
# print(t01)
# #修改
# t01[2] = 100   #   语法错误tuple 不支持修改
# t01[2][0] 100  #   修改的是元素第三个元素(列表)的元素
#
# #3. 获取元素(索引/切片）
# print(t01[:2])
# #获取元组所有元素
# for item in t01:
#     print(item)
# #倒序获取元组所有元素
# for item in range(len(t01) - 1, -1, -1):
#     print(t01[item])

t02 = ("a", "b")
l02 = ["a", "b"]

t03 = t02
l03 = l02

t02 += ("c", "d")   #创建了新元组对象，改变了t02存储的地址
l02 += ["c", "d"]   #将["c", "d"]添加到原列表中

print(t02)  #['a', 'b', 'c', 'd']
print(t03)  #('a', 'b')
print(l03)  #['a', 'b', 'c', 'd']

#如果元组只有一个元素，必须多谢一个逗号，否则视为普通对象，不是元组对象
t04 = (1)
print(t04)  # 1
t04 = (1,)
print(t04)  #(1,)





"""
字典 dict：
有一系列键值对组成的可变映射容器。
映射：通过键获取值（字符串/列表/元组通过索引），
创建字典: {键1：值1，键2：值2}     dict(可迭代对象)
添加/修改元素：
语法：
字典[键] = 数据
说明：
键不存在，创建键，并绑定键对应的值。
键存在，修改绑的绑定关系。
获取元素：V 字典[键]    #没有键则错误
删除元素：del 字典[键]

"""
#创建空字典
d01 = {}
d02 = dict()

#d01 = {键:值}
d01 = {"a":"A","b":"B"}
d01 = dict("ab")   #   分不清键，值
d01 = dict([(1,2),(3,4)])    #{1:2, 3:4}
print(d01)

#第一次增加
d01["c"] = "C"
#第二次修改
d01["c"] = "CC"
#读取元素（如果不存在则异常）
print(d01["d"])

#读取元素（如果不存在则异常）
#建议：再字典中读取元素，先判断存在，再进行读取。
if "d" in d01:
    print(d01["d"])
#删除
del d01["c"]
print(d01)

#获取字典中所有元素：
for key in d01:
    print(key)
    print(d01[key])

for item in d01.items():
    print(item[0])  #key
    print(item[1])  #value

for k, v in d01.items():
    print(k)  #key
    print(v)  #value

#获取所有键
for k in d01.keys():
    print(k)
#获取所有值
for v in d01.values():
    print(v)



























































































































