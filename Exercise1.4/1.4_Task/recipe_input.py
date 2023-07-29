import pickle

def calc_difficulty(recipe):
    difficulty = ""
    if(recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4):
        difficulty = "Easy"
    elif (recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4):
        difficulty = "Medium"
    elif (recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4):
        difficulty = "Intermediate"
    elif (recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4):
        difficulty = "Hard"
    return difficulty


def take_recipe(n):
    name = input(f'What will the name of recipe {n + 1} be? ')
    cooking_time = 0
    while cooking_time == 0:
        try:
            cooking_time = int(input("How long will it take to cook? (minutes) "))
        except ValueError:
            print ("cook time must be a number!")
    ingredients = []
    finished = False
    while not finished:
        try:
            ingredient = input(f"Input an ingredient required in {name}:  ")
            ingredients.append(ingredient)
            response = input("Do you have more ingredients (y or n):  ")
            if (response == "n"):
                finished = True
        except ValueError:
            print('ingredient can only contain letters')
    recipe = {
        "name" : name,
        "cooking_time" : cooking_time,
        "ingredients" : ingredients
    }
    difficulty = calc_difficulty(recipe)
    recipe['Difficulty'] = difficulty
    return recipe



# prompt the user for a filename to be opened and read. 
# handle issues with file unknown or general input issues by creating new dict
try:
    filename = input("enter the name of a file to be opened (without extension) ")
    filename += '.bin'
    file = open(filename, 'rb')
    data = pickle.load(file)
except FileNotFoundError:
    data = {
        "recipes_list" : [],
        "all_ingredients" : []
    }
except :
     data = {
        "recipes_list" : [],
        "all_ingredients" : []
    }
else :
    file.close()
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]


n = 0
while n == 0:
    try:
        n = int(input("How many recipes will you be entering today? "))
    except ValueError:
        print('the value must be a number')

for i in range(n):
    recipe = take_recipe(i)
    for ingredient in recipe["ingredients"]:
        if (not ingredient in all_ingredients):
            all_ingredients.append(ingredient)
    recipes_list.append(recipe)
    

data["recipes_list"], data["all_ingredients"] = recipes_list, all_ingredients

with open(filename, 'wb') as file:
    pickle.dump(data, file)

