from recipe_utils import all_recipes
from pymongo import MongoClient

client = MongoClient()
db = client.recipes
link_to_search = "http://allrecipes.com/recipes/80/main-dish"
links = all_recipes.get_recipe_links(link_to_search)
recipes = list()

for link in links:
    recipe = all_recipes.get_recipe_from_url(link)

    # If the recipe is not already in the database
    if not db.recipes.find({"name": recipe['name']}):
        db.recipes.insert_one(recipe)
        print("Added: " + recipe['name'])
    else:
        print(recipe['name'] + " is already in the database")


