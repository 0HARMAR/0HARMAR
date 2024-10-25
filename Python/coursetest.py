'''
:@Author: hmy
:@Date: 2024/9/19 09:55:19
:@LastEditors: hmy
:@LastEditTime: 2024/9/26 08:47:44
:Description: 
:Copyright: Copyright (©) 2024 hmy. All rights reserved.
'''

import random
# x,y,z = input("please input three values").split()

# print(x,y,z)

# first test .......................................................................

# mulit = 1
# n = int(input("请输入一个数字"))

# for i in range(1,n+1):
#     if i % 2 == 0:
#         mulit *= i

# print(f"result : {mulit}")

# second test ......................................................................

# def sm(n):
#     if n == 1:
#         c = 100
#     else :
#         c = sm(n-1)*1.035
#     return c
# n = int(input("请输入n年："))

# print(f"result : {sm(n):.2f}")

# join test
# str = '123456'

# str_list = list(str)

# print(str_list)

# str = ",".join(str_list)

# print(str)

# third test

# while(1):
#     name = input("please input name : ")

#     skills = input("please input skills : ")

#     wage = int(input("please input wage : "))

#     if ("计算机" or "编程" in skills) and wage <= 4000:
#         print(f"{name} : you ared hired!")

# str1 = '**'
# str2 = "python"

# print(str2.join(str1)+ str2)

# words = input("please input a santense: ")
# bereplaced = input("please input a bereplaced word: ")

# if bereplaced in words:
#     newword = input("new word: ")
#     print(words.replace(bereplaced,newword))
# else:
#     print(f"{bereplaced} not in {words},please 好好看看!")

# words = input("please input a string: ")

# result = []

# for word in words:
#     if word.isdigit():
#         intword = int(word)
#         if intword % 2 == 0:
#             result.append(str(intword))

# result = "".join(result)
# print(result)

# str1 = '---'
# str2 = '*'*11
# print(str1 + str1.join(str2))

# words = input("please input a words: ")

# for i in range(-1,-len(words)-1,-1):
#     print(words[i],end="")

# NUM = 198

# print(bin(NUM))
# print(oct(NUM))
# print(hex(NUM))

# words = "hemingyang"

# print("{}".format(words))

# n = int(input("请输入n"))

# result = 0

# for i in range(1,n+1):
#     if i % 2 != 0:
#         result += i
        
# print(result)

# given_num = random.randint(0,100)

# while True:
#     n = int(input("please input a num"))
#     if(n < given_num):
#         print("too low")
#     elif(n > given_num):
#         print("too big")
#     else:
#         print(f"you are right,num is {given_num}")
#         break

# 判断回文数

n = input("please input a 四位数")

if n[0] == n[3] and n[1] == n[2]:
    print("you are right")


