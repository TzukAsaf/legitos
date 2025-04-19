import requests

from clients.nutritionix.consts import NUTRIENTS_URI, REQUEST_HEADERS
from clients.nutritionix.models import FoodItem


class NutritionixClient:
    @staticmethod
    def query_nutrition(query: str, timezone: str = "Asia/Jerusalem") -> list[FoodItem]:
        response = requests.post(
            NUTRIENTS_URI,
            headers=REQUEST_HEADERS,
            json={"query": query, "timezone": timezone}
        )
        response.raise_for_status()
        data = response.json()

        results = []
        for item in data["foods"]:
            results.append(FoodItem(
                name=item["food_name"],
                quantity=item["serving_qty"],
                unit=item["serving_unit"],
                protein=item["nf_protein"],
                calories=item["nf_calories"],
                fat=item["nf_total_fat"],
                carbs=item["nf_total_carbohydrate"]
            ))

        return results
