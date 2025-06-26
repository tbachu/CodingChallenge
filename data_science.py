import pandas as pd
import os

def flavor_distance(dish, profile):
    # Handle missing flavors by defaulting to 0
    return sum((dish.get(flavor, 0) - profile.get(flavor, 0)) ** 2 for flavor in profile) ** 0.5

def find_closest_dish(dishes, profile, num):
    dishes_sorted = sorted(dishes, key=lambda d: flavor_distance(d, profile))
    return dishes_sorted[:num]


dishes = pd.read_csv('data.csv').to_dict(orient='records')
savory_profile = {'Sweet': 10, 'Sour': 15, 'Salty': 25, 'Bitter': 5, 'Umami': 45}
sweet_profile = {'Sweet': 65, 'Sour': 10, 'Salty': 5, 'Bitter': 10, 'Umami': 10}
mixed_profile = {'Sweet': 15, 'Sour': 30, 'Salty': 25, 'Bitter': 10, 'Umami': 20}

savory_dishes = find_closest_dish(dishes, savory_profile, 15)
sweet_dishes = find_closest_dish(dishes, sweet_profile, 5)
mixed_dishes = find_closest_dish(dishes, mixed_profile, 5)
selected = savory_dishes + sweet_dishes + mixed_dishes

print([dish['dish_name'] for dish in selected])
    