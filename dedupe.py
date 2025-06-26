import pandas as pd

def flavor_distance(dish1, dish2):
    return sum((dish1.get(flavor, 0) - dish2.get(flavor, 0)) ** 2 for flavor in ['Sweet', 'Sour', 'Salty', 'Bitter', 'Unami']) ** 0.5

def similarity_score(dish1, dish2):
    set1 = set(dish1['ingredients'])
    set2 = set(dish2['ingredients'])
    return len(set1 & set2) / len(set1 | set2) if len(set1 | set2) > 0 else 0

def dedupe_dishes(dishes, flavor_threshold=30, similarity_threshold=0.5):
    clusters = []
    for dish in dishes:
        found_cluster = False
        for cluster in clusters:
            for cluster_dish in cluster:
                if (flavor_distance(dish, cluster_dish) < flavor_threshold and
                        similarity_score(dish, cluster_dish) > similarity_threshold):
                    cluster.append(dish)
                    found_cluster = True
                    break
            if found_cluster:
                break
        if not found_cluster:
            clusters.append([dish])
    return clusters

if __name__ == "__main__":
    flavors_df = pd.read_csv("Flavors.csv")
    ingredients_df = pd.read_csv("ingredients.csv")
    ingredients_map = ingredients_df.copy()
    ingredients_map['dish_name'] = ingredients_map['dish_name'].str.strip().str.lower()
    ingredients_map = ingredients_map.groupby('dish_name')['raw_ingredient'].apply(list).to_dict()
    flavors_df['dish_name'] = flavors_df['dish_name'].str.strip().str.lower()
    input_dishes = input("Enter comma-separated dish names: ").lower().split(",")
    input_dishes = [name.strip() for name in input_dishes]
    filtered_flavors = flavors_df[flavors_df['dish_name'].isin(input_dishes)]
    if filtered_flavors.empty:
        print("No matching dishes found. Please check your input.")
    else:
        dishes = []
        for _, row in filtered_flavors.iterrows():
            dish_name = row['dish_name']
            dish = {
                "dish_name": dish_name,
                "Sweet": float(row["sweet"]),
                "Salty": float(row["salty"]),
                "Sour": float(row["sour"]),
                "Bitter": float(row["bitter"]),
                "Unami": float(row["umami"]),
                "ingredients": ingredients_map.get(dish_name, [])
            }
            dishes.append(dish)
        clusters = dedupe_dishes(dishes)
        for i in range(len(clusters)):
            cluster = clusters[i]
            print("Cluster", i+1, ":", [dish['dish_name'] for dish in cluster])