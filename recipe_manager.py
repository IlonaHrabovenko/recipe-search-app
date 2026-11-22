
import json
import unicodedata
from pathlib import Path


class RecipeManager:

    def __init__(self, json_path):
        self.json_path = Path(json_path)
        self.recipes = self._load_recipes()

    @staticmethod
    def _normalize(value):
        normalized = unicodedata.normalize("NFC", str(value))
        return normalized.strip().casefold()

    def _load_recipes(self):
        if not self.json_path.is_file():
            raise FileNotFoundError(
                f"Nie znaleziono pliku: {self.json_path}"
            )

        try:
            with self.json_path.open(
                "r",
                encoding="utf-8"
            ) as file:
                recipes = json.load(file)

        except json.JSONDecodeError as error:
            raise ValueError(
                "Plik recipes.json zawiera niepoprawny JSON."
            ) from error

        if not isinstance(recipes, list):
            raise ValueError(
                "Baza przepisów musi być listą."
            )

        for index, recipe in enumerate(recipes):
            if not isinstance(recipe, dict):
                raise ValueError(
                    f"Przepis nr {index + 1} musi być obiektem."
                )

            if not isinstance(recipe.get("name"), str) or not recipe["name"].strip():
                raise ValueError(
                    f"Przepis nr {index + 1} ma niepoprawną nazwę."
                )

            if not isinstance(recipe.get("ingredients"), list):
                raise ValueError(
                    f"Przepis nr {index + 1} musi mieć listę składników."
                )

            if (
                not isinstance(recipe.get("time_minutes"), int)
                or recipe["time_minutes"] < 0
            ):
                raise ValueError(
                    f"Przepis nr {index + 1} ma niepoprawny czas."
                )

        return recipes

    def get_all_recipes(self):
        return list(self.recipes)

    def search_by_ingredient(self, query_ingredient):
        query = self._normalize(query_ingredient or "")

        if not query:
            return []

        return [
            recipe
            for recipe in self.recipes
            if any(
                query in self._normalize(ingredient)
                for ingredient in recipe["ingredients"]
            )
        ]

    def search_by_ingredients(self, query):
        terms = [
            self._normalize(term)
            for term in (query or "").split(",")
        ]

        terms = [term for term in terms if term]

        if not terms:
            return []

        return [
            recipe
            for recipe in self.recipes
            if all(
                any(
                    term in self._normalize(ingredient)
                    for ingredient in recipe["ingredients"]
                )
                for term in terms
            )
        ]

    @staticmethod
    def filter_by_max_time(recipes, max_minutes):
        return [
            recipe
            for recipe in recipes
            if recipe["time_minutes"] <= max_minutes
        ]

    @staticmethod
    def sort_recipes(recipes, sort_order="fastest"):
        reverse = sort_order == "slowest"

        return sorted(
            recipes,
            key=lambda recipe: recipe["time_minutes"],
            reverse=reverse
        )
