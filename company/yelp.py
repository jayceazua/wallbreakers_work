def number_unique_meals(meals):
    # do I make a copy of this list or edit the incoming input
    unique_count = 0
    
    # only handles the given test input
    # not for arbitrary test inputs

    meal_one = meals[0]
    meal_two_index = 1
    while meal_two_index < len(meals):
        meal_two = meals[meal_two_index]

        # looks cleaner when negating the sanity check
        if set(meal_one.ingredients) != set(meal_two.ingredients):
            unique_count += 1

        meal_two_index += 1

    return unique_count


# ... Everything below works ...
if __name__ == "__main__":
    class Meal(object):

        def __init__(self, name, ingredients):
            self.name = name
            self.ingredients = ingredients

# Sample input
    meals = []

    raw_data = [
        {'name': 'Basic Burger', 'ingredients': [
            'Lettuce', 'Tomato', 'Onion', 'Patty']},  # 1

        {'name': 'Chief Cheese Burger', 'ingredients': [
            'Cheese', 'Tomato',  'Patty', 'Lettuce']},  # 2

        {'name': 'Jay\'s burger', 'ingredients': [
            'Onion', 'Tomato', 'Patty', 'Lettuce']},  # 1

        {'name': 'High Water Sandwhich', 'ingredients': [
            'Tomato', 'Patty', 'Lettuce', 'Cheese']},  # 2

        {'name': 'Pasta', 'ingredients': [
            'Meat Sauce', 'Cheese', 'Tomato']},  # 3

        {'name': 'someshit', 'ingredients': [
            'Cheese', 'Meat Sauce', 'Tomato']},  # 3
        {'name': 'Chief Cheese Burger', 'ingredients': [
            'Cheese', 'Tomato',  'Patty', 'Lettuce']},  # 2

        {'name': 'Jay\'s burger', 'ingredients': [
            'Onion', 'Tomato', 'Patty', 'Lettuce']},  # 1

        {'name': 'High Water Sandwhich', 'ingredients': [
            'Tomato', 'Patty', 'Lettuce', 'Cheese']},  # 2

        {'name': 'Pasta', 'ingredients': [
            'Meat Sauce', 'Cheese', 'Tomato']},  # 3
    ]

    for data in raw_data:
        meal = Meal(data['name'], data['ingredients'])
        meals.append(meal)

print(number_unique_meals(meals))
