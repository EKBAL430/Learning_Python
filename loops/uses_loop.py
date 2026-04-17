# while loop

# i = 1
# while i < 8:
#     print("Hello !")
#     i += 3
    

# ******************************************************************  
# print number from 100 to 1

# i = 100  
# while i > 0:
#     print(i)
#     i -= 1


# *******************************************************************
# Print the multiplication table of a number n

# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(f"{n}x{i} = {n*i}")
#     i += 1

# *******************************************************************
# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# i = 0
# print("Length of the list:", len(list))

# while i < len(list):
#     print("Element at index", i, ":", list[i])
#     i += 1
#     print("i =", i)
    
    
# i = 1
# while i <= 20:
#     print(i)
#     i += 2

# *******************************************************************
# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# search = int(input("Enter a number to search: "))
# numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# while True:
#     if search in numbers:
#         print(f"{search} is found in the tuple.")
#         break
#     else:
#         print(f"{search} is not found in the tuple.")
#         break


# for num in numbers:
#     if num == search:
#         print(f"{search} is found in the tuple.")
#         break
# else:
#     print(f"{search} is not found in the tuple.")


# ******************************************************************
# user = int(input("Enter a number: "))
# for i in range(11):
#     # i = i * user
#     # print (f"{user} x {i//user} = {i}")
#     print (f"{user} x {i} = {user*i}")


# *****************************************************************
# pass statement

for i in range(5):
    pass # it is used when we want to write a loop but we don't want to do anything in the loop