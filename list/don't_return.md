# Python List Methods (Important Notes)


Some list methods **modify the original list** and **do NOT return anything (return None)**.

---
### Example:

🧠 Real-life example (important)

You have a notebook.

You write a new line in it.

Now question:

Did you get a new notebook?
❌ No

The same notebook changed.

---
## 🔥 Methods That DO NOT Return Value

Modify the original list
Return None -
List :

append() ;

sort() ;

reverse() ;

extend() ;

insert() 

---
## 🧠 Memory Trick

👉 If function changes original object → returns None

👉 If function creates new object → returns value

---
### ❌ Wrong 
```
🔍 What actually happens

list = [1, 5, 3, 2, 5, 6, 7, 8]
list_append = list.append(9)
list becomes: [1,5,3,2,5,6,7,8,9]
list_append = None

So:

print(list_append)

👉 prints None
```

---
### ✅ Correct way
```
If you want to print updated list:

my_list = [1, 5, 3, 2, 5, 6, 7, 8]
my_list.append(9)

print(my_list)
```