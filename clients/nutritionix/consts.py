from config.settings import settings

NUTRIENTS_URI = f"{settings.NUTRITIONIX_API_URL}/v2/natural/nutrients"
REQUEST_HEADERS = {
    "x-app-id": settings.NUTRITIONIX_APP_ID,
    "x-app-key": settings.NUTRITIONIX_APP_KEY.get_secret_value(),
    "Content-Type": "application/json"
}
