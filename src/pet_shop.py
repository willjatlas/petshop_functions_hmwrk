# Codeclan week 1 - Day 5 - Weekend Homework

# Return the value from the "name" key in the cc_pet_shop
def get_pet_shop_name(input_dict):
    return input_dict["name"]

# Returns the value from the "total_cash" key in the admin dict of cc_pet_shop
def get_total_cash(input_dict):
    return input_dict["admin"]["total_cash"]

# Function that adds or removes cash to the total cash in admin.
def add_or_remove_cash(input_dict, input_int):

    current_value = get_total_cash(input_dict)
    new_value = 0

    if input_int >= 0:
         new_value = current_value + input_int
    else:
         new_value = current_value - abs(input_int) # Make input_int an absolute number.
    
    input_dict["admin"]["total_cash"] = new_value 

# Returns the amount of pets sold in the admin dict of cc_pet_shop
def get_pets_sold(input_dict):
    return input_dict["admin"]["pets_sold"]















    

