import sys
print(sys.version)
# Learn about how to Print and comment
print("Hello world!")

# Learn about variables and types
x = 5
print(x)
print(type(x))
y = 12.5
print(y)
print(type(y))

print(x+y)
print(type(x+y))

z = "Sakin"
print(z)
print(type(z))   
a, b, c = "Orange", "Banana", "Mango"
print(a,b,c)

fruits = ["apple", "Mango", "Lichi"]
x,y,z = fruits
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))
#or
print(fruits)
print(type(fruits))

b = True
print(b)
print(type(b))

c = complex(8,2)
print(c)
print(type(c))

#Learn about Typecast

string = "15"
number = 7
string_number = int(string)
print(type(string_number))

sum=number+string_number
print(sum)