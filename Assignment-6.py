# Assignment_6
# python

# Create a following function in python.
# # 1.Find square root of a given integer.
# def root(x):
#     return x**0.5
# print("root of given numer is",root(int(input("enter a numer: "))))

# # 2.Find simple interest and compound interest
# x = float(input("enter principle amount P$:"))
# y = float(input("enter interest rate R%:"))
# z = float(input("enter number of year N:"))
# def SI(p,r,n):
#     return (p*r*n)/100
# def CI(p,r,n):
#     a = p*(1+r/100)**n-p
#     return a
# print("simple interest is",SI(x,y,z))
# print("compound interest is",CI(x,y,z))

# # 3.For is even, is odd, is prime and factorial of a given integer  
# n = int(input("enter any number: "))
# def OE(x):
#     a = 0
#     if x%2==0 :
#         a = 1
#     return a
# def fact(x):
#     c = 1
#     for i in range(1,x+1):
#         c*=i
#     return c
# def prime(x):
#     a = 0
#     b = int(x/2)
#     for i in range(2,b+1):
#         if x%i==0:
#             a = 1
#             break
#     return a
# if OE(n)==0 :
#     print("given number is odd")
# else :
#     print("given number is even")
# if prime(n)==0:
#     print("given number is prime")
# else :
#     print("ginen number is not prime")
# print(n,"!=",fact(n),sep="")

# # 4.Find factorial of given integer
# n = int(input("enter any number: "))
# def fact(x):
#     c = 1
#     for i in range(1,x+1):
#         c*=i
#     return c
# print(n,"!=",fact(n),sep="")

# # 5.Find area and circumference of circle.
# import math
# x = float(input("enter radius of the circle: "))
# def area(r):
#     return math.pi*r**2
# def cir(r):
#     return 2*math.pi*r
# print("area of the circle is",area(x))
# print("circumference of the circle is",cir(x))

# 6.Find area of sphere
# import math
# x = float(input("enter radius of the circle: "))
# def area(r):
#     return 4*math.pi*r**2
# print("area of the sphere is",area(x))

# import math
# import numpy as np
# from pylab import *
# x=np.arange(0, math.pi*2, 0.05)
# plot(x, sin(x)) 
# plot(x, cos(x), 'r|') 
# plot(x, -sin(x), 'y*') 
# show()
