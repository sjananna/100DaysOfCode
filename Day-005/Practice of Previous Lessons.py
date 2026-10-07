# Output to be in the same line

print("My name is Samia." , "I am 22 years old")

# Variable: A variable is a name for the memory location in a program.

name ="Samia"
age= 24
education = "PHD"

print("age")
print(age)
#Note: Here see the differences that when you give print function "age" it will give the output of age, but when you print (age) it will give the output of 24.

print("My name is :", name)
print("My age is:", age)
print("My education is :", education)

#Note: never put variable inside the "" in the print function.

age = 24
old = False
picture= None

print(type(age), type(old), type(picture))
#Note: for each variable to know their type in one line, we have to make sure we are adding type functions before each variable to understand their value type.

a= 23
b= 27
sum= a+b
print(sum)
#Note: here we have created two variables 'a' and 'b' and then put value to it. Then we have added the value of 'a' and 'b' to the another variable called 'sum'. To print the variables value as an output we added the print function and then got the summed values on the terminal.

#Expression Execution
#(Number and String)
a,b = 2,3
txt = "@"
print(a*txt*b)

#(String and String)
a,b= "2",3
Str = "@"
print((a+Str)*b)
#or,
a,b = 2,3
Str = "@"
print((str(a)+Str)*b)
#Note: whenever you are working with number and the string you use * and you do not need to recognize any str or integer differently. But when you are working with string and the string while using '+' you have to remember one thing that if you do not put "" in the variable to make it string and then you directly without explaing it that it is string and try to add with + with another string it won't be working out as python is an implicit language and it still required to know which one is number and which one is string.

# Arithmatic expression with integer and float will always result in float
a,b = 2, 0.5
c= a/b
print(c)
#output= 4.0

#Division operator with two integers will always give float
a,b = 2,10
c=b/a
print(c)
#output: 5.0

#Integer division with float and int will always give int display as float value
a,b= 1.5, 3
c=a//b
print(c)
#output: When using floor division //, Python divides the numbers and rounds the result down to the nearest integer value. If either number is a float, the result will also be a float.

a,b= 5, 12
c=b//a
print(c)
#Output: 2

#input function
#(string input)
name=input("name: ")
print(name)

#(int input)
age = int(input("age: "))
print(age)

#(float input)
price = float(input("price: "))
print(price)

print("My name is", name, "and I am", age, "years old. The price of the potatoes are", price,"cad.")






