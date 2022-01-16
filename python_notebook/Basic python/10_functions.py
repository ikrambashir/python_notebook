print("i am pytho")
print("i am python")
print("i am python")

# #defining a functions
# from typing import Text


def print_batata():
    print("i am pytho")
    print("i am python")
    print("i am python")

print_batata()

#2
def print_batata():
    text="i am python"
    print(text)
    print(text)
    print(text)
print_batata()

#3
def print_batata(text):
    print(text)
    print(text)
    print(text)
print_batata("I am ikram learning python")

#defining a function with if, elif and else statment
def school_calculator(age, text):
    if age==5:
        print("eshal can join the school")
    elif age>5:
        print("eshal should got to higher school")
    else:
        print("eshal is still a baby")

school_calculator(3.5, "eshal")

# defining a function of future

def future_age(age):
    new_age=age+20
    return new_age
    print(new_age)

future_predicted_age=future_age(31)
print(future_predicted_age)