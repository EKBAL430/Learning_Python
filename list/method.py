list = [1, 5, 3, 2, 5, 6, 7, 8]
print("Original list:", list)

#append
list.append(9)
print("Appended 9:", list)

#sort
list.sort()
print("Sorted :", list)

#reverse
list.reverse()
print("Reversed :", list)

#sort(reverse=True)
list.sort(reverse=True)
print("Sorted (reverse):", list)


#insert
list.insert(1, 20)
print("insert (index 1,value 20):", list)

#remove
list.remove(1)
print("Removed 1:", list)

#pop
list.pop()
print("Popped :", list)

#count
list_count = list.count(5)
print("Count of 5 :", list_count)

#index
list_index = list.index(3)
print("Index of 3 :", list_index)

reversed_list = list[2::-1]
print("Reversed list using slicing:", reversed_list)

sorted_list = sorted(list)
print("Sorted list using sorted():", sorted_list)