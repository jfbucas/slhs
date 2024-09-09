# Boolean
# True or False?

print(10 > 9)
print(10 == 9)
print(10 < 9)

exit() # Remove this line to continue



# When you run a condition in an if statement, Python returns True or False:
# Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

exit() # Remove this line to continue



# The bool() function allows you to evaluate any value, and give you True or False in return,

# Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

# Evaluate two variables:
x = "Hello"
y = 15
z = 0

print(bool(x))
print(bool(y))
print(bool(z))

exit() # Remove this line to continue


# NOT

aaaa = 65
bbbb = 29

if not bbbb > aaaa:
  print("bbbb is not greater than aaaa")
else:
  print("bbbb is greater than aaaa")
