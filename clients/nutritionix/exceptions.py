from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND


class FoodItemNotFound(HTTPException):
    def __init__(self, query: str):
        super().__init__(status_code=HTTP_404_NOT_FOUND, detail=f"Food item '{query}' not found")
