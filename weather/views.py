from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

def get_weather(request):
    city = request.GET.get("city", "New York")  # Default city
    api_key = "f250ec9a616f4931a9a92512253004"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    weather_data = response.json()

    context = {
        "city": city,
        "temperature": weather_data["current"]["temp_c"],
        "description": weather_data["current"]["condition"]["text"],
        "icon": weather_data["current"]["condition"]["icon"],
    }
    return render(request, "weather/weather.html", context)