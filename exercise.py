
# #练习：在控制台中录入学生信息(姓名，年龄，性别，成绩）
# #在一行输出：
# #格式：我的姓名是：XXX，年龄是：XXX，性别是XXX，成绩是：XXX
# str_name = input("请输入姓名；")
# str_age = input("请输入年龄；")
# str_sex = input("请输入性别；")
# str_score = input("请输入成绩；")
# #int 不能与str 拼接
# #不同类型需要转换成字符串后进行拼接
# print("我的姓名是" + str_name + "，年龄是" + str_age + "，性别是：" + str_sex + "，成绩是：" + str_score)


"""
练习1：计算找零
在控制台中获取一个商品单价    10
     再获取一个商品数量   3
     再获取一个金额   50
     计算：应该找回多少钱

"""
# str_price = input("请输入单价:")
# str_num = input("请输入数量:")
# str_pay = input("请输入金额:")
# float_Ps = float(str_price)
# float_num = float(str_num)
# float_pay = float(str_pay)
# payback = float(float_pay - (float_Ps * float_num))
# print("应该找回" + str(payback))



"""
练习2：时间换算
在控制台中获取小时/分钟/秒，计算总秒数。

"""

# hour = int(input("小时数："))
# minute = int(input("分钟数："))
# second = int(input("秒数："))
# Total_seconds = second + minute * 60 +  hour * 60 * 60
# print(str(Total_seconds))

"""
练习3：换算斤 两
古代的称一斤16两
在控制台中输入两， 换算出是几斤几两。

"""

# total_tael = float(input("tael："))
# kilo = total_tael // 16
# tael = total_tael % 16
# print(str(kilo) + "斤" + "零" + str(tael) + "两")

"""
练习1：闰年判断
条件1：年份能被4整除，但是不能被100整除
或者条件2：年份能被400整除
在控制台中获取年份
判断是否为闰年，如果是则显示true， 否则显示false

"""

# year = int(input("请输入年份："))
# result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# print(result)
# if result == 1:
#     print("是闰年")
# else:
#     print("不是闰年")
"""
练习2：获取个位，十位，百位。。。。上的数值
在控制台中获取一个4位整数 1234
  计算每位相加和   1+2+3+4  -->   10
获取个位：
获取十位：
。。。。
"""
# num01 = int(input("请输入数字："))
# num02 = num01 % 10     # 个位
# print(num02)
# num03 = num01 // 10 % 10   # 十位
# print(num03)
# num04 = num01 // 100 % 10  # 百位
# print(num04)
# num05 = num01 // 1000 % 10   #  千位
# print(num05)
# result = num02 + num03 + num04 + num05
# print(result)

#或者这么做：
# int_inputnumber = int(input("请输入数字："))
# result = int_inputnumber % 10     # 个位
# print(result)
# result += int_inputnumber // 10 % 10   # 十位
# print(result)
# result += int_inputnumber // 100 % 10  # 百位
# print(result)
# result += int_inputnumber // 1000 % 10   #  千位
# print(result)

"""
练习：时间换算
在控制台中获取一个总秒数
计算几小时零几分钟零几秒钟。

"""
# int_input_second = int(input("请输入总秒数："))
# hour = str(int_input_second // 3600)
# minute = str(int_input_second // 60 % 60)
# second = str(int_input_second % 60)
# print(hour + "小时" + "零" + minute + "分钟" + "零" + second + "秒")

"""
练习1 奇数偶数判断
在控制台中获取一个整数
如果是奇数  则显示奇数   否则显示偶数

练习2 闰年平年判断
在控制台中获取一个年份
如果是闰年  则显示闰年   否则显示平年

"""
# #练习1
# int_input_num01 = int(input("请输入数："))
# if int_input_num01 % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")


# #练习2
# year = int(input("请输入年份："))
# result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# if result == 1:
#     print("是闰年")
# else:
#     print("是平年")

"""
练习1 ：温度换算器（华氏度，摄氏度，开氏度）
摄氏度 = （华氏度 - 32）/ 1.8
华氏度 = 摄氏度*1.8 + 32
开氏度 = 摄氏度 + 273.15
-- 在控制台中获取华氏度，计算摄氏度
-- 在控制台中获取摄氏度，计算华氏度
-- 在控制台中获取摄氏度，计算开氏度

"""
# float_input_fahrenheit = float(input("请输入华氏度："))
# result_centigrade = str((float_input_fahrenheit - 32) / 1.8)
# print("=" + result_centigrade + "摄氏度")
#
# float_input_centigrade = float(input("请输入摄氏度："))
# result_fahrenheit = str(float_input_centigrade*1.8 + 32)
# print("=" + result_fahrenheit + "华氏度")
#
# float_input_centigrade = float(input("请输入摄氏度："))
# result_kelvin = str(float_input_centigrade + 273.15)
# print("=" + result_kelvin + "开氏度")


"""
练习2： 在控制台中获取圆形半径， 计算面积（3.14*r的平方）和周长（2*3.14*r）

"""
# float_radius = float(input("请输入半径(mm)："))
# area = 3.14*float_radius**2
# round_area = round(3.14*float_radius**2, 3)   # 此句为保留3位小数，round()函数可以做四舍五入
# perimeter = 2*3.14*float_radius
# print(str(float_radius) + "毫米半径的圆的面积是：" + str(round_area) + "平方毫米" + ", 周长是：" + str(perimeter) + "毫米")


"""

修改“计算找零”的练习，如果金额不足，提示还差多少钱，如果金额够了，提示应找回多少钱
---尝试：如果总价达到100元，打八折

"""
# float_unite_price = float(input("请输入单价（元）:"))
# float_amount = float(input("请输入数量（个）:"))
# float_pay = float(input("请输入付款金额（元）:"))
# total_price = float_amount * float_unite_price
#
# if total_price >= 100:
#     payback = float_pay - total_price*0.8
#     if payback < 0:
#         print("金额不足，还差" + str(payback) + "元")
#     else:
#         print("消费已达到100元，八折优惠后应找零" + str(payback) + "元")
# else:
#     payback = float_pay - total_price
#     if payback < 0:
#         print("金额不足，还差" + str(payback) + "元")
#     else:
#         print("应找零" + str(payback) + "元")

"""
练习1：
在控制台中获取一个月份
打印季节（春1--3  夏4--6  秋7--9  冬10--12

"""
# int_input_month = int(input("请属于月份："))
# if 1 <= int_input_month <= 3:
#     print("春季")
# elif 4 <= int_input_month <= 6:
#     print("夏季")
# elif 7 <= int_input_month <= 9:
#     print("秋季")
# elif 10 <= int_input_month <= 12:
#     print("冬季")
# else:
#     print("输入错误")

# # if...elif...表示条件之间有关联，如果有一个满足其他则不执行了
# int_input_month = int(input("请属于月份："))
# if int_input_month <1 or int_input_month >12:
#     print("输入错误")
# elif int_input_month <= 3:
#     print("春季")
# elif int_input_month <= 6:
#     print("夏季")
# elif int_input_month <= 9:
#     print("秋季")
# else:
#     print("冬季")

# # if...if...表示条件之间没有关联，如果有一个满足其他条件还会区判断
# int_input_month = int(input("请属于月份："))
# if int_input_month <1 or int_input_month >12:
#     print("输入错误")
# if int_input_month <= 3:
#     print("春季")
# if int_input_month <= 6:
#     print("夏季")
# if int_input_month <= 9:
#     print("秋季")


"""
练习2：在控制台中输入一个季度
显示该季度中的月份

"""
# int_input_season = int(input("请输入季度："))
# if int_input_season <1 or int_input_season >4:
#     print("输入错误")
# elif int_input_season == 1:
#     print("有1.2.3月")
# elif int_input_season == 2:
#     print("有4，5，6月")
# elif int_input_season == 3:
#     print("有7，8，9月")
# else:
#     print("有10，11，12月")


"""
练习3： 在控制台中输入一个月份
返回该月的天数
1  3  5    7  8     10   12   ---->   31 天
4  6  9    11   -->  3天
2   --->  28天

"""
# int_input_month = int(input("请输入月份："))
# if int_input_month < 1 or int_input_month > 12:
#     print("输入错误")
# elif int_input_month == 2:
#     print("28天")
# elif int_input_month == 4 or int_input_month == 6 or int_input_month == 9 or int_input_month == 12:
#     print("30天")
# else:
#     print("31天")

"""
计算最大数
思路：假设第一个变量就是最大值
      然后依次与下面的几个变量进行比较，如果还有更大的则替换假设的。
      
"""
# num01 = 8
# num02 = 6
# num03 = 10
# num04 = 5
# max_valueW#Day_01x_value \= num01
# if max_value < num02:
#     max_value = num02
# if max_value < num03:
#     max_value = num03
# if max_value < num04:
#     max_value = num04
# print(max_value)

"""
练习1：在控制台中获取一个整数，判断是奇数还是偶数，要求使用真值表达式
"""
# int_input_num01 = int(input("请输入一个数："))
# if input_num01 % 2:
#     print("奇数")
# else:
#     print("偶数")

"""
练习2：在控制台中获取一个年份，如果是闰年给变量day赋值29， 平年赋值28.

"""
# year = int(input("请输入年份："))
# # day = None
# # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
# #     day = 29
# # else:
# #     day = 28
#
# day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
# #或者
# day = 29 if not year % 4 and year % 100 or not year % 400 else 28

"""
练习：循环判断输出中间数字
在控制台中分别获取两个整数，一个作为开始值（），一个作为结束值。
#    请输入\出中间的数字
#    8               13
#      9  10  11  12

"""
# int_input_num01 = int(input("请输入开始值"))
# int_input_num02 = int(input("请输入结束值"))
#
# while int_input_num01 < int_input_num02 -1:
#     int_input_num01 += 1
#     print(int_input_num01)
#     # if int_input_num01 >= int_input_num02:   #后面两行也可以删掉
#     #     break

"""
练习2：一张纸厚度是0.01毫米
请问，对折多少次，可以超过珠穆朗玛峰8848.43米？


"""
# thickness = 0.01 / 1000
# count = 0 #计数器
# while thickness <= 8848.43:
#     thickness *= 2
#     count += 1
#     if thickness > 8848.43:
#         print(count)
#         break

"""
练习：猜数字1.0
规则：系统产生1 ---100 之间的随机数
      让用户重复猜测，知道猜对了为止
      提示：大了    小了      猜对了
      
      猜数字2.0
      最多只能猜10次
"""
# #1.0
# import random
# random_number = random.randint(1,100)
#
# while True:
#     input_number = int(input("请输入："))
#     if input_number > random_number:
#         print("大了")
#     elif input_number < random_number:
#         print("小了")
#     else:
#         print("猜对了")
#         break

#2.0

# import random
# random_number = random.randint(1,100)
# count = 0
# print(random_number)
# while count < 10:
#     count += 1
#     input_number = int(input("第"+ str(count) + "次请输入:"))
#     if input_number > random_number:
#         print("大了")
#     elif input_number < random_number:
#         print("小了")
#     else:
#         print("猜对了")
#         break
# else:
#     # 只有从while 条件结束，才执行else 语句。
#     # （从循环体内部break, 不会执行）
#     print("没机会了你")


"""
练习：执行下列代码执行5次
input01 = input("请输入第一个变量:")
input02 = input("请输入第一个变量:")
input01, input02 = input02, input01


"""
# for element in range(6):  # range 里 ：0  1  2  3  4  5
#     input01 = input("请输入第一个变量:")
#     input02 = input("请输入第一个变量:")
#     input01, input02 = input02, input01
#     print(input01)
#     print(input02)

"""
练习：随机加法考试
随机产生两个数字
在控制台中获取两个数字的相加结果
如果输入正确成绩累加10分
如果输入错误成绩扣除5分
总共5道题
"""
# import random
# score = 0
# for element in range(5):
#     random_number01 = random.randint(1, 5)
#     random_number02 = random.randint(1, 5)
#     result_input = int(input("请计算：" + str(random_number01) + "+" + str(random_number02) + "="))
#     if result_input == random_number01 + random_number02:
#         score += 10
#         print("You are Right, your score + 10 = " + str(score))
#     else:
#         score -= 5
#         print("You are Right, your score - 5 = " + str(score))
# else:
#     print("Finish your final score is " + str(score))

"""
累加1 -- 100 之间 能被3  整除的整数和

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
# print(sum)

"""
练习1 ：半衰落球计数，记距
一个球从100米的高度落下，每次弹回原高度的一半。
   总共谈起多少次？（假定：最小弹起高度是0.01m)
   总共走了多少米？
"""
# hight = 100
# count = 0
# distance = 100
# while 0.01 <= hight / 2:
#     count += 1
#     hight /= 2
#     distance += hight * 2
#     print("第" + str(count) + "谈起高度是" + str(hight))
# print(count)
# print(str(distance) + str(hight))






"""
在控制台中获取一个整数，判断是否为素数（只能被1和自身整除的数字）。
例如：9
    判断9能否被 2--8之间的数字整除
    如果能，说明不是素数。
    如果都不能，说明是素数。
    
     7
    判断7能否被 2--6之间的数字整除
    如果能，说明不是素数。
    如果都不能，说明是素数。
    
提示：循环2到 该数字-1 之间的整数
    再判断能否被整除
    if 数字 % 之间的整数 == 0:
        不是素数
"""

# int_input_num = int(input("请输入整数："))
# if int_input_num < 2:
#     print("不是素数")
# else:
#     for element in range(2 , int_input_num):
#          if int_input_num % element == 0:
#             print("不是素数")
#             break
#     else:
#         print("是素数")


"""
练习1：在控制台总获取一个字符串，打印每个字的编码值
"""
# str_input = input("请输入文字：")
# for item in str_input:
#     print(ord(item))

"""
练习2：在控制台总循环输入编码值，显示字符，知道输入负数时，退出。
"""
# while True:
#     number = int(input("请输入编码值："))
#     if number < 0:
#         break
#     print(chr(number))


"""
练习：在控制台中显示120秒倒计时
02:00   01:59   ....... 00:00
"""
# for second in range(120,-1,-1):
#     print("%02d:%02d" % (second // 60,second % 60))

"""
练习：在控制台中，获取一个字符串。
1. 打印第一个字符
2. 打印最后一个字符
3. 如果是奇数，打印中间的字符串（字符串长度---len(字符串)
4. 打印倒数3个字符
5. 倒叙打印字符串
"""
# str_input = input("请输入")
# #1. 打印第一个字符
# print(str_input[0])
# #2. 打印最后一个字符
# print(str_input[-1])
# #3. 如果是奇数，打印中间的字符串（字符串长度---len(字符串)
# if len(str_input) % 2 == 1:
#     print(str_input[len(str_input) // 2])
# #4. 打印倒数3个字符
# print(str_input[-3:])
# #5. 倒叙打印字符串
# print(str_input[::-1])

"""
练习  在控制台中输入一个整数，根据整数打印一个矩形。
 4
****
*  *
*  *
****
"""
# input_num = int(input("请输入"))
# #头
# print("*" * input_num)
# #中间
# for i in range(input_num - 2):
#     print("*" + " " * (input_num - 2) + "*")
# #尾
# print("*" * input_num)


"""
练习：在控制台中录入学生成绩,计算总分，最高分，最低分。
"请输入学生总数："
"请输入第一个学生成绩：
......

"""
# stu_count = int(input("请输入总人数："))
# list01 = []
# for i in range(stu_count):
#     score = int(input("请输入第%d学生："%(i+1)))
#     list01.append(score)
# print("总分：%d"%(sum(list01)))
# print("最高分：%d"%(max(list01)))
# print("最低分：%d"%(min(list01)))


"""
练习2：在控制台中录入学生姓名
       要求：姓名不能重复
            如果录入esc，则停止录入，打印每个学生姓名。
"""

# list_name = []
# while True:
#     stu_name = input("请输入姓名：")
#     if stu_name == "esc":
#         break
#     if stu_name not in list_name:
#         list_name.append(stu_name)
#
# for item in list_name:
#     print(item)

"""
练习：在列表中找最大元素
"""
# list01 = [34,5,6,78,9,0,5,8,88,4]
# #假设第一个元素就是最大值
# min = list01[0]
# #依次与后面的元素进行比较
# for i in range(1,len(list01)):
# #发现更大的，则替换假设的
#     if min < list01[i]:
#         min = list01[i]
# #最后假设的就是真的最大值
# print(min)

"""
练习：在列表中找最小元素
"""

# list01 = [34,5,6,78,9,0,5,8,88,4]
# #假设第一个元素就是最大值
# min = list01[0]
# #依次与后面的元素进行比较
# for i in range(1,len(list01)):
# #发现更大的，则替换假设的
#     if min < list01[i]:
#         min = list01[i]
# #最后假设的就是真的最大值
# print(min)

# #另一种表达方式，但不推荐
# list01 = [34,5,6,78,9,0,5,8,88,4]
# #假设第一个元素就是最大值
# min = list01[0]
# #依次与后面的元素进行比较
# for item in list01[1:]:     # 用切片方法是新生成新的切片列表巨大空间浪费，不推荐
# #发现更大的，则替换假设的
#     if min > item:
#         min = item
# #最后假设的就是真的最大值
# print(min)

"""
字符串与列表

"""
# #根据某些逻辑，拼接成一个字符串。
# list_result = []
# for item in range(10):
#     #以下方法不用每次拼接，都生成一个列表
#     list_result.append(str(item))
# #join: 将列表使用连接符，合成一个字符串
# str_result = "-".join(list_result)
# print(str_result)
#
# #splite：根据分隔符拆分字符串
# list01 = str_result.split("-")
# print(list01)

"""
练习：在控制台中循环录入字符串，输入q时退出。
      然后显示一个新的字符串。
"""
# list01 = []
# while True:
#     str_input = input("请输入：")
#     if str_input != "q":
#         list01.append(str_input)
#     if str_input == "q":
#         break
# print(list01)



"""
练习： 判断字符串是否是回文：
    上海自来水来自海上
    奶牛场牛奶
    提示：字符串反转
"""
# str01 = None
# while True:
#     str01 = input("请输入：")
#     if str01 == "esc":
#         break
#     if str01 != str01[::-1]:
#         print("不是回文")
#     if str01 == str01[::-1]:
#         print("是回文")

"""
练习：双色球
一注彩票7个球
前六个球是红球：1 ~ 33 之间的数字， 且不能重复
最后一个是篮球：1 ~ 16 之间的数字
（1）在控制台中购买彩票：
（2）随机产生一注彩票
import random
number = random.randint(1,33)
"""
# # （1）在控制台中购买彩票：
# ticket = []
# # 前六个红球
# while len(ticket) < 6:
#     number = int(input("请输入第%d个篮球数字：" % (len(ticket) + 1)))
#     if number < 1 or number > 33:
#         print("不在范围内")
#     elif number in ticket:
#         print("该号码已经存在")
#     else:
#         ticket.append(number)
# #篮球
# while True:
#     number = int(input("请输入篮球号码："))
#     if 1<= number <= 16:
#         ticket.append(number)
#         break  #退出循环
#     else:
#         print("不在范围内")
#
# # print(ticket)   # 只是将列表转换为字符串    再显示
#
# #获取每个元素
# for item in ticket:
#     print(item)
#
# #（2）随机产生一注彩票
# import random
# ticket = []
# while len(ticket) < 6:
#     number = random.randint(1,33)
#     if number not in ticket:
#         ticket.append(number)
# #整体排序
# ticket.sort()
#
# # number = random.randint(1,16)
# # ticket.append(1,16)
# ticket.append(random.randint(1,16))
# #通过切片返回昕列表
# temp = ticket[:6]
# #对新列表进行排序
# temp.sort()
# #将新列表赋值给原列表
# ticket = temp
# print(ticket)

"""
列表推导式
练习：使用range 生成1--10 之前的数字，存入列表list01中。
      使用列表推导式，将list01中所有奇数存入list02
                     将list01中所有奇数存入list02 
                     将list01中元素大于3的存入list03

"""

# # list01 = []
# # for item in range(1,11):
# #     list01.append(item)
#
# list01 = [item for item in range(1, 11)]
# list02 = [item for item in list01 if item % 2 == 1]
# list03 = [item for item in list01 if item % 2 == 0]
# list04 = [item for item in list01 if item > 3]

"""
根据月份计算天数
"""
# int_input_month = int(input("请输入月份："))
# if int_input_month < 1 or int_input_month > 12:
#     print("输入错误")
# elif int_input_month == 2:
#     print("28天")
# # elif int_input_month == 4 or int_input_month == 6 or int_input_month == 9 or int_input_month == 12:
# elif int_input_month in (4, 6, 9, 11):
#     print("30天")
# else:
#     print("31天")

# month = int(input("请输入月份："))
# # if month < 1 or month > 12:
# #     print("输入错误")
# # else:
# #     #将每月的天数，存入元组
# #     day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# #     print(day_of_month[month - 1])

"""
练习：
    在控制台中输入月，日
    计算这是一年的第几天
例如：3月5日
     累加1月，2月总天数，再累加3月的第五天
例如：5月10日
     累加1月，2月，3月，4月总天数，再累加5月的10天
"""
# month = int(input("请输入月份："))
# day = int(input("请输入天："))
# day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#
# #累加前几个月
# # result = 0
# # for i in range(month - 1):
# #     result += day_of_month[i]
# result = sum(day_of_month[:month])
# #累加当月
# result += day
# print(result)



"""
练习：
在控制台中录入一个字符串
打印这个字符串中的字符以及出现的次数
    abcdbcd
    a字符1次
    b    2
    c    2
    d    2
字符  in 字符串     
"""
str_input = "abcdbcd"
#key: 字符   value:次数
result = {}
#逐一判断字符出现的次数
for item in str_input:
    #如果没有统计过该字符串
    if item not in result:
        result[item] = 1
    else:
        #(3)否则，次数增加
        #result[item] = result[item] + 1
        result[item] +=1
print(result)


















































































