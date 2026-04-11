# a = 15
# b = 10
# c = 5



# and operator

# if a > b and b > c:
#     print("Both conditions are true")
# else:
#     print("At least one condition is false")
    



# or operator

# if a < b or a < c:
#     print("Condition is true")
# elif a > b or c < a:
#     print("At least one condition is true")
# else:
#     print("Both conditions are false")



# not operator

# if not c <= b:
#     print("c is not less than or equal to b")
# elif not a > c:
#     print("a is not greater than c")
# elif not a < b:
#     print("a is not less than b")  # this condition is true, so it will print this statement and skip the rest
# elif not a == b:
#     print("a is not equal to b")
# else:
#     print("Both conditions are true")




Age = 25
is_premium_member = True
original_price = 900


# discount_percentage

def calculate_discount(discount_percentage):
    discount = original_price * (discount_percentage / 100)
    final_price = original_price - discount
    return final_price

# if the person is eligile or not for the discount
# applyinf the discount of 2%

if Age > 18 and original_price >= 1000 and is_premium_member:
    Price = calculate_discount(2)       
    print(f"Original Price : {original_price} \nPrice after 2% discount: {Price}")   
        
    # Getting the extra 20% discount
    
    if original_price >= 10000:           
        discount2 = calculate_discount(20)
        extra_discount2 = (discount2 + Price) - original_price 
        print(f"Total 22% Discount: {extra_discount2}")  
    else:      
        # Getting the extra 10% discount
        
        if original_price >= 5000:           
            discount1 = calculate_discount(10)
            extra_discount1 = (discount1 + Price) - original_price 
            print(f"Total 12% Discount: {extra_discount1}")
        
else:
    print("You are not eligible for the discount.")
