from django.shortcuts import render
from .models import *

def home(request):
    effects = Effects.objects.all()
    solutions = Solutions.objects.all()
    readmores = ReadMore.objects.all()
    opinions = Opinion.objects.all()
    return render(request, 'core/home.html', {'effects': effects, 'solutions': solutions, 'readmores': readmores, 'opinions': opinions,})

def detail(request):
    opinions = Opinion.objects.all()
    return render(request, 'core/detail.html', {'opinions': opinions,})

def info(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + str(zipcode) + "&distance=1&API_KEY=A4C73258-C694-4AC4-8680-5B8284D5D581")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[1]['Category']['Name'] == "Good":
            description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[1]['Category']['Name'] == "Moderate":
            description = "(51-100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[1]['Category']['Name'] == "USG":
            description = "(101-150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk form the presence of particles in the air."
            category_color = "usg"
        elif api[1]['Category']['Name'] == "Unhealthy":
            description = "(151-200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[1]['Category']['Name'] == "Very Unhealthy":
            description = "(201-300) Health alert: everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif api[1]['Category']['Name'] == "Hazardous":
            description = "(301-500) Health warnings of emergency condition. The entire population is more likely to be affected."
            category_color = "hazardous"

        return render(request, 'core/info.html',
                      {'api': api, 'description': description, 'category_color': category_color, 'zipcode': zipcode, 'info': info})

    else:
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=11217&distance=25&API_KEY=A4C73258-C694-4AC4-8680-5B8284D5D581")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            description = "(51-100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "USG":
            description = "(101-150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk form the presence of particles in the air."
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            description = "(151-200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            description = "(201-300) Health alert: everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            description = "(301-500) Health warnings of emergency condition. The entire population is more likely to be affected."
            category_color = "hazardous"

        return render(request, 'core/info.html', {'api': api, 'description': description, 'category_color': category_color,})