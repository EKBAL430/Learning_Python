student = ["David", 23, "Male", "Computer Science", 7.3]

# value at index 0 and 1
print(f"Index 0: {student[0]}") 
print(f"Index 1: {student[1]}")

# updating the value at index 1
student[1] = 24
print(f"Index 1 (updated): {student[1]}")

# using for loop to check all indexes and values in the list
for i, value in enumerate(student):
    print(f"Index {i}: {value}")

#slicing
print(f"Index 1-3: {student[1:3]}")
print(f"Last index (-1): {student[-1]}")

# length of the list
length = len(student)
print(f"Length of the list: {length}")