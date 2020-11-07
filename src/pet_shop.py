# Codeclan week 1 - Day 5 - Weekend Homework

# Return the value from the "name" key in the cc_pet_shop
def get_pet_shop_name(input_dict):
    return input_dict["name"]

# Returns the value from the "total_cash" key in the admin dict of cc_pet_shop
def get_total_cash(input_dict):
    return input_dict["admin"]["total_cash"]

# Function that adds or removes cash to the total cash in admin.
def add_or_remove_cash(input_dict, input_int):
    input_dict["admin"]["total_cash"] += input_int

# Returns the amount of pets sold in the admin dict of cc_pet_shop
def get_pets_sold(input_dict):
    return input_dict["admin"]["pets_sold"]

# Function that increases the amount of pets sold.
def increase_pets_sold(input_dict, input_int):
    current_value = get_pets_sold(input_dict)
    input_dict["admin"]["pets_sold"] = current_value + input_int

# Returns the number of pets in stock
def get_stock_count(input_dict):
    return len(input_dict["pets"])

# Return list of pets by breed.
def get_pets_by_breed(input_dict, input_breed):
    output_list = []
    for pet in input_dict["pets"]:
        if pet["breed"] == input_breed:
            output_list.append(pet["name"]) # might use other keys later. 
    return output_list

# Return dict of pets by name.
def find_pet_by_name(input_dict, input_name):
    output_dict = None #----originally declared as dict in case there was more than one with that name.
    for pet in input_dict["pets"]:
        if pet["name"] == input_name:
            output_dict = {} #---- would like to add each pet to dict here
            output_dict.update(pet)
    return output_dict

# Function that removes a pet by name.
def remove_pet_by_name(input_dict, input_name):
    for pet in input_dict["pets"]:
        if pet["name"] == input_name:
            input_dict["pets"].remove(pet)

# Function that adds a new pet with details to the pets dictionary.
def add_pet_to_stock(input_dict, new_pet):
    input_dict["pets"].append(new_pet)

# Returns the cash key value from customers list, given the indexed dictionary.
def get_customer_cash(input_dict):
    return input_dict["cash"]

# Function that removes an amount of cash from a customer.
def remove_customer_cash(input_dict, input_int):
    input_dict["cash"] -= input_int

# Returns how many pets the customer has.
def get_customer_pet_count(input_dict):
    return len(input_dict["pets"])

# Function that adds a pet to the customer.
def add_pet_to_customer(input_dict, input_new_pet_dict):
    input_dict["pets"].append(input_new_pet_dict)

# Funtions that determines if a customer can afford a given pet.
def customer_can_afford_pet(input_dict, input_pet):
    if input_dict["cash"] >= input_pet["price"]:
        return True
    else: 
        return False


# Function that combines the above to sell a customer a pet. 
def sell_pet_to_customer(input_dict, input_pet, input_customer):
    if input_pet != None:
        if customer_can_afford_pet(input_customer, input_pet) == True:
            remove_customer_cash(input_customer, input_pet["price"])
            add_or_remove_cash(input_dict, input_pet["price"])
            add_pet_to_customer(input_customer, input_pet)
            remove_pet_by_name(input_dict, input_pet)
            increase_pets_sold(input_dict, 1)
        

    



