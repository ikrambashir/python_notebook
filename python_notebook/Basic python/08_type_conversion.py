x = 10          #integer
y = 10.2        #float
z = "hello"     #string

#implicit type conversion
x=x/y
print(x, "Type of x is:", type(x))

#explicit type conversion
age=input("what is your age? ")
age=int(age)
print(age, type(int(age)))
print(age, type(float(age)))

#name
b