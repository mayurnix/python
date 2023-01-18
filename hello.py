# print("hello")
# x = 5 + 5
# print(x)
# x = 3 / 0

# print(x)
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# print('Welcome to Python!')
# print('Welcome', 'to', 'Python!')
# print("hello, \"friend\"")
# print('hello, "friend"')
# print("hello, 'friend'")
# print('Welcome\nto\n\nPython!')
# print('this is a longer string, so we \
# ...: split it over two lines')
# print('Sum is', 7 + 3)
# print('int(5.2)', 'truncates 5.2 to', int(5.2))
# print('Display "hi" in quotes')
# print("Display the name O'Brien")
# print("Display \"hi\" in quotes")
# print("""Display "hi" and 'bye' in quotes""")

# # input 
# name = input('What is your name? \n')
# print = (name)

# hello.py
# print('Enter two integers, and I will tell you','the relationships they satisfy.')
# # read first integer
# number1 = int(input('Enter first integer: '))
# # read second integer
# number2 = int(input('Enter second integer: '))
# if number1 == number2:
#  print(number1, 'is equal to', number2)
# if number1 != number2:
#  print(number1, 'is not equal to', number2)
# if number1 < number2:
#  print(number1, 'is less than', number2)
# if number1 > number2:
#  print(number1, 'is greater than', number2)
# if number1 <= number2:
#  print(number1, 'is less than or equal to', number2)
# if number1 >= number2:
#  print(number1, 'is greater than or equal to', number2)

# guju=input("what is your age ? \n ")
# boss=int(guju)
# # print(boss+1)
# # print(boss) == print(+boss)
# print(-boss)... -age
# print(*boss)... TypeError: print() argument after * must be an iterable, not int
 
# def john():
#     print("He was a gangster ?")
#     print("He is good man ?")
# print('it is all about john wike')
# john()
# print("he lost he's wife")
# john()
# john()

# def age(introduction):
#     # introduction = input('enter your age: ') 
#     # introduction = int(introduction)
#     if introduction < 18 :
#         print('you are a child')
#     elif introduction==18 : 
#         print('now you are adult')
#     elif introduction in list(range(19,30)) :
#         print('you become a men')
#     else :
#         print('you are old man')
# age(73)

# The "try" block lets you test a block of code for errors. 
# The "except" block lets you handle the error.

# def man():
#     return "mayur"
# print(man(), "mistry")

# def man(a, b):
#     add = a + b 
#     return add
# x=man(5, 6)
# print(x)
    
# for i in range(1,100):
#     if i%2==0 or i%3==0 or i%5==0 or i%7==0 or i%9==0 :
#         continue
#     print(i)
# print("stop")
         
# for n in range(1,10):
#     if n<50:
#         print(6*n+1,6*n-1)

# while True:
#         line = input(">>")
#         if line == "stop" :
#                 break
#         print(line)
# print("Stop!")

# while True:
#         line = input(">>")
#         if line == "start":
#                 continue
#         if line == "stop" :
#                 break
#         print(line)
# print("Stop!")
           
# # Find a Smallest number 
# smallest = None
# for x in [12,5,25,2,75,65,7,57,39]:
#     if smallest is None or x < smallest :
#         smallest=x
#         print(x,smallest)
# print('Smallest = ',smallest)

# # Find a largest number 
# largest = None
# for x in [12,5,25,2,75,65,7,57,39]:
#     if largest is None or x > largest :
#         largest=x
#         print(x,largest)
# print('Largest = ',largest)

# Find a smallest & largest number 
# smallest = None
# largest = None
# numbers = [15,58,79,65,12,89,23,29,37,97,5,77,99,11,17]
# for x in numbers:
#     if smallest is None or x < smallest :
#         smallest=x        
# print('Smallest = ',smallest)
# for x in numbers:
#     if largest is None or x > largest :
#         largest=x          
# print('Largest = ',largest)

# ironman ='robertdowneyjunior'
# index = 0
# while index < len(ironman) :
#     print(index, ironman[index])
#     index = index + 1

# for n in "banana":
#     print(n)

# ironman ='robertdowneyjunior'
# # r o b e r t d o w n e  y  j  u  n  i  o  r
# # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
# print(ironman[2:5])
# print(ironman[:12])
# print(ironman[12:])

# print("robert"+"downey"+"junior")
# print("robert"+" downey"+" junior")
# print("robert"+" "+"downey"+" "+"junior")

# print("IRONMAN".lower())
# print("ironman".upper())
# print("IROnmaN".lower())
# print("iRonMan".upper())

# ironman ='robertdowneyjunior'
# # print(ironman.find("ju"))
# print(ironman.find("m"))
    
# def fibo(n) :
#     a = 1
#     b = 1   
#     if n == 1 :
#         print(a)
#     elif n == 2 :
#         print(b)
#     else :
#         print (a)
#         print (b)
#         for i in range(2,n) :
#             c = a + b
#             a = b
#             b = c
#             print (c)
#             if c > 5000 :
#                 break
# Fibonacci = fibo(int(input(("enter a turms of fibo series "))))

# friends = ['mitesh', 'yash', 'brijesh', 'jayesh', 'aadit']
# print (len(friends))
# # for friend in friends : 
# #     print('Happy New Year: ', friend)
# for i in  range (len(friends)) :
#     friend = friends[2]
#     print('Happy New Year: ', friend)

# xyz= ' How are you? '
# print(xyz.split())
# xyz= 'How;are;you'
# print(xyz.split(';'))

# purse = dict()
# purse['money'] = 1000
# purse['candy'] = 5
# purse['card'] = 6 
# print(purse)
# print(purse['card'])
# # print(purse['card']+2)
# purse['candy'] = 11
# purse['photoid'] = 1
# print(purse)

# array = list()
# array.append(15)
# array.append(65)
# print(array)
# array[1] = 85
# print(array)

# counts = dict()
# names = ['ramesh', 'suresh','ramesh','mohit','suresh','ramesh']
# for name in names : 
#     if name in counts:
#         counts[name] = counts[name] + 1 
#     else :
#         counts[name]=1
# print(counts)

# counts = dict()
# names = ['ramesh', 'suresh','ramesh','mohit','suresh','ramesh']
# for name in names : 
#     counts[name] = counts.get(name,0) + 1
# print(counts)

# file = dict()
# file = {'ramesh': 3, 'suresh': 2, 'mohit': 1}
# file={'ramesh': 3, 'suresh': 2, 'mohit': 1}
# print(list(file))
# print(file.keys())
# print(file.values())
# print(file.items())

# for key in result
# counts = {'ramesh': 3, 'suresh': 20, 'mohit': 389}
# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])

# data = 'From stephan.ndksfin@ndv.nnd.vb. sat jan 5 09:14:16 2008'
# a = data.find('@')
# print(a)
# b = data.find(' ',a)
# print(b)
# c = data[a+1 : b]
# print(c)

# # use regular Expressions
# import re
# data = 'From stephan.ndksfin@ndv.nnd.vb. sat jan 5 09:14:16 2008'
# d = re.findall('@([^ ]*)',data)
# print(d)

# # Python program for implementation of Bubble Sort
# def bubblesort(elements):
#   swapped = False
#   for n in range(len(elements)-1, 0, -1):
#     for i in range(n):
#       if elements[i] > elements[i + 1]:
#         swapped = True
#         elements[i], elements[i + 1] = elements[i + 1], elements[i]  
#     if not swapped:
#         return
# # that's print to show how to work this programm 
#     # print(elements)
# elements = [39, 12, 18, 85, 72, 10, 2, 18]
# print('Unsorted list is')
# print(elements)
# bubblesort(elements)
# print("Sorted Array is, ")
# print(elements)

# # Python program for implementation of Bubble Sort
# def bubblesort(num):
#     for i in range(0,len(num)):
#         for j in range(i,len(num)): 
#             if num[i] > num[j] :
#                 num[i], num[j] = num[j], num[i]
#     print(num)
#     # return num
# nums = [35,5,54,87,36,-56,0,25,48,2,18,39]
# print(bubblesort(nums))

# open
# open(file, mode='r', buffering=-1, encoding=None, 
#       errors=None, newline=None, closefd=True, opener=None)
# mode
# 'r'  = open for reading (default) 
# 'w'  = open for writing, truncating the file first 
# 'x'  = open for exclusive creation, failing if the file already exists 
# 'a'  = open for writing, appending to the end of file if it exists 
# 'b'  = binary mode 
# 't'  = text mode (default) 
# '+'  = open for updating (reading and writing) 

# def num(n) :
#     a = 9
#     b = 0  
#     if b in range (0,987654321) :
#         print (b)
#         for i in range(0,n) :
#             c = a + b
#             b = c
#             print (c)
#             if i > 10 :
#                 break
# num(100)

# sum of number of turms 
# def Separate(num) :
#     srt1 = (num)
#     arr1 = list(map(int,srt1))
#     # print(arr1)
#     ans1 = sum(arr1)
#     # print(ans1)
#     if ans1 > 9 :
#         srt2 = str(ans1)
#         arr2 = list(map(int,srt2))
#         ans2 = sum(arr2)
#         print(ans2)
#         if ans2 > 9 :
#             srt3 = str(ans2)
#             arr3 = list(map(int,srt3))
#             ans3 = sum(arr3)
#             print(ans3)
# num = input("enter number: ")
# number = int(num)
# if number <= 9 :
#     print(num)
# else :
#     Separate(num)

# series of sum of number digit (sum=5)
# def Separate(num) :
#     p = 7
#     if num < 10 :
#         if num == p :
#             print(p)
#         return num
#     int1 = (num)
#     arr1 = [int(x) for x in str(int1)]
#     ans1 = sum(arr1)
#     if ans1 > 10 :
#         arr2 = [int(x) for x in str(ans1)]
#         ans2 = sum(arr2)
#         if ans2==p :
#             print(num)
#         elif ans2 > 10 :
#             arr3 = [int(x) for x in str(ans2)]
#             ans3 = sum(arr3)
#             if ans3==p :
#                 print(num)
#     elif ans1==p :
#         print(num)
#     return num
# no = int(input("Enter number: "))
# i = 1
# while i <= no:
#     i = i + 1
#     Separate(i)

# # series of natural numbers
# no = int(input("Enter number: "))
# i = 1
# print(1)
# while i <= no:
#     i = i + 1
#     print(i) 

# # series of even numbers
# no = int(input("Enter number: "))
# i = 2
# print(2)
# while i <= no:
#     i = i + 2
#     print(i)

# # series of odd numbers
# no = int(input("Enter number: "))
# i = 1
# print(1)
# while i <= no:
#     i = i + 1
#     if i%2 != 0 :
#         print(i)

# # series of p square 
# no = int(input("Enter number: "))
# p = int(input("which number do you have square: "))
# i = p
# print(p)
# while i <= no:
#     i = i*p
#     print(i)

# # use.stripe 
# x= "           which number do you have square           "
# print(x.strip()) 

# # using socket
# import socket
# path = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# path.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# path.send(cmd)
# while True:
#     data = path.recv(512)
#     if (len(data)<1):
#         break
#     print(data.decode())
# path.close()

# # Using uellib
# import urllib.request, urllib.parse, urllib.error 
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

# # Using requests
# import requests
# x = requests.get('https://w3schools.com/python/demopage.htm')
# print(x.text)

# # use xml
# import xml.etree.ElementTree as ET 
# data = '''<person>
#     <name>Chuck</name>
#     <phone type="intl">
#        +1 734 303 4456
#     </phone>
#     <email hide="yes"/>
# </person>'''
# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))

# # use json
# import json
# data = '''
#   [
#     { "id" : "001",
#       "x" : "2",
#      "name" : "Quincy"
#     } ,
#     { "id" : "009",
#       "x" : "7",
#       "name" : "Mrugesh"
#     }
#   ]
# '''
# info = json.loads(data)
# # print(info[1]['name'])
# print('user count: ', len(info))
# for item in info:
#     print('Name', item['name'])
#     print('id', item['id'])
#     print('attribute', item['x'])

# counts = dict()
# names = {'ramesh': 3, 'suresh': 20, 'mohit': 389}
# total=0
# for key in names : 
#     total += names[key]
# print(total) 
# 1..........
# fromuser = input("Enter student name : ")
# file = dict()
# file = {"ramesh":{'physics':95,'science':72,'maths':98},
# "suresh":{'physics':87,'science':65,'maths':35},
# "mahesh":{'physics':65,'science':79,'maths':85}}
# total=0
# if fromuser=="ramesh":
#     A = file["ramesh"]
#     print(A)
#     for key1 in A : 
#         total += A[key1]
#     print(total)
# elif fromuser=="suresh":
#     B = file["suresh"]
#     print(B)
#     for key2 in B : 
#         total += B[key2]
#     print(total)
# elif fromuser=="mahesh":
#     C = file["mahesh"]
#     print(C)
#     for key3 in C : 
#         total += C[key3]
#     print(total)
# else :
#     print("This Name is not in the file")
# 2......
#    fromuser = input("Enter student name : ")
# file = {"ramesh":{'physics':95,'science':72,'maths':98},
# "suresh":{'physics':87,'science':65,'maths':35},
# "mahesh":{'physics':65,'science':79,'maths':85}}
# if fromuser=="ramesh" :
#     S = file.get('ramesh')
#     print(S)
#     print(sum(S.values()))
# elif fromuser=="suresh" :
#     print(S)
#     S = file.get('suresh')
#     print(sum(S.values()))
# elif fromuser=="mahesh" :
#     print(S)
#     S = file.get('mahesh')
#     print(sum(S.values()))
# else :
#     print("This Name is not in the file")
# 3.......
# fromuser = input("Enter student name : ")
# file = {"ramesh":{'physics':95,'science':72,'maths':98},
# "suresh":{'physics':87,'science':65,'maths':35},
# "mahesh":{'physics':65,'science':79,'maths':85}}
# if fromuser=="ramesh":
#     print(sum(file["ramesh"].values()))
# elif fromuser=="suresh":
#     print(sum(file["suresh"].values()))
# elif fromuser=="mahesh":
#     print(sum(file["mahesh"].values()))
# else :
#     print("This Name is not in the file")
# 4.....
# fromuser = input("Enter student name : ")
# file = {"ramesh":{'physics':95,'science':72,'maths':98},
# "suresh":{'physics':87,'science':65,'maths':35},
# "mahesh":{'physics':65,'science':79,'maths':85}}
# for k, v in file.items() :
#     if k==fromuser :
#         print(sum(file[k].values()))


# file = {"ramesh":{'physics':95,'science':72,'maths':98},
# "suresh":{'physics':87,'science':65,'maths':35},
# "mahesh":{'physics':65,'science':79,'maths':85}}
# file1 = []
# for k, v in file.items() :
#     total=sum(file[k].values())
#     file1.append(total)
# K=file.keys()
# V=file1
# print("File of student name with total marks")
# file3=dict(zip(K,V))
# print(file3)
# # print(file.items())
# # output:dict_items([('ramesh', {'physics': 95, 'science': 72, 'maths': 98}),
# #  ('suresh', {'physics': 87, 'science': 65, 'maths': 35}), 
# #  ('mahesh', {'physics': 65, 'science': 79, 'maths': 85})])

# # create a simple list using append
# list1=[]
# list1.append(15)
# list1.append(25)
# print(list1)
# # create a simple list using extend
# List2 = [25,89,45,"python",15]
# list1.extend(List2)
# print(list1)
# # create a integer list using for loop
# list3=[]
# for i in range(0,10) :
#     list3.append(i)
# print(list3)

# # create a simple list using for-loop
# list=[]
# for i in range(0,6) :
#     list.append(i)
# print("list:",list)
# # create a nested list
# list1=['A','B','C']
# list3=[list,list1]
# print("nested list:",list3)
# # creat a empty list
# list.clear()
# print("empty list:",list)
# # output:list: [0, 1, 2, 3, 4, 5]
# # nested list: [[0, 1, 2, 3, 4, 5], ['A', 'B', 'C']]
# # empty list: []

# # swap Element in list 
# list = [5,8,6,9,8]
# print("before swap :", list)
# b = int(input("enter list index No.1 : "))
# c = int(input("enter list index No.2 : "))
# a = list[b]
# list[b]=list[c]
# list[c]= a
# print("after swap :", list)
# # output: before swap : [5, 8, 6, 9, 8]
# # enter index No.1 : 1
# # enter index No.2 : 2
# # after swap : [5, 6, 8, 9, 8]
    
# # Find a largest number in list
# list = [1,5,6,9,15,65,2,9,45,85,152,22,7,10,3]
# max = None
# for x in list:
#     if max is None or x > max :
#         max=x
# print('maximum Number is',max)
# # output: maximum Number is 152

# list = [1,2,3,4,'mango',25,15,'banana',49,17]
# print(list)
# # remove element in list
# list.remove('mango')
# print(list)
# #insert element in list
# list.insert(2,'orange')
# print(list)
# # update element in list 
# list.remove(25)
# list.insert(5,24)
# print(list)
# # output=[1, 2, 3, 4, 'mango', 25, 15, 'banana', 49, 17]
# # [1, 2, 3, 4, 25, 15, 'banana', 49, 17]
# # [1, 2, 'orange', 3, 4, 25, 15, 'banana', 49, 17]
# # [1, 2, 'orange', 3, 4, 24, 15, 'banana', 49, 17]

# creat a dictionary
# list1=[1,2,3,4,5]
# list2=['apple','orange','mango','banana',]
# A = dict(zip(list1,list2))
# print('your dictionary is',A)
# output: your dictionary is 
# {1: 'apple', 2: 'orange', 3: 'mango', 4: 'banana'}

# word="jfeicie2ef626r"
# a = len(word)
# # b=0
# for i in range(-1,-a-1,-1): # range(-1,-a-1,-1) = range(a-1,-1,-1)
#     # b = b-1
#     print(word[i],end="")


# for i in range(5):
#     a=2
#     for j in range(5,i,-1):
#         print(a,end=" ")
#         a+=2
#     print()  

# for i in range(12,0,-2):
#     for j in range(2,i,2):
#         print(j,end=" ")
#     print()

# for i in range (1,7):
#     print(i*"* ")
#     print()
# for i in range (5,0,-1):
#     print(i*"* ")
#     print()

# for i in range (1,12):
#     if i<7:
#         print(i*" *")
#     else :
#         a = 12-i
#         print(a*" *")

# 2. Write a python program to print any alphabet.
# for i in range(1,6):
#     print("M",end="")
#     for j in range(1,10):
#         if i==j:
#             print("M",end="")
#         elif (i+(j-4))==6 and i<5:
#             print("M",end="")
#         else :
#             print(" ",end="")
#     print("M",end="")
#     print()
# _________________________________________
# n = int(input("enter value of i ="))
# for i in range(1,n+1):
#     for j in range(1,2*n):
#         if (i+j)==(n+1) and i<n:
#             print("M",end="")
#         elif i==(j-n+1) and i<n:
#             print("M",end="")
#         elif i<n:
#             print(" ",end="")
#     if i==n:
#         print(n*"M_")
#     print()
# ________________________________
# a=1
# for i in range(1,6):
#     for j in range(1,6):
#         if (i+j)<6 and i<5:
#             print(" ",end="")
#         if (i+j)==6 and i<5:
#             print("M",end="")
#         if (i+j)==7 and i<5:
#             print(a*" ",end="")
#             a+=2
#             print("M",end="")
#     if i==5:
#         print(5*"M ")
#     print()

# for i in range(10):
#     for j in range(10):
#         if i in [0,9]:
#             print("Z",end="")
#         elif j in [0,9]:
#             print("Z",end="")
#         else:
#             print(" ",end="")
#             # print(end=" ")
#     print()

# n = int(input("enter value of i ="))
# for i in range(1,n+1):
#     for j in range(1,2*n):
#         if (i+j)==(n+1) and i<n:
#             print("#",end="")
#         elif i==(j-n+1) and i<n:
#             print("#",end="")
#         elif i<n:
#             print(" ",end="")
#     if i==n:
#         print(n*"# ")
#     print()


# import matplotlib.pyplot as plt
  
# # x axis values
# x = [1,2,3,4,5,6]
# # corresponding y axis values
# y = [2,4,1,5,2,6]
  
# # plotting the points 
# plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
  
# # setting x and y axis range
# plt.ylim(1,8)
# plt.xlim(1,8)
  
# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
  
# # giving a title to my graph
# plt.title('Some cool customizations!')
  
# # function to show the plot
# plt.show() 


# # find a roots in given interval using False bisection method with plot
# import matplotlib.pyplot as plt
# a=float(input ("a="))
# b=float(input ("b="))
# if a>b:
#    m=a
#    a=b
#    b=m
# root=[]
# def f(x):
#     return (x*x)-(5*x)+6
#     # return (x*x)+(5*x)-6
# if (f(a)*f(b))<=0:
#     while True:
#         if abs(a-b)<0.0001:
#             break
#         else:
#             c=(a+b)/2
#             if (f(c)*f(b))<0:
#                 a=c
#             else:
#                 b=c
#         root.append(c)
# else:
#     print("entre valid inreval")
# print(root)
# plt.plot(root)
# plt.show()


# # find a roots in given interval using False Position Method (or) Regula Falsi Method with plot
# import numpy as np
# import matplotlib.pyplot as plt
# a=float(input ("a="))
# b=float(input ("b="))
# if a>b:
#    m=a
#    a=b
#    b=m
# root=[]
# def f(x):
#      return x*x-5*x+6
# if (f(a)*f(b))<=0:
#     while True:
#         c=(a*f(b)-b*f(a))/(f(b)-f(a))
#         root.append(c)
#         print("c=",c)
#         if (b-c)<0.00000001:
#             break
#         b=c
# else:
#     print("entre valid inreval")
# print(root)
# plt.plot(root)
# # b = np.arange(0,10,0.005)
# # y = b*b-5*b+6
# # plt.plot(b,y)
# plt.show()





# D = {}
# n = int(input("Enter a number of student you have: "))
# while len(D) < n :
#     name = input("Enter name: ")
#     grad = float(input("Enter his grad: "))
#     D[name] = grad
# # print("1",D)
# a = sorted(D.items(),key = lambda x : x[1])
# # print("2",a)
# list = [a[0][0],a[1][0]]
# b = sorted(list)
# # print("3",b)
# print(b[0])
# print(b[1])

# print(dict(map(lambda x: (x[0], x[1]+5), D.items() ))) # changise in values
# g = list(D.values()) # use to print values
# s = list(D.keys()) # use to print keys
# print(s)

# D = {}
# n = int(input())
# while len(D) < n :
#     name = input()
#     grad = float(input())
#     D[name] = grad
# # print("1",D)
# a = sorted(D.items(),key = lambda x : x[1])
# # print("2",a)
# list = [a[0][0],a[1][0]]
# b = sorted(list)
# # print("3",b)
# print(b[0])
# print(b[1])



# L1=[]
# for i in range (5):
#     L2=[]
#     for j in range (3):
#         L2.append(input("="))
#     L1.append(L2)
# print(L1)



# marksheet=[]
# marks=[]
# x=int(input())
# for i in range(x): 
#     name=input()
#     grade=float(input())
#     marksheet+=[[name,grade]] 
#     marks+=[grade]
# sl=(sorted(set(marks))) [1] 
# for i,j in sorted (marksheet):
#     if j==sl: 
#        print(i)