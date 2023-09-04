class MealRecommender:
    def __init__(self):
        self.meal_options = {
            'breakfast': {
                'vegan': 'Oatmeal with fruits and nuts',
                'vegetarian': 'Vegetable omelette',
                'non-vegetarian': 'Ham and cheese omelette'
            },
            'lunch': {
                'vegan': 'Quinoa Salad with mixed vegetables',
                'vegetarian': 'Grilled cheese sandwich with tomato soup',
                'non-vegetarian': 'Chicken Caesar salad'
            },
            'dinner': {
                'vegan': 'Vegetable stir fry with tofu',
                'vegetarian': 'Pasta with marinara sauce',
                'non-vegetarian': 'Grilled salmon with asparagus'
            }
        }

    def recommend_meal(self, meal_time, dietary_pref):
        try:
            return self.meal_options[meal_time.lower()][dietary_pref.lower()]
        except KeyError:
            return 'Sorry, we could not find a meal for your preferences. Please try again.'

# Initialize MealRecommender
recommender = MealRecommender()

# Get user input
meal_time = input("Enter the meal time (breakfast, lunch, or dinner): ")
dietary_pref = input("Enter your dietary preference (vegan, vegetarian, or non-vegetarian): ")

# Recommend a meal
meal = recommender.recommend_meal(meal_time, dietary_pref)

print(f"We recommend you have {meal} for {meal_time}.")
