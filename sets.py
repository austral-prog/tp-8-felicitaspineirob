from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    return drink_name + " Cocktail" if ALCOHOLS.intersection(drink_ingredients) else drink_name + " Mocktail"

