# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students?
# "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"

subjects = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]

classrooms_needed = len(set(subjects))
print(classrooms_needed)



# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)


value = {9, "9.0"}
print(value)