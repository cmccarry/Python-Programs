class foodItem:
    def __init__(self, name, fat, carbs, protein, servings):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.servings = servings
        self.calories1 = foodItem.get_calories(self, 1)
        self.calories = foodItem.get_calories(self, int(self.servings))
    def get_calories(self, num_servings):
        #Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories
    def nutritionalInfo(self):
        if self.servings == 1:
            print(f"Nutritional information per serving of {self.name}: \
                  \n  Fat: {self.fat} g \
                  \n  Carbohydrates: {self.carbs} g \
                  \n  Protein: {self.protein} g \
                  \n  Number of calories for 1 serving: {self.calories}")
        else:
            print(f"Nutritional information per serving of {self.name}: \
                  \n  Fat: {self.fat} g \
                  \n  Carbohydrates: {self.carbs} g \
                  \n  Protein: {self.protein} g \
                  \n  Number of calories for 1 serving: {self.calories1} \
                  \n  Number of calories for {self.servings} servings: {self.calories}")
    
def main():
    user_input = str(input(f"Enter the food name and any additional information: \n(fat, carbs, protein, servings)")).split()
    name = user_input[0]
    fat = int(user_input[1]) if len(user_input)>1 else 0
    carbs = int(user_input[2]) if len(user_input)>2 else 0
    protein = int(user_input[3]) if len(user_input)>3 else 0
    servings = int(user_input[4]) if len(user_input)>4 else 1
    food = foodItem(name, fat, carbs, protein, servings)
    food.nutritionalInfo()

main()
