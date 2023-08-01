class Recipe():
    
    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = None
        self.difficulty = ""

    def __str__(self):
        output = f'{self.name.upper()}\n' + f'Cooking Time (min) : {self.cooking_time}\n' + f'Difficulty: {self.difficulty}'
        for index, ingredient in enumerate(self.ingredients):
            output += f'\n {index} --- {ingredient}' 
        return output

    def set_name(self, name):
        self.name = name
    
    def set_cooking_time(self, time):
        self.cooking_time = time

    def add_ingredients(self, *ingredients):
        for i in ingredients:
            if(not i in self.ingredients):
                self.ingredients.append(i)
        self.update_all_ingredients()
    

    def get_ingredients(self):
        return self.ingredients
    

    def calculate_difficulty(self, cooking_time, ingredients):
        difficulty = ""
        if(cooking_time < 10 and len(ingredients) < 4):
            difficulty = "Easy"
        elif (cooking_time < 10 and len(ingredients) >= 4):
            difficulty = "Medium"
        elif (cooking_time >= 10 and len(ingredients) < 4):
            difficulty = "Intermediate"
        elif (cooking_time >= 10 and len(ingredients) >= 4):
            difficulty = "Hard"
        self.difficulty = difficulty
    

    def get_difficulty(self):
        if(self.difficulty == ""):
            self.calculate_difficulty(self.cooking_time, self.ingredients)
        return self.difficulty
    

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients
    

    def update_all_ingredients(self):
        for ing in self.ingredients:
            if(not ing in Recipe.all_ingredients):
                Recipe.all_ingredients.append(ing)
                Recipe.all_ingredients.sort()
    

def recipe_search(list_of_recipes, search_term):
    for recipe in list_of_recipes:
        if search_term in recipe.get_ingredients():
            print(recipe)
    return


# step 
tea = Recipe('Tea')
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)
tea.get_difficulty()
print(tea)

# step 

coffee = Recipe('Coffee')
coffee.add_ingredients('Coffee Grinds', "Sugar", "Water")
coffee.set_cooking_time(5)
coffee.get_difficulty()


#step 

cake = Recipe('Cake')
cake.add_ingredients('Sugar', 'Butter', 'Eggs', 'Vanilla Essence', 'Flour','Baking Powder', 'Milk')
cake.set_cooking_time(50)
cake.get_difficulty()

#step

banana_smoothie = Recipe('Banana Smoothie')
banana_smoothie.add_ingredients('Bananas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice Cubes')
banana_smoothie.set_cooking_time(5)
banana_smoothie.get_difficulty()


recipes_list = [tea, coffee, cake, banana_smoothie]

print("Calling search for 'Water'-----------------")
recipe_search(recipes_list, "Water")
print("Calling search for 'Sugar'-----------------")
recipe_search(recipes_list, "Sugar")
print("Calling search for 'Bananas'---------------")
recipe_search(recipes_list, "Bananas")

