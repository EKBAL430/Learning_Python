# method

tuple = (1, 2, 0, 4, 5, 3, 3, 6, 3, 7, 6, 8, 7, 9,)

# count() method returns the number of times a specified value appears in the tuple
print(tuple.count(6)) 


# index() method searches the tuple for a specified value and returns the position of where it was found    
print(tuple.index(3))


# len() method returns the number of items in the tuple
print(len(tuple))

# max() method returns the largest item in the tuple
print(max(tuple))


# min() method returns the smallest item in the tuple
print(min(tuple))


# sorted() method returns a sorted list of the specified iterable's items in ascending order
print(sorted(tuple))


# reversed() method returns a reversed iterator of the specified sequence
print(reversed(tuple)) 

print(list(reversed(tuple))) # to convert the reversed iterator to a list
 
print(tuple[::-2])# slicing method to reverse the tuple


# sum() method returns the sum of all items in the tuple
print(sum(tuple))

# any() method returns True if any item in the tuple is true, otherwise it returns False. If the tuple is empty, it returns False.
print(any(tuple)) # because there is at least one item in the tuple that is true (non-zero)

# all() method returns True if all items in the tuple are true, otherwise it returns False. If the tuple is empty, it returns True.
print(all(tuple)) # because there is at least one item in the tuple that is false (zero)