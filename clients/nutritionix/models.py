from enum import StrEnum

from pydantic import BaseModel


class Units(StrEnum):
    grams = "g"


class UnitedFood(BaseModel):
    value: float
    unit: Units

    def __str__(self):
        return f"{self.value}{self.unit}"

    @property
    def display(self):
        return str(self)


class FoodItem(BaseModel):
    name: str
    quantity: float
    unit: str
    protein: UnitedFood
    calories: float
    fat: UnitedFood
    carbs: UnitedFood


class FoodSummary(BaseModel):
    total_protein: str
    total_calories: float
    total_fat: str
    total_carbs: str


class FoodItemsOut(BaseModel):
    """
    BaseModel representing the model that will be returned to the client
    """
    items: list[FoodItem]
    summary: FoodSummary
