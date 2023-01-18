# Assignment_5
# python

#1. Write python program to construct following patterns.
print("pattern 1.")
for i in range(1,6):
    print(i*"* ")
    # print()
print("pattern 2.")
for i in range(5,0,-1):
    print(i*"* ")
    # print()
print("pattern 3.")
for i in range(1,12):
    if i<7:
        print(i*"* ")
        # print()
    else :
        a = 12 - i
        print(a*"* ")
        # print()


# 2. Write a python program to print any alphabet.
for i in range(1,6):
    print("@",end="")
    for j in range(1,10):
        if i==j:
            print("@",end="")
        elif (i+(j-4))==6: 
            print("@",end="")
        else :
            print(" ",end="")
    print("@",end="")
    print()
 

# 3. Write a python program that accepts a word from the user and reverse it.
W = input("enter any word:")
n = len(W)
for i in range(n-1,-1,-1):
    print(W[i],end="")

# 4. Write a python program that accepts a number from the user and reverse it.
n = int(input("enter any big digit number:"))
a = str(n)
b = len(a)
for i in range(1,b+1):
    c = n%10
    print(c,end="")
    d = n/10
    n = int(d)

# 5. Write a python program to check inputted number is prime or not.
n = int(input("enter any number:"))
m = n/2
p = int(m)
f = 0
for i in range(2,p):
    if n%i==0:
        f = 1
        break
if f==0:
    print(n,"is prime")
else :
    print(n,"is not prime")

# 6. Write a python program t0 check inputted number is perfect or not.
n = int(input("enter any number:"))
m = n/2
p = int(m)
sum = 0
for i in range(1,p+1):
    if n%i==0:
        sum+=i
if sum==n:
    print(n,"is perfect number")
else:
    print(n,"is not perfect number")
# Example. 6, 28, 496, 8128, and 33550336 are perfect numbers


# 7. Write a python program to create multiplication table of any number.
n = int(input("enter any number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

# 8. Write a python program to find sum and average of inputted numbers.
n = input("Enter elements (Space-Separated):")
m = n.split()
a = list(map(int,m))
b = sum(a)
c = len(m)
d = b/c
print(b,"is sum of given number")
print(d,"is average of given number")

# 9. Write a python program to find factorial of inputted number.
n = int(input("enter any number:"))
a = 1
for i in range(1,n+1):
    a*=i
print(n,"!=",a,sep="")

# 10. Write a python program to find series of an exponential function.
n = int(input("enter a required terms for accurate value:"))
x = float(input("enter a value of x:"))
sum = 0
nume = 1
deno = 1
for i in range(n):
    if i==0:
        sum+=1
    else :
        deno*=i
        nume*=x
        sum+=(nume/deno)
print("value of e^x is",sum)




