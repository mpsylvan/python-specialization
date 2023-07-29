import pickle

def display_recipe(recipe):
    print(f'Recipe: {recipe["name"].capitalize()}')
    print(f'Cooking Time (min): {recipe["cooking_time"]}')
    print('Ingredients --------------- ')
    for index,  ingredient in enumerate(recipe["ingredients"], 1):
        print(f'Ingredient {index} : {ingredient} ')
    print(f'Difficulty: {recipe["Difficulty"]}')
    print('----------------------------------')


def search_ingredients (data):
    print("List of used ingredients")
    print("-------------------------")
    for index, ingredient in enumerate(data["all_ingredients"], 1):
        print(f'{index} -- {ingredient}')
    
    loading = True
    while loading:   
        try:
            n = int(input("Enter the number of the ingredient you'd like to search in recipe data: "))    
            ingredient_searched = data['all_ingredients'][n -1]
        except ValueError:
            print('value error: search term must be a number.\n')
        except IndexError:
            print('selection must be within the available list.\n')
        except:
            print("unknown error, please enter a new selection.\n")
        else:
            print(f'List of Recipes using {ingredient_searched.upper()}')
            print("******************************")
            for recipe in data['recipes_list']:
                if(ingredient_searched in recipe['ingredients']):
                    display_recipe(recipe)
            loading = False

loading = True # variable to track when good input comes in.
while loading:
    try:
        filename = input("What is the name of the file you are searching? ")
        filename += ".bin"
        with open(filename, 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print("This file has not been found. Please check your inputs. ")
    else:
        search_ingredients(data)
        loading = False
