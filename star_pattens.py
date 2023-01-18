

# n = 11
# #1
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("\n")
# #2
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print("\n")
# # 3
# k=int(n/2)
# for i in range(n):
#     if i>k :
#         for j in range(i,n):
#             print("*",end=" ")
#         print("\n")
#     else :
#         for j in range(i):
#             print("*",end=" ")
#         print("\n")
# k=int(n/2)
# for i in range(n):
#     for j in range(n):
#         print(end= " ")
#     n-=1
#     for j in range(i+1):
#         if i>4:

#         print("*",end=" ")

#     print("\n")
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print("\n")
# k=int(n/2)
# for i in range(k):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("\n")
# for i in range(k-1,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print("\n")

# n = 10
# k=int(n/2)
# for i in range(n):
#     if i>k :
#         for j in range(i,n):
#             print("*",end=" ")
#         print("\n")
#     else :
#         for j in range(i):
#             print("*",end=" ")
#         print("\n")
# a=0
# for i in range(7):
#     if i==0 :
        
#     elif i==4 :
#         for j in range(7):
#             print("M",end="")
#         print("\n")
#     elif i in range(1,4):
#         for j in range(i,3):
#             print(end=" ")
#         print("M",end="")
#         a+=1
#         for k in range((2*a)-1):
#             print(end=" ")
#         print("M",end="")
#         print("\n")
#     else :
#         print("M",end="")
#         for j in range(5):
#             print(end=" ")
#         print("M",end="")
#         print("\n")

# n = 0
# b = 0
# while n<20:
#     n=n+1
#     b=b+n
#     print(n,b)
# a = 0
# while a<99:
#     a+=1
#     print(a)
# b = 48
# while b>0:
#     print(b)
#     b-=2
# while b>0:
#     print(b,end='@')
#     b-=3
# print('4644',"5452",sep='@')

# a = 22
# while a<40:
#     print(a,end=' @ ')
#     a+=2   

# matrix=[[1,2,3],[3,4,5],[5,6,7]]
# for i in range(3):
#     for j in range(3):
#         print(matrix[i][j],end=" ")
#     print()

# a = int(input("enter a number: "))
# b = 0
# c = 1
# for i in range(a):
#     b+=1
#     c*=b
# print("factorial of given number is ",a,"!"," = ",c,sep="")

##prime No. Between m and n
# m = int(input("enter number 1."))
# n = int(input("enter number 2."))
# if m<n:
#     c=m
#     m=n 
#     n=c
# for i in range(1,m):
#     p=0
#     a=int(i/2)
#     for j in range(2,a+1):
#         if i%j==0:
#             p=1
#     if p==0 and i>n:
#         print(i,end=",")

# m = int(input("enter year 1."))
# n = int(input("enter year 2."))
# if m<n:
#     c=m
#     m=n 
#     n=c
# for i in range(n,m):
#     if ((i%4==0 and i%100!=0) or i%400==0):
#         print(i,end=",")

print(5,",",4)