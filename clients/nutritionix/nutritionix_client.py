import requests
from requests import HTTPError
from starlette.status import HTTP_404_NOT_FOUND

from clients.nutritionix.consts import NUTRIENTS_URI, REQUEST_HEADERS
from clients.nutritionix.exceptions import FoodItemNotFound
from clients.nutritionix.models import FoodItem, UnitedFood, Units, FoodSummary, FoodItemsOut


class NutritionixClient:
    @staticmethod
    def query_nutrition(query: str) -> FoodItemsOut:
        response = requests.post(
            NUTRIENTS_URI,
            headers=REQUEST_HEADERS,
            json={"query": query}
        )
        try:
            response.raise_for_status()
        except HTTPError as e: # TODO make generic client error handling
            if e.response.status_code == HTTP_404_NOT_FOUND:
                raise FoodItemNotFound(query)

        data = response.json()

        items = []
        for item in data["foods"]:
            items.append(FoodItem(
                name=item["food_name"],
                quantity=item["serving_qty"],
                unit=item["serving_unit"],
                protein=UnitedFood(value=item["nf_protein"], unit=Units.grams),
                calories=item["nf_calories"],
                fat=UnitedFood(value=item["nf_total_fat"], unit=Units.grams),
                carbs=UnitedFood(value=item["nf_total_carbohydrate"], unit=Units.grams)
            ))

        total_protein = UnitedFood(value=0, unit=Units.grams)
        total_calories = 0
        total_fat = UnitedFood(value=0, unit=Units.grams)
        total_carbs = UnitedFood(value=0, unit=Units.grams)
        for food_item in items:
            total_protein.value += food_item.protein.value
            total_calories += food_item.calories
            total_fat.value += food_item.fat.value
            total_carbs.value += food_item.carbs.value

        food_summary = FoodSummary(total_protein=total_protein.display, total_calories=total_calories,
                                   total_fat=total_fat.display, total_carbs=total_carbs.display)
        return FoodItemsOut(items=items, summary=food_summary)
