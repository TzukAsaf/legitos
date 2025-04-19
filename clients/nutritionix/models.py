from pydantic import BaseModel


class FoodItem(BaseModel):
    name: str
    quantity: float
    unit: str
    protein: float
    calories: float
    fat: float
    carbs: float
