"""
Seção 6 - Exercícios
"""
"""1:"""
x = 150
if x > 100:
    print("Congratulations!")

"""2:"""
number = int(input("Enter a number: "))
if number > 0:
    a = number
    print("Valor positivo.")
    print(a)
else:
    b = number
    print("Valor negativo.")
    print(b)

"""3:"""
p = 0
i = 0
number = int(input("Enter a number: "))
if (number / 2 == 0):
    p = number
else:
    i = number

print(p)
print(i)

"""4:"""
height = int(input("Enter a number: "))
gender = input("Enter your gender: ")
if gender == "Man":
    For_men = int(input(72.7 * height - 58))
    print(For_men)
else:
    For_women = int(input(62.1 * height - 44.7))
    print(For_women)

"""5:"""
e = 0
m = 0
Weight = int(input("Enter a number: "))
if Weight > 50:
    e = Weight - 50
    m = e * 4
    print("Weight: " + str(Weight))
    print("Excess: " + str(e))
    print("Fine: " + str(m))
else:
    
    print(e)
    print(m)

"""6:"""
e = 0
c = int(input("Enter a number: "))
n = int(input("Enter a number: "))
if n > 50:
    e = n - 50
    n = n - e
    Salary = n * 10
    Excess = e * 20
    print("Salary is " + str(Salary))
    print("Extra is " + str(Excess))
else:
    
    print(c)
    print(n)
    print(e)

"""7:"""
Number1 = int(input("Enter a number: "))
Number2 = int(input("Enter a number: "))
Number3 = int(input("Enter a number: "))
Number4 = int(input("Enter a number: "))

num1 = Number1 ** 2
num2 = Number2 ** 2
num3 = Number3 ** 2
num4 = Number4 ** 2
if num3 >= 1000:
    print(num3)
else:
    print("The first number is: " + str(Number1) + " and your squared is: " + str(num1))
    print("The second number is: " + str(Number2) + " and your squared is: " + str(num2))
    print("The third number is: " + str(Number3) + " and your squared is: " + str(num3))
    print("The forth number is: " + str(Number4) + " and your squared is: " + str(num4))

"""8:"""
Number = int(input("Enter a number: "))
if (Number % 2 == 0):
    print("Even number.")
else:
    print("Odd number.")
if (Number > 0):
    print("Positive number.")
else:
    print("Negative number.")

"""9:"""
Pollution_level = float(input("Enter a number: "))
if (Pollution_level >= 0.3) and (Pollution_level < 0.4):
    print("Company 1 must suspend its activities!")
if (Pollution_level >= 0.4) and (Pollution_level < 0.5):
    print("Company 1 and 2 must suspend its activities!")
if (Pollution_level >= 0.5):
    print("All companies must suspend its activities!")
else:
    print("Acceptable levels!")

"""10:"""
Age = int(input("Enter your age: "))
if (Age >= 5) and (Age < 7):
    print("Infantil-a")
elif (Age >= 8) and (Age < 11):
    print("Infantil-b")
elif (Age >= 12) and (Age < 13):
    print("Juvenil-a")
elif (Age >= 14) and (Age < 17):
    print("Juvenil-b")
else:
    print("Adults")           






               


    







