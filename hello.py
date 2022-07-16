# print("hello")
# x = 5 + 5
# print(x)
# x = 3 / 0

# # print(x)
# # print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
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
# fibonachi = fibo(int(input(("enter a turms of fibo series "))))

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
# print(list(file))
# print(file.keys())
# print(file.values())
# print(file.items())

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






