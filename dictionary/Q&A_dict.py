# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start withan empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

for i in range(3):
    subject = input("Enter subject name: ")
    mark = int(input("Enter marks: "))
    marks[subject] = mark
    
print(marks)
    
    


# Store following word meanings in a python dictionary :

# table : "a piece of furniture", "list of facts & figures"

# cat : "a small animal"