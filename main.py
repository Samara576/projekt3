import requests

def get_weather(city):
    api_key = "your_api_key"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"{city}: {data['current']['temp_c']}°C")
    else:
        print("Маалымат табылган жок")

# get_weather("Bishkek")