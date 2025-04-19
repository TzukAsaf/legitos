from fastapi import APIRouter
from fastapi import Response

from clients.nutritionix.nutritionix_client import NutritionixClient

router = APIRouter(prefix="/nutrition")


@router.get("/values")
def get_nutrition_of_item(query: str):
    return NutritionixClient().query_nutrition(query)
