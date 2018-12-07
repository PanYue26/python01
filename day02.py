# print("tom's pet is a cat")
# world=('hello\nworld')
# print(world)
# a='''1.2.3.'''
# print (a)
# a='''1
# 2
# 3'''
# print (a)
# a='1\n2\n3'
# print (a)
# a='helloworld'
# print (len(a))
# print(a[2:4])
# print(a[4:5])
# print(a[:3])
# print(a[4])
# print (a[-1])
# print(a[-10])
# print (a[-10:])
# print (a+' haha')
# print ('*'*50)
# print (a*3)
# print ('a' in a)
# print('ll' in a)
# print ('wo' in a )
# print (a[0:0])
# print (a[:])
# print (a[::-1])
# print (a[::2])
# print (a[-5:-2])
# print (a[-10:-9])
# print (a[-10::-10])
# list=[10,20,'haha','xixi']
# # # print(len(list))
# # # print(list[0])
# # # print(list[0:2])
# # # print(list[2:4])
# # # print(list*2)
# # # list[-1]= 'hehe'
# # # print(list)
# # list.append('lele')
# # # print(list)
# # print(list[-1])
# # list=(11,22,33,44)
# # print(list)
# # # list.append(55)
# # print(list[-1])
# # print(list[::2])
# user={'name':'lisi','age':20,'like':'play'}
# # print(user)
# # print(user['like'])
# # print(len(user))
# # user['tel']=8208208820
# # user['age']=18
# # print(user)
# # user['sex','ss']='boy','haha'
# # print(user)
# # print('age' in user)
# # if 10 < 20 :
# #     print('Ture')
# # else:
# #     print('False')
# # if 33 in list:
# #     print('yes')
# # if 55 not in list:
# #     print('yes')
# # if 'hh' in list:
# #     print('hh')
# # else:
# #     list.append('hh')
# #     print(list)
# if not None:
#     print('true')
# name=input('username:')
# import getpass
# passwd=getpass.getpass('pass:')
# print(name,passwd)
# ll
# ll
# import random
# number=random.randint(1,100)
# print(number)
# answer=int(input('请输入：'))
# if number > answer:
#     print('猜小了')
# elif number < answer:
#     print('猜大了')
# else:
#     print('猜对了')
# a=100
# b=80
# # if a < b:
# #     smaller=a
# # else:
# #     smaller=b
# # print(smaller)
# smaller=a if a < b else b
# print(smaller)
# score=int(input('请输入你的分数：'))
# if score >=90:
#     print('优秀')
# elif score >=80:
#     print('好')
# elif score >=70:
#     print('良')
# elif score >=60:
#     print('及格')
# else:
#     print('你要努力了')
# a=int(input('请输入你的分数：'))
# if 60<= a < 70:
#     print('及格')
# elif 70 <= a < 80:
#     print('良')
# elif 80 <=a < 90:
#     print('好')
# elif 90 <= a:
#     print('优秀')
# else:
#     print('你要努力了')
# import random
#
# all_choice = ['石头', '剪刀', '布']
# win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# computer = random.choice(all_choice)
# player = input('请出拳(石头/剪刀/布): ')
#
# print('你的出拳:', player, ', 计算机出拳:', computer)
# if player == computer:
#     print('平局')
# elif [player, computer] in win_list:
#     print('You WIN!!!')
# else:
#     print('You LOSE!!!')

# sum=0
# counter=1
# while counter <= 100:
#     sum += counter
#     counter += 1
# print(sum)

# sum=0
# counter=100
# while counter <=100:
#     sum += counter
#     counter -= 1
# print(sum)
# import random
# number=random.randint(1,10)
# answer=int(input('请输入1-10的数字：'))
#
# if number > answer:
#     print('猜小了')
# elif number < answer:
#     print('猜大了')
# else:
#     print('猜对了')

# import random
# number=random.randint(1,10)
# run = 2
# while run:
#     answer=int(input('请输入1-10的数字：'))
#
#     if number > answer:
#         print('猜小了')
#     elif number < answer:
#         print('猜大了')
#     else:
#         print('猜对了')
#         run = 0
# import random
# number=random.randint(1,10)

# while True:
#     answer = int(input('请输入1-10的数字：'))
#     if number > answer:
#         print('猜小了')
#     elif number < answer:
#         print('猜大了')
#     else:
#         print('猜对了')
#         break


# sum=0
# num=0
# while num < 100:
#     num += 1
#     if num % 2:
#         continue
#     sum += num
# print(sum)

# sum=0
# num=0
# while num <= 100:
#     sum += num
#     num += 1
# print(sum)
a='hello'
# print(len(a))
# print(a[1])
# print(a[4])
# print(len(a) -1)
# print(a[-1])
# print(a[:5])
# print(a[:])
# print(a[1:])
# print(a[::-1])
# print(a[::1])
# print(a[::2])
# print(a+' world')

# print('#'*50)
# print('''1*1
# 2*2
# 3*3
# ''')
# print('*'*8\n)

# a=[1,2,3,4,'a','b']
# print(a)
# print(a[-1])
# a.append('c')
# print(a)
# a[-1]='d'
# print(a)

# a={'name':'tom','age':18,'sex':'boy'}
# print(a)
# # print(a[1])
# print(a['name'])
# print('age' in a)
# a['like']='read'
# print(a)

# a=100
# b=80
# if a < b:
#     smaller=a
# else:
#     smaller=b
# print(smaller)
# smaller=a if a < b else b
# print(smaller)

# import random
# a=random.choice(['石头','剪刀','石头'])
# b=input('请出拳：')
# print('计算机的出拳：',a,', 你的出拳：',b)
# if b=='石头':
#     if a == '布':
#         print('你输了')
#     elif a =='剪刀':
#         print('你赢了')
#     else:
#         print('平局')
# elif b=='剪刀':
#     if a == '布':
#         print('你赢了')
#     elif a =='剪刀':
#         print('平局')
#     else:
#         print('你输了')
# else:
#     if a == '布':
#         print('平局')
#     elif a =='剪刀':
#         print('你输了')
#     else:
#         print('你赢了')

# import random
# a=['石头','剪刀','布']
# com=random.choice(['石头','剪刀','布'])
# win=[[[a[0],a[1]]],[[a[1],a[2]]],[a[2],a[0]]]
# play=input('请出拳：')
# print('计算机的出拳：',com,', 你的出拳：',play)
# if com==play:
#     print('平局')
# elif [play,com] in win:
#     print('win')
# else:
#     print('lose')

# import random
# a=['石头','剪刀','布']
# com=random.choice(['石头','剪刀','布'])
# win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# b='''0:石头
# 1：剪刀
# 2：布
# 请出拳：'''
# index=int(input(b))
# play=a[index]
# print('计算机的出拳：',com,', 你的出拳：',play)
# if com==play:
#     print('平局')
# elif [play,com] in win_list:
#     print('\033[32;1mwin\033[0m')
# else:
#     print('\034[34;mlose\034[0m')

# import random
# a=['石头','剪刀','布']
# win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# time=0
# win=0
# while time<3 :
#     com = random.choice(['石头', '剪刀', '布'])
#     print('计算机的出拳：', com)
#     b = '''
#         0:石头
#         1：剪刀
#         2：布
#         请出拳：'''
#     index=int(input(b))
#     play = a[index]
#     if com==play:
#         print('平局')
#     elif [play,com] in win_list:
#         print('win')
#         win+=1
#         while win > 2:
#             break
#     else:
#         print('lose')
#     time += 1

import random
a=random.randint(1,100)
time=0
while time <5:
    print(a)
    b=int(input('请输入一个数字：'))
    if a < b or a > b:
        print('你猜错了')
    else:
        print('猜对了')
        break
    time +=1


