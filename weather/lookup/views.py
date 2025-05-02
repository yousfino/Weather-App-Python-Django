from django.shortcuts import render
import json
import requests

def home(request):
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" +
            zipcode +
            "&distance=5&API_KEY=32D707B9-F40E-4173-BAD9-1C764CB55443"
        )

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if isinstance(api, list) and len(api) > 0:
            category_name = api[0]['Category']['Name']

            if category_name == "Good":
                category_description = "(0 - 50) Enjoy your outdoor activities."
                category_color = "good"
            elif category_name == "Moderate":
                category_description = "(51 - 100) If you are unusually sensitive to ozone, consider reducing your activity level or shorten the amount of time you are active outdoors."
                category_color = "moderate"
            elif category_name == "Unhealthy for Sensitive Groups":
                category_description = "(101 - 150) Unhealthy for Sensitive Groups."
                category_color = "usg"
            elif category_name == "Unhealthy":
                category_description = "(151 - 200) Unhealthy."
                category_color = "unhealthy"
            elif category_name == "Very Unhealthy":
                category_description = "(201 - 300) Very Unhealthy."
                category_color = "veryunhealthy"
            elif category_name == "Hazardous":
                category_description = "(301 - 500) Hazardous."
                category_color = "hazardous"
            else:
                category_description = "Unknown category."
                category_color = "unknown"
        else:
            category_description = "No data available."
            category_color = "nodata"

        return render(request, 'home.html', {
            'api': api,
            'category_description': category_description,
            'category_color': category_color
        })
    else:
        return render(request, 'home.html', {})  # Show a blank form on GET

def about(request):
    return render(request, 'about.html', {})
