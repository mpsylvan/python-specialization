class Height():

    def __init__(self, title, feet, inches):
        self.title = title
        self.feet = feet
        self.inches = inches
    
    def __str__(self):
        height_string = f'Height {self.title} : {self.feet} feet {self.inches} inches'
        return height_string
    
    def __add__(self, other):
        height_a_inches = self.feet * 12 + self.inches
        height_b_inches = other.feet * 12 + other.inches
        total_height_inches = height_a_inches + height_b_inches
        height_feet = total_height_inches // 12
        height_inches = total_height_inches - (height_feet * 12)
        return Height('combined height', height_feet, height_inches)
    
    def __sub__(self, other):
        height_a_inches = self.feet * 12 + self.inches
        height_b_inches = other.feet * 12 + other.inches
        difference_height_inches = height_a_inches - height_b_inches
        height_feet = difference_height_inches // 12
        height_inches = difference_height_inches - (height_feet * 12)
        return Height('reduced height', height_feet, height_inches)


person =  Height('person',5, 10)
dog = Height('dog', 3, 9)
person_plus_dog = person + dog
person_minus_dog = person - dog

print(person)
print(dog)
print(person_plus_dog)
print(person_minus_dog)
