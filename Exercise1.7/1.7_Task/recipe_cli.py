# environment imports
from dotenv import load_dotenv
import os
# sql alchemy methods and types
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String


# find .env file and define an env variable from within
load_dotenv()
CONNECTION_URL = os.getenv('CONNECTION_URL')

# make connection via engine 
engine = create_engine(CONNECTION_URL)

# initiate a session bound to engine
Session = sessionmaker(bind=engine)
session = Session()

# access Base object

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "achievement_database"

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(50), nullable = False)
    cooking_time = Column(Integer)
    ingredients = Column(String(255))
    difficulty = Column(String(20))

    def __repr__(self):
        return f"RecipeID : {self.id} -- Recipe Name : {self.name} -- Difficulty {self.difficulty}"

    def __str__(self):
        ingredients_output = "\n"
        ingredients_list = self.ingredients.split(', ')
        for index, ingredient in enumerate(ingredients_list, 1):
            ingredients_output += f'{index} -- {ingredient}\n'
        return f"Recipe Name : {self.name.upper()}\nKey : {self.id}\nDifficulty: {self.difficulty}\nIngredients List {ingredients_output}"

    def calc_difficulty(self):
        difficulty = ""
        self.ingredients_list = self.retrieve_ingredients_as_list()
        if(self.cooking_time < 10 and len(self.ingredients_list) < 4):
            difficulty = "Easy"
        elif (self.cooking_time < 10 and len(self.ingredients_list) >= 4):
            difficulty = "Medium"
        elif (self.cooking_time >= 10 and len(self.ingredients_list) < 4):
            difficulty = "Intermediate"
        elif (self.cooking_time >= 10 and len(self.ingredients_list) >= 4):
            difficulty = "Hard"
        self.difficulty = difficulty

    def retrieve_ingredients_as_list(self):
        if len(self.ingredients) < 1:
            return []
        else:
            return self.ingredients.split(", ")

# create our table and corresponding recipe mapping
Base.metadata.create_all(engine)


def main_menu():
    # functions


    def create_recipe():
        name_captured = False
        while not name_captured:
            name_attempt = input(f'What will the name of recipe be? ')
            if not name_attempt.replace(" ", "").isalpha() or len(name_attempt) > 50:
                print("Name unaccepted. Must be letters only and has 50 char max.")
            else:
                name = name_attempt
                name_captured = True
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

        ingredients_str = ', '.join(ingredients)
        new_recipe = Recipe(
            name = name,
            cooking_time =  cooking_time,
            ingredients = ingredients_str,
            
        )
        new_recipe.calc_difficulty()
        session.add(new_recipe)
        session.commit()

    def view_all_recipes():
        try :
            recipe_list = session.query(Recipe).all()
        except:
            print("There was an issue with the database connection. Shutting down. ")
        else:
            if len(recipe_list) < 1:
                print("Database is empty. Recipes can be added from the main menu")
                return
            else:
                print("(-=-(=-=)-=-)"*6)
                print("*** Recipe Database Overview ***")
                for result in recipe_list:
                    print(result)
                print("ENDOFLIST "*5)


    def search_recipes():
        count = session.query(Recipe).count()
        if count < 1:
            print("Database empty. Recipes can be added from the main menu.")
            return
        results = session.query(Recipe.ingredients).all()
        all_ingredients = []
        for row in results:
            print(row)
            ingredients_list = row[0].split(', ')
            for i in ingredients_list:
                if(not i in all_ingredients):
                    all_ingredients.append(i)
        print("List of ingredients in database")
        print("-------------------------")
        for index, ingredient in enumerate(all_ingredients, 1):
            print(f'{index} -- {ingredient}')
        has_search_term = False
        while not has_search_term:   
            try:
                n = input("Enter the numbers of the ingredients you'd like to search in recipe data separated by space. (e.g 4 8 12)")
                search_keys = n.split(" ")
                try:
                    ingredients_to_search = [int(search_key) for search_key in search_keys]
                    for key in ingredients_to_search:
                        if(key < 1 or key > len(all_ingredients)):
                            print(f'{key} is out of range of ingredients list. Must reenter search keys')
                        continue
                except: 
                    print("Issue with search. Make sure the ingredients are entered as numbers, separated by a space.")
                else:
                    like_terms = ['%'+ all_ingredients[key -1]+'%' for key in ingredients_to_search]
                    conditions = []
                    for like_term in like_terms:
                        conditions.append(Recipe.ingredients.like(like_term))
                    
                    
            except:
                print("unknown error, please enter a new selection.\n")
            else:
                has_search_term = True
        search_results = session.query(Recipe).filter(*conditions).all()
        for result in search_results:
            print(result)
    

    def edit_recipe():
        if session.query(Recipe).count() < 1:
            print("Empty database.")
            return
        results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
        print("\tRecipe Overview")
        for recipe in results:
            print(f'key : {recipe[0]} --- {recipe[1].upper()}')
        has_query_data = False
        db_id = None
        db_column_key = None
        while not has_query_data:  
            db_id = int(input("Enter the id of that recipe you'd update: "))
            if db_id not in [recipe[0] for recipe in results]:
                print("Exiting... Key did not match the available database keys. ")
                return
            recipe_to_edit = session.query(Recipe).filter(Recipe.id == db_id).one()
            print("******* Data that can be edited ******* (below)")
            print(f' [1] (name) --- {recipe_to_edit.name}')
            print(f' [2] (ingredients) --- {recipe_to_edit.ingredients}')
            print(f' [3] (cooking time) --- {recipe_to_edit.cooking_time}')
            while db_column_key not in [n for n in range(1,4)]:
                    try: 
                        db_column_key = int(input("Enter 1, 2, or 3 for corresponding column to edit. (will repeat until proper entry received) "))
                    except ValueError:
                        print("Input must be a number, restarting ")
                        return
                    else:
                        has_query_data = True
        if db_column_key == 1:
            new_name = input("What will the new recipe name be? ")
            session.query(Recipe).filter(Recipe.id == db_id).update({Recipe.name : new_name })
            session.commit()
            
        elif db_column_key == 2:
            finished = False
            ingredients = []
            while not finished:
                try:
                    ingredient = input(f"Input an ingredient required in {recipe_to_edit.name}:  ")
                    ingredients.append(ingredient)
                    response = input("Do you have more ingredients (y or n):  ")
                    if (response == "n"):
                        finished = True
                except ValueError:
                    print('ingredient can only contain letters')
            ingredients_str = ', '.join(ingredients)
            recipe_to_edit.ingredients = ingredients_str
            recipe_to_edit.calc_difficulty()
            print(recipe_to_edit.retrieve_ingredients_as_list())
            session.commit()

        elif db_column_key == 3:
            data_received = False
            while not data_received:
                try:
                    new_time = int(input(f"What will the new cooking time for {recipe_to_edit.name} be? (in minutes) "))
                except ValueError:
                    print("input must be a whole number. ")
                else:
                    data_received = True
            recipe_to_edit.cooking_time = new_time
            recipe_to_edit.calc_difficulty()
            session.commit()
            
    def delete_recipe():
        if session.query(Recipe).count() < 1:
            print("Empty database.")
            return
        results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
        print("\tRecipe Overview")
        for recipe in results:
            print(f'key : {recipe[0]} --- {recipe[1].upper()}')
        has_delete_data = False
        db_id = None
        while not has_delete_data:  
            user_input = input("\nEnter the id of the recipe you'd delete (press ENTER to quit action.)  ")
            try:
                db_id = int(user_input)
            except ValueError:
                return
            else:
                has_delete_data = True    
        recipe_to_delete = session.query(Recipe).filter(Recipe.id == db_id).one()
        choice = input(f"You are about to delete the recipe {recipe_to_delete.name.capitalize()}. Confirm DELETE with 'y' or exit with any key.")
        if choice == 'y' or choice == 'Y':        
            session.delete(recipe_to_delete)
            session.commit()
            return
        else:
            print('exiting, no action taken...')
            return None
        
        

    # main menu flow
    print("MAIN MENU")
    print("=*" *20)

    choice = "" 

    while (choice != 'quit'):
        print("""Choose an action: 

                    1. Input a new recipe
                    2. Database overview
                    3. Search recipes by ingredient
                    4. Edit a recipe  
                    5. Delete a recipe
                    Type 'quit' to exit the program.            
            """)
        choice = input("Your choice : ")
    
        if(choice == '1'):
            create_recipe()
        elif(choice == '2' ):
            view_all_recipes()
        elif(choice == '3'):
            search_recipes()
        elif(choice == '4'):
            edit_recipe()
        elif(choice == '5'):
            delete_recipe()
    session.close()          
    print("exiting program.")

main_menu()