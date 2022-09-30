"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 Spring 2021
__updated__ = "2021-05-17"
-------------------------------------------------------
"""
from Food import Food



def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """
    name = input("Enter name of food: ")
    print("Origin")
    print("""0 Canadian
1 Chinese
2 Indian
3 Ethiopian
4 Mexican
5 Greek
6 Japanese
7 Italian
8 American
9 Scottish
10 New Zealand
11 English""")
    origin = int(input(":"))
    vegetarian = input("Is the food vegetarian(Y/N): ")
    calories = int(input("Enter calories: "))
    
    
    if vegetarian == "Y":
        is_vegetarian = True
    else:
        is_vegetarian = False
        
    food = Food(name,origin,is_vegetarian,calories)
    

    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    line.strip()
    line = line.split("|")
    
    name = line[0]
    origin = int(line[1])
    is_vegetarian = eval(line[2])
    calories = int(line[3])
    
    food = Food(name,origin,is_vegetarian,calories)
    

    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    read = file_variable.readlines()
    foods = []

    
    for line in read:
        set_food = line.strip().split("|")
        food = Food(str(set_food[0]),int(set_food[1]),eval(set_food[2]),int(set_food[3]))
        foods.append(food)
        
        
    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    for food in foods:
        file_variable.write(str(food.name))
        file_variable.write("|")
        file_variable.write(str(food.origin))
        file_variable.write("|")
        file_variable.write(str(food.is_vegetarian))
        file_variable.write("|")
        file_variable.write(str(food.calories))
        file_variable.write("\n")
            

    


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    foods is unchanged.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    veggies = []

    for food in foods:
        if food.is_vegetarian == True:
            veggies.append(food)

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    foods is unchanged.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    origins = []
    
    for food in foods:
        if food.origin == origin:
            origins.append(food)
    

    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    total = 0
    num = 0

    for food in foods:
        total = total + food.calories
        num = num + 1
        
    avg = total/num

    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    
    origins = []
    total = 0
    num = 0
    
    for food in foods:
        if food.origin == origin:
            origins.append(food)
            
            
    for origin in origins:
        total = total + origin.calories
        num = num + 1
    
    avg = total/num
    
    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    print("Food                                Origin       Vegetarian Calories")
    print("----------------------------------- ------------ ---------- --------")

    for food in foods:
        
        print(f"{food.name:<36}{Food.ORIGIN[food.origin]:<18}{str(food.is_vegetarian):<9}{food.calories:>5}")

    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    result = []
    
    if is_veg == False:
        for food in foods:
            if food.origin == origin and food.calories <= max_cals:
                result.append(food)
            
    else:
        for food in foods:
            if food.origin == origin and food.calories <= max_cals and food.is_vegetarian == is_veg:
                result.append(food)
                
                
                
                
    return result
    return result
