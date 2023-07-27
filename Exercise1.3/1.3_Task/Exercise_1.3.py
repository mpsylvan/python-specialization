recipes_list = []
ingredients_list= []

def take_recipe(n):
    name = input(f'What will the name of recipe {n + 1} be? ')
    cooking_time = int(input("How long will it take to cook? (minutes) "))
    ingredients = []
    finished = False
    while not finished:
        ingredient = input(f"Input an ingredient required in {name}:  ")
        ingredients.append(ingredient)
        response = input("Do you have more ingredients (y or n):  ")
        if (response == "n"):
            finished = True
    recipe = {
        "name" : name,
        "cooking_time" : cooking_time,
        "ingredients" : ingredients
    }
    return recipe

n = int(input("How many recipes will you be entering today? "))

for i in range(n):
    recipe = take_recipe(i)
    for ingredient in recipe["ingredients"]:
        if (not ingredient in ingredients_list):
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for recipe in recipes_list:
    if(recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4):
        recipe["Difficulty"] = "Easy"
    elif (recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4):
        recipe["Difficulty"] = "Medium"
    elif (recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4):
        recipe["Difficulty"] = "Intermediate"
    elif (recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) > 4):
        recipe["Difficulty"] = "Hard"
    print('')
    print(f'Recipe: {recipe["name"].capitalize()}')
    print(f'Cooking Time (min): {recipe["cooking_time"]}')
    print('Ingredients --------------- ')
    for index,  ingredient in enumerate(recipe["ingredients"], 1):
        print(f'Ingredient {index} : {ingredient} ')
    print(f'Difficulty: {recipe["Difficulty"]}')
    print('----------------------------------------')

print(f'Ingredients available across all {len(recipes_list)} recipes')
print("---------------------------------------------")
ingredients_list.sort()
for ingredient in ingredients_list:
    print(ingredient.capitalize())






