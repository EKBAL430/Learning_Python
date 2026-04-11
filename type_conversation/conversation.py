a = 10  # integer
b = 52.5    # float
c = "Hello, World!" # string
d = True    # boolean

# e = a + b

# f = str(a) + " How are you?"
# print(f)

# g = not d
# print(g)

# h = c + " " + str(a) + " " + str(b) + " " + str(d)
# print(h)



# # j = b + c         # This will raise a TypeError because you cannot add a float and a string


# print(type(e))  # <class 'float'>
# print(type(f))  # <class 'str'>
# print(type(g))  # <class 'str'>
# print(type(h))  # <class 'str'>


# convert to dictonary from variables
# dictonary = dict(a=10, b=52.5, c="Hello, World!", d=True)
# print(dictonary)


hexadecimal = hex(a)
print(hexadecimal)  

octal = oct(a)
print(octal)


# convert from variables

x = 5, 9, 2, 8, 1, 4, 7, 6, 3

integer = int(x[0])
print(f'integer: {integer}')

set = set(x)
print(f'set: {set}')

tuple = tuple(x)
print(f'tuple: {tuple}')

list = list([x])
print(f'list: {list}')

ordered_dict = dict(enumerate(x))
print(f'ordered_key_dict: {ordered_dict}')

dictonary = dict(y = x)
print(f'dictonary: {dictonary}')

string = str(x)
print(f'string: {string}')

order = sorted(x)
print(f'order: {order}')