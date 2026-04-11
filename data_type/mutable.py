# Mutable data types are those that can be changed after they have been created. In Python, lists, dictionaries, and sets are examples of mutable data types.

# List

Chikni = [1, "A", 1.5, True, None]

Chikni.append("Madam")

print(type(Chikni))
print(Chikni)

Chikni[1] = "Chikni"
print(Chikni)

Chikni.remove("Chikni")
print(Chikni)




# Dictionary

Madam = {"name": "Jesmin", "age": 25, "city": "Dhaka"}

print(type(Madam))
print(Madam)


Madam["city"] = "Guwahati"
print(Madam["city"] == "Guwahati")


Madam.pop("age")
print(Madam)


# Set

number = {1, 2, 3, 4, 5}

print(type(number))

number.add(6)
print(number)
