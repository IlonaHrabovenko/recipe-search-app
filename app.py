
from flask import Flask, render_template, request
from recipe_manager import RecipeManager

app = Flask(__name__)
recipe_manager = RecipeManager("data/recipes.json")


@app.route("/", methods=["GET"])
def index():
    ingredients = request.args.get("ingredients", "").strip()

    if ingredients:
        recipes = recipe_manager.search_by_ingredients(ingredients)
    else:
        recipes = recipe_manager.get_all_recipes()

    return render_template(
        "index.html",
        recipes=recipes,
        ingredients=ingredients
    )


if __name__ == "__main__":
    app.run(debug=True)
