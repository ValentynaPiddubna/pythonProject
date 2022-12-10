# x = 0
# if x > 0:
#   print('This is true')
# else:
#   print('x is not greater then 0')


# age = 42

# if age < 18:
#    print('You are not allowed to see this')#
# elif age > 100:
#    print('Wow')
# elif age >= 68:
#    print('You are too old. Get rest')
# elif age == 42:
#    print('You know the answer')
# else:
#    print('You are 18 to 59 years')

# var = 1

# print(bool(var))

# if var:
#     print('var is here')
# else:
# print('There is no var')

print('Code before input')
age = input('Enter your age:')

if age.isdigit():
    age = int(age)
    print(type(age))
print(f' The age is {age}')
print('Code after input')
