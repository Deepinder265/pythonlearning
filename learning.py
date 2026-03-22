a = 20  # integer
print("The number is:", a)

b = 109.12  # float
print("The float number is:", b)

name = "Parminder Singh" # string variable
print(name)

list_var = [10,20,30,40,50,90,19,21,45,67,37] #list is mutable
list_var[1] = 702
print(list_var[1])


tuple_var = (10,20,30,40,50,90,19,21,45,67) # tuple is immutable
#tuple_var[2] = 43 # this is not possible
print(tuple_var[2])

range_var = range(100)
print(range_var[3])



#"parminder", "deepinder", "inder"
#10.1,19.2,

def display_name(firstname, lastname = ''):
    print("My name is ", firstname, lastname)

#display_name("Deepinder", "Singh")
#display_name("Parminder", "Singh")
display_name("Deepinder Singh")


def addition(num1, num2):
    return num1 + num2

def display(value):
    print(value)


a = 10
b = 20
c = addition(a, b)
display(c)
