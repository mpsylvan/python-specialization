class ShoppingList():

    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if (not item in self.shopping_list):
            self.shopping_list.append(item)
            print(item, " ADDED")
        else:
            print("item already present.")
    
    def remove_item(self, item):
        if (item in self.shopping_list):
            remove_index = self.shopping_list.index(item)
            self.shopping_list.pop(remove_index)
            print(item, " REMOVED")
        else:
            print("Item not present in list.")

    def view_list(self):
        for i, e in enumerate(self.shopping_list, 1):
            print(f'{i} - {e}')


pet_store_list = ShoppingList('Pet Store Shopping List')

items = ['dog food', 'frisbee', 'bowl', 'collars', 'flea collars']

for i in items:
    pet_store_list.add_item(i)


pet_store_list.remove_item('flea collars')
pet_store_list.add_item('frisbee')
pet_store_list.view_list()


