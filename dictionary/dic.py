# dic
# student = {
#     "name": "Ekbal",
#     "age": 24, 
#     "city": "Shadulla Bari",
#     "cgpa": 8.50
# }

# student["city"] = "Dhubri"
# print(student)

# print(student.keys())
# print(student.values())

# nested dic
My_detais = {
    "name": "Ekbal",
    "age": 24,
    "city": {
        "house no" : "129k", 
        "street" : "Shadulla Bari Bazar",
        "post office" : "Kalapani",
        "police station" : "Mankachar",
        "district" : "South Salmara Mankachar",
        "state" : "Assam",
        "country" : "India"
    },
    "cgpa": 8.50,
    "subjects": {
        "C" : 80,
        "Python" : 90,
        "Java" : 85,
        "DSA" : 88
    }
}


# print(My_detais["city"]["street"])
# print(My_detais["subjects"]["Python"])

# items
# print(My_detais.items())

# get
# print(My_detais.get("name"))
# print(My_detais.get("hobby"))  # None because hobby key is not present in the dictionary

# update
# My_detais.update({"age": 25})
# print(My_detais)


print(My_detais)