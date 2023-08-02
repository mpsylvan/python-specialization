import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

cursor = conn.cursor()


cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")


cursor.execute("""CREATE TABLE IF NOT EXISTS Recipes(
                recipe_id   INT PRIMARY KEY AUTO_INCREMENT,
                name    VARCHAR(50),
                ingredients     VARCHAR(255),
                cooking_time    INT,
                difficulty      VARCHAR(20)     
                )
            """)

# Database functions



def main_menu(conn, cursor):
    # functions

    def calc_difficulty(cooking_time, ingredients):
        difficulty = ""
        if(cooking_time < 10 and len(ingredients) < 4):
            difficulty = "Easy"
        elif (cooking_time < 10 and len(ingredients) >= 4):
            difficulty = "Medium"
        elif (cooking_time >= 10 and len(ingredients) < 4):
            difficulty = "Intermediate"
        elif (cooking_time >= 10 and len(ingredients) >= 4):
            difficulty = "Hard"
        return difficulty

    def create_recipe(conn, cursor):
        name = input(f'What will the name of recipe be? ')
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
        difficulty = calc_difficulty(recipe["cooking_time"], recipe["ingredients"])
        recipe['difficulty'] = difficulty
        ingredients_str = ', '.join(recipe["ingredients"])
        print(ingredients_str)
        cursor.execute(f"""INSERT INTO Recipes(name, ingredients, cooking_time, difficulty) 
                            VALUES ('{recipe['name']}', '{ingredients_str}', {recipe['cooking_time']}, '{recipe['difficulty']}')
                        """)
        conn.commit()
        return

    def search_recipes():
        cursor.execute("SELECT ingredients FROM Recipes")
        results = cursor.fetchall()
        all_ingredients = []
        for row in results:
            ingredient_string = row[0]
            ingredients_list = ingredient_string.split(', ')
            for i in ingredients_list:
                if(not i in all_ingredients):
                    all_ingredients.append(i)
        print("List of ingredients in database")
        print("-------------------------")
        for index, ingredient in enumerate(all_ingredients, 1):
            print(f'{index} -- {ingredient}')
        has_search_term = False
        ingredient_searched = ""
        while not has_search_term:   
            try:
                n = int(input("Enter the number of the ingredient you'd like to search in recipe data: "))    
                ingredient_searched = all_ingredients[n -1]
            except ValueError:
                print('value error: search term must be a number.\n')
            except IndexError:
                print('selection must be within the available list.\n')
            except:
                print("unknown error, please enter a new selection.\n")
            else:
                has_search_term = True
        cursor.execute(f"SELECT recipe_id, name, difficulty, cooking_time, ingredients FROM Recipes WHERE ingredients LIKE '%{ingredient_searched}%'")
        search_results = cursor.fetchall()
        print(f" Recipes using {ingredient_searched}\n")
        for index, result in enumerate(search_results, 1):
            print(f'Recipe {index} : {result[1].capitalize()}')
            print(f'    Difficulty : {result[2]}')
            print(f'    Cooking Time (min) : {result[3]}')
            print('    Ingredients -------------')
            for index, ingredient in enumerate(result[4].split(', '), 1):
                print(f'    {index} -- {ingredient}')

    def update_recipe():
        cursor.execute("SELECT recipe_id, name, cooking_time, difficulty, ingredients from Recipes")
        results = cursor.fetchall()
        print("Here are recipes and their db keys")
        for result in results :
            print( result[0], '---' , result[1].upper())
        has_query_data = False
        db_id = None
        db_column = ""
        while not has_query_data:  
            try:
                db_id = int(input("Enter the id of that recipe you'd update: "))
                while db_column not in ['name', 'cooking_time', 'ingredients']: 
                        db_column = input("Enter the data you would like to update 'name', 'cooking_time', or 'ingredients' (must match one of the 3 strings): ").lower()
            except ValueError:
                print('value error: search term must be a number.\n')
            except IndexError:
                print('selection must be within the available list.\n')
            except:
                print("unknown error, please enter a new selection.\n")
            else:
                has_query_data = True
        filtered_results = [result for result in results if result[0] == db_id]
        if db_column == "name":
            new_name = input("enter a new name for this recipe: ")
            cursor.execute(f"UPDATE Recipes SET name = '{new_name}' WHERE recipe_id = {db_id} ")
            conn.commit()
            print("record updated")
        elif db_column == "cooking_time":
            new_time = int(input('Input a new time in minutes '))
            new_difficulty = calc_difficulty(new_time, filtered_results[0][4].split(', '))
            cursor.execute(f"UPDATE Recipes SET cooking_time = {new_time}, difficulty = '{new_difficulty}' WHERE recipe_id = {db_id} ")
            conn.commit()
            print("record updated")
        elif db_column == "ingredients":
            new_ingredients = []
            finished = False
            while not finished:
                try:
                    ingredient = input(f"Input an ingredient required in {filtered_results[0][1]}:  ")
                    new_ingredients.append(ingredient)
                    response = input("Do you have more ingredients (y or n):  ")
                    if (response == "n"):
                        finished = True
                except ValueError:
                    print('ingredient can only contain letters')

            print(filtered_results[0][2])
            print(new_ingredients)      
            new_difficulty = calc_difficulty(filtered_results[0][2], new_ingredients)
            ingredients_str = ', '.join(new_ingredients)
            cursor.execute(f"UPDATE Recipes SET ingredients = '{ingredients_str}', difficulty = '{new_difficulty}' WHERE recipe_id = {db_id}")
            conn.commit()
            print("record updated.")    
        return
        
    def delete_recipe():
        cursor.execute("SELECT recipe_id, name, cooking_time, difficulty, ingredients from Recipes")
        results = cursor.fetchall()
        print("Here is an overview of the recipes and their db keys")
        for result in results :
            print( result[0], '---' , result[1].upper())
        has_delete_data = False
        db_id = None
        while not has_delete_data:  
            try:
                db_id = int(input("Enter the id of that recipe you'd delete: "))
            except ValueError:
                print('value error: db key must be a number.\n')
            except IndexError:
                print('selection must be within the available list.\n')
            except:
                print("unknown error, please enter a new selection.\n")
            else:
                has_delete_data = True
        cursor.execute(f"DELETE FROM Recipes WHERE recipe_id = {db_id} ")
        conn.commit()
        print('record deleted')
        return
        
        

    # main menu flow
    print("MAIN MENU")
    print("=*" *20)

    choice = "" 

    while (choice != 'quit'):
        print("""Choose an action: 

                    1. Input a new recipe
                    2. Search recipe db for an ingredient
                    3. Update an existing recipe
                    4. Delete a recipe  
                    Type 'quit' to exit the program.            
            """)
        choice = input("Your choice : ")
    
        if(choice == '1'):
            create_recipe(conn, cursor)
        elif(choice == '2' ):
            search_recipes()
        elif(choice == '3'):
            update_recipe()
        elif(choice == '4'):
            delete_recipe()
        

main_menu(conn, cursor)