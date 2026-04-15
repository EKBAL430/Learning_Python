name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"I am {name}! and I am {age} years old.")

# normally input is string
print(type(name))
print(type(age))

# if we want to convert age to int
Int_age = int(age)
print(Int_age)

print(type(Int_age))