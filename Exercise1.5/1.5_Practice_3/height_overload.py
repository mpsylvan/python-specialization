class Height():

    def __init__(self, feet, inches):
        
        self.feet = feet
        self.inches = inches
    
    def __str__(self):
        height_string = f'Height : {self.feet} feet {self.inches} inches'
        return height_string
    
    def __add__(self, other):
        height_a_inches = self.feet * 12 + self.inches
        height_b_inches = other.feet * 12 + other.inches
        total_height_inches = height_a_inches + height_b_inches
        height_feet = total_height_inches // 12
        height_inches = total_height_inches - (height_feet * 12)
        return Height(height_feet, height_inches)
    
    def __sub__(self, other):
        height_a_inches = self.feet * 12 + self.inches
        height_b_inches = other.feet * 12 + other.inches
        difference_height_inches = height_a_inches - height_b_inches
        height_feet = difference_height_inches // 12
        height_inches = difference_height_inches - (height_feet * 12)
        return Height(height_feet, height_inches)

    def __gt__(self, other):
        height_a_inches = self.feet * 12 + self.inches
        height_b_inches = other.feet * 12 + other.inches
        return height_a_inches > height_b_inches


    def __ge__(self, other):
        height_a_inches = self.feet * 12 + self.inches
        height_b_inches = other.feet * 12 + other.inches
        return height_a_inches >= height_b_inches


    def __ne__(self, other):
        height_a_inches = self.feet * 12 + self.inches
        height_b_inches = other.feet * 12 + other.inches
        return height_a_inches != height_b_inches
    
    def __lt__(self, other):
        height_a_inches = self.feet * 12 + self.inches
        height_b_inches = other.feet * 12 + other.inches
        return height_a_inches < height_b_inches
        
    
person =  Height(5, 10)
dog = Height(3, 9)
person_plus_dog = person + dog
person_minus_dog = person - dog

print(person)
print(dog)
print(person_plus_dog)
print(person_minus_dog)
print(Height(4, 6) > Height( 4, 5))
print(Height(4, 5) >= Height( 4, 5))
print(Height(5, 10) != Height( 5, 6))


heights = [Height(5, 6), Height(5, 5), Height(6, 1), Height(7, 1), Height(5,10)]

heights = sorted(heights)

for height in heights:
    print(height)