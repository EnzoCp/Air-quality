from django.shortcuts import render


# Create your views here.


def home(request):
    import json
    import requests

    if request.method == 'POST':
        zipcode = request.POST['zipcode']
        api_request = requests.get(
            "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=" + zipcode + "&date=2020-11-11&distance=5&API_KEY=EFDA23AC-9FB1-4DA7-8765-6813521A7E83")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api ="Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50)Air quality is considered satisfactory, and air pollution poses little or no risk"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51-100) Air quality is acceptable; However, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) Although general public is no likely to be affectedat this AQI range, people with lung desease, older adults and children are at a greater risk from exposure to ozone, where as persons with heart and lung disease, older adults and children areat a greater risk from the presence of particles in the air"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151-200) Everyone may begin to experience health effects; membersof sensitive groups may experience more serious health effects."
            category_color = "un"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201-300) Health Alert: Everyone may experience more serious health effects"
            category_color = "vun"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(300-500) Health warnings of emergency conditions. The entire population is more likely to be affected."
            category_color = "haz"

        data = {'api': api, 'category_description': category_description, 'category_color': category_color}
        return render(request, 'lookup/home.html', data)

    else:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=889901&date=2020-11-11&distance=5&API_KEY=EFDA23AC-9FB1-4DA7-8765-6813521A7E83")
        data = {'api_request': api_request}
        return render(request, 'lookup/home.html', data)

def about(request):
    data = {}
    return render(request, 'lookup/about.html', data)
