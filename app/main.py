from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
import json
import time
from models.Recipe import Recipe
import deletelater

app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:4200"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

EDAMAM_APP_ID = deletelater.EDAMAM_APP_ID #os.environ['EDAMAM_APP_ID']
EDAMAM_API_KEY = deletelater.EDAMAM_API_KEY #os.environ['EDAMAM_API_KEY']
BASE_URL = "https://api.edamam.com/api/recipes/v2"

ingredients_json_file_path = "ingredients.json"
basic_ingredients_json_file_path = "ingredients.json"

with open(ingredients_json_file_path, "r") as file:
    all_ingredients = json.load(file)

with open(basic_ingredients_json_file_path, "r") as file:
    basic_ingredients = json.load(file)
    
# put these endpoints in a separate file
def search_recipes(ingredients, only_picked_ingredients, cuisine = "", health = ""):
    params = {
        "type": "public",
        "app_id": EDAMAM_APP_ID,
        "app_key": EDAMAM_API_KEY,
        "q": ",".join(ingredients)
    }

    if cuisine:
        params["cuisineType"] = cuisine
    if health:
        params["health"] = health


    if only_picked_ingredients:
        print("yooooo we here thooo")
        params["allowedIngredient[]"] = ingredients
        params["q"] = ""

        excluded_ingredients = [ingredient for ingredient in all_ingredients if ingredient not in ingredients]
        params["excludedIngredient[]"] = excluded_ingredients

    print("naaaah")
    response = requests.get(BASE_URL, params = params)

    if response.status_code == 200:
        data = response.json()
        recipes = []

        for hit in data['hits']:
            recipe_data = hit['recipe']
            recipe = Recipe(
                label = recipe_data['label'],
                image = recipe_data['image'],
                url = recipe_data['url'],
                dietLabels = recipe_data['dietLabels'],
                portion = recipe_data['yield'],
                healthLabels = recipe_data['healthLabels'],
                cautions = recipe_data['cautions'],
                ingredientLines = recipe_data['ingredientLines'],
                calories = recipe_data['calories'],
                totalTime = recipe_data['totalTime'],
                cuisineType = recipe_data['cuisineType'],
                totalNutrients = recipe_data['totalNutrients'],
            )
            recipes.append(recipe)

        return recipes
    else:
        raise HTTPException(status_code=400, detail="Error fetching recipes")


@app.get("/recipes")
def get_recipes(ingredients: str,cuisine:str = "", health:str = ""):
    try:
        ingredients_list = ingredients.split(",")
        recipes = search_recipes(ingredients_list, False, cuisine, health)
        print("not strict: ",len(recipes))
        return {"recipes": recipes}
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error":str(e)}, 500
        


@app.get("/recipes/strict")
def get_recipes_with_only_given_ingredients(ingredients: str,cuisine:str = "", health:str = ""):
    try:
        ingredients_list = ingredients.split(",")
        recipes = search_recipes(ingredients_list, True, cuisine, health)
        print("strict: ",len(recipes))
        return {"recipes": recipes}
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error":str(e)}, 500
        


def save_ingredients_to_json(ingredients, filename="ingredients.json"):
    with open(filename, "w") as f:
        json.dump(list(ingredients), f, indent=4)



def fetch_recipes(keyword, max_pages=1):
    ingredients_set = set()
    url = f"https://api.edamam.com/api/recipes/v2?type=public&q={keyword}&app_id={EDAMAM_APP_ID}&app_key={EDAMAM_API_KEY}"
    page = 0

    while url and page < max_pages:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            for hit in data['hits']:
                for ingredient in hit['recipe']['ingredients']:

                    #food = ingredient.get('food')
                    #food_category = ingreident.get('foodCategory')

                    #if food and food_category:
                        #ingredients_set.add((food.lower(), food_category))
                    
                    if(ingredient.get('foodCategory') not in ['Condiments and sauces', 'Oils', 'water', 'sugars']):
                        ingredients_set.add(ingredient['food'])


            url = data.get('_links', {}).get('next', {}).get('href')
            page += 1
        else:
            print(f"Error fetching data: {response.status_code}, {response.text}")
            break

    return ingredients_set



#all_ingredients = set()
#for keyword in keywords:
#    print(f"Fetching recipes for keyword {keyword}")
#    ingredients = fetch_recipes(keyword)
#    all_ingredients.update([ingredient.lower() for ingredient in ingredients])

#save_ingredients_to_json(all_ingredients)

def load_existing_ingredients(filename="ingredients.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return set(json.load(file))
    else:
        return set()

        

#all_ingredients = set()
all_ingredients = load_existing_ingredients()


def add_ingredients_to_json():
    keywords = ["chicken", "beef", "pork"]
    for keyword in keywords:
        print(f"Fetching recipes for keyword {keyword}")
        ingredients = fetch_recipes(keyword)
        #all_ingredients.update([ingredient['text'].lower() for ingredient in ingredients if ingredient.get('foodCategory') not in ["Condiments and sauces", "water"]])

        all_ingredients.update([ingredient.lower() for ingredient in ingredients])

        print("\nkeyword sent\n")
        time.sleep(30)
    save_ingredients_to_json(all_ingredients)


#add_ingredients_to_json()
keywords = "coconut, shrimp, coconut milk"
#get_recipes_with_only_given_ingredients(keywords,"","" )
#get_recipes(keywords,"","" )

if __name__ == "__main__":
    app.run(debug=True)