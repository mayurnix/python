# Assignment_8
# python

# 1.Write a Python program to create a lambda function that adds 15 to a
# given number passed in as an argument, also create a lambda function that
# multiplies argument x with argument y and print the result.
f1 = lambda arg : arg + 15
a = int(input("enter any number = "))
print(a,'+ 15 =',f1(a))
f2 = lambda arg1,arg2 : arg1*arg2
b = int(input("enter any number = "))
print(a,'*',b,'=',f2(a,b))


# 2.Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number
f = lambda arg : arg*7
a = int(input("enter any number = "))
print(a,'*',7,'=',f(a))


# 3.Write a Python program to sort a list of tuples using Lambda.
xyz = [('English', 88),('Social sciences', 82),('Maths', 97),('Science', 90)]
print("given list",xyz,sep="\n")
list.sort(xyz,key=lambda x : x[1])
print("sorted list ",xyz,sep="\n")


# 4.Write a Python program to sort a given list of strings(numbers)
# numerically using lambda.
xyz = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
list.sort(xyz,key=lambda x : int(x))
print("sorted list ",xyz,sep="\n")


# 5.Write a Python program to find index position and value of the maximum and
#  minimum values in a given list of numbers using lambda.
xyz = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
print("(index, maximum) =",max(enumerate(xyz), key=(lambda x: x[1])))
print("(index, minimum) =",min(enumerate(xyz), key=(lambda x: x[1])))


# 6.Write a Python program to multiply all the numbers in a given list using lambda.
mul = lambda a, b : a * b
xyz = [4, 3, 2, 2, -1, 18] 
x = 1
for i in range(len(xyz)) :
    y = xyz[i]
    x = mul(x,y)
print(x)


# 7.Write a Python program to reverse strings in a given list of string values using lambda.
xyz = ['Red', 'Green', 'Blue', 'White', 'Black']
print(list(map(lambda x:"".join(reversed(x)),xyz)))


# 8.Write a Python program to triple all numbers of a given list of integers. Use Python map.
xyz = [4, 3, 2, 2, -1, 18]
print(list(map(lambda x: x*3,xyz)))


# 9.Write a Python program to listify the list of given strings individually using Python map.
xyz = ['Red', 'Green', 'Blue']
print(list(map(lambda x: list(x),xyz)))


# 10.write a Python program to create a list containing the power of said
# number in bases raised to the corresponding number in the index using Python map.
b = [5, 5, 5, 4, 7, 3]
p = [1, -2, 3, 0, 5, 6]
print('bases =',b)
print('powers =',p)
print(list(map(pow, b, p)))


# 11.Write a Python program to square the elements of a list using map() function.
xyz = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x : x*x, xyz)))


# 12.Write a Python program to compute the square of first N Fibonacci
# numbers, using map function and generate a list of the numbers.
n = int(input("enter required square terms of Fibonacci series: "))
xyz = []
a = 1
b = 1
for i in range(n):
    xyz.append(a)
    c=a+b
    a=b
    b=c
print(list(map(lambda x : x*x, xyz)))


# 13.Using filter() function filter the list so that only negative numbers are left.
xyz = [4, 3, 2, -2, -1, 18]
print(list(filter(lambda x: x<0, xyz)))


# 14.Using filter function, filter the even numbers so that only odd numbers
# are passed to the new list. Using filter() and list() functions and .lower()
# method filter all the vowels in a given string.
xyz = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda x: x%2!=0, xyz)))
m = input("enter any word : ")
vowels = ['a','e','i','o','u']
a = m.lower()
b = list(filter(lambda x: x not in vowels, a))
for i in b:
    print(i,end="")
# print(list(b))

# 15.Using map() and filter() functions add 2000 to the values below 8000.
xyz = [20,75,8732,49,7,9999]
a = filter(lambda x : x<8000,xyz)
b = map(lambda x : x+2000,list(a))
print(list(b))


# 16.This time swap the map() and filter() functions so that map() function is
# inside filter() function. Convert a number to positive if it's negative in the
# list. Only pass those that are converted from negative to positive to the new list.
xyz = [1, -2, 3, -4, 5, -6, 7, -8, 9]
b = filter(lambda x : x>0, map(lambda x : x*(-1), xyz))
print(list(b))


# 17.Using zip() function and list() function, create a merged list of tuples
# from the two lists given.
subject = ['English','Social sciences','Maths','Science']
marks = [88,82,97,90]
a = zip(subject,marks)
print(list(a))



