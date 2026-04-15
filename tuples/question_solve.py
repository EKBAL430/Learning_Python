# **************************Question: 1**********************************

# ask the user to enter names of their 3 favorite movies & store them in a list
# movie_names = input("Enter the names of your 3 favorite movies, separated by commas: ").split(",") # split the input string into a list of movie names using comma as the separator

# user1 = [name.strip() for name in movie_names] # strip() method is used to remove any leading or trailing whitespace from each movie name in the list
# print(user1)

# user2 = list(map(str.strip, movie_names)) # using map() function to apply the strip() method to each movie name in the list
# print(user2)

# user3 = tuple(movie_names) # convert the list of movie names to a tuple and print it
# print(user3)

# print(type(user1)) # check the type of user1
# print(type(user2)) # check the type of user2
# print(type(user3)) # check the type of user3





# **************************Question: 2**********************************

# check if a list contains a palindrome of elements. (Hint: use copy( ) method)    ////// [1, 2, 3, 2, 1] [1,“abc”,“abc”, 1]

list1 = [1, 2, 3, 2, 1] 
list2 = [1,"abc","abc", 1]

# copy and reverse list1
copy_Of_List1 = list1.copy() 
copy_Of_List1.reverse() 

#  palindron means that the list is the same as its reverse, so we check if list1 is equal to reverse_copy_list1
print(list1 == copy_Of_List1) 



# copy and reverse list2
copy_Of_List2 = list2.copy()
copy_Of_List2.reverse()

# list2 is not a palindrome because it is not the same as its reverse (reverse_copy_list2)
print(list2 == copy_Of_List1) 





# *******************************Question: 3*************************
# [”C”,“D”,“A”,“A”,“B”,“B”,“A”]    ///// the above values in a list & sort them from “A” to “D”.

list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort() # sort the list in place (modifies the original list)
print(list) # print the sorted list