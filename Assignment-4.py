# Assignment-4
# Python:

# 1) Write a Python code to check whether an inputted number is even or odd using an if-else statement.
n = int(input("Enter a number: "))
if n%2==0 :
    print("given number is even")
else :
    print("given number is odd")

# 2) Write a Python code to convert a length in cm to an inch. If inputted length is negative, then print “Entry is invalid”.
n = float(input("Enter a length in centimeter: "))
if n>0 :
    a = n/(2.54)
    print("langth is",a,"inch")
else :
    print("Entry is invalid")

# 3) Write a Python code to check whether the inputted number is positive, negative or zero using if - elif - else statement.
n = float(input("Enter a number: "))
if n>0 :
    print("given number is positive")
elif n<0 :
    print("given number is nagative")
else :
    print("given number is zero")

# 4) Write a Python code to print the statements for runs scored by batsmen using the following table. Take runs as user input
n = int(input("Enter a Batsman runs: "))
if n>=100 :
    print("Batsman scored a Century")
elif n in range(50,100) :
    print("Batsman scored a Half Century")
elif n<50 :
    print("Batsman has scored neither Century nor fifty")

# 5) Write a Python code to calculate the percentage of marks of 5 subjects entered by the user and print the grade of a student by his/her percentage:
m1 = int(input("Enter a student obtained marks in particular subject out of 100 \nMathematics: "))
m2 = int(input("Physics: "))
m3 = int(input("Chemistry: "))
m4 = int(input("Gujarati: "))
m5 = int(input("English: "))
total = m1+m2+m3+m4+m5
p = (total*100)/500
q = int(p)
if q in range(90,101) :
    a = "A+"
elif q in range(70,90) :
    a = "A"
elif q in range(60,70) :
    a = "B+"
elif q in range(50,60) :
    a = "B"
elif q in range(40,50) :
    a = "C"
elif q in range(33,40) :
    a = "D"
else :
    a = "F"
print("Student have a",p,"%")
print("Student have a",a,"Grade")

# 6) Write a Python code to input the Name, Gender, and Age of the candidate and print the statements according to the following table.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
g = input("Enter your gender M or F: ")
if g in ['M','m'] :
    if age>=21:
        print("Mr.",name,", you are eligible to marry.\nCongratulation!!!!")
    else :
        print("Mr.",name,", you are not eligible to marry.\nWait for",21-age,"years")
elif g in ['f','F'] :
    if age>=18:
        print("Ms.",name,", you are eligible to marry.\nCongratulation!!!!")
    else :
        print("Ms.",name,", you are not eligible to marry.\nWait for",18-age,"years")
else :
    print("invalid Gender")

