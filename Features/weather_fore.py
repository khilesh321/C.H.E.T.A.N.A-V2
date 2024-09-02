import requests

def weather_forecast2(city="yawal"):
    # city = "yawal"
    api_key = "1566b66ef12840f0bd553196f7e95e87"  # replace with your valid API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    res = requests.get(url)
    if res.status_code == 200:
        res_json = res.json()
        if 'weather' in res_json and 'main' in res_json:
            weather_description = res_json["weather"][0]["description"]
            temp_kelvin = res_json["main"]["temp"]
            feels_like_kelvin = res_json["main"]["feels_like"]
            temp_celsius = temp_kelvin - 273.15
            feels_like_celsius = feels_like_kelvin - 273.15
            return weather_description, f"{temp_celsius:.2f}°C", f"{feels_like_celsius:.2f}°C"
        else:
            print("Invalid response format")
            return None
    else:
        print(f"API request failed with status code {res.status_code}")
        print(res.content)
        return None

if __name__ == '__main__':
    weather_data = weather_forecast2()
    if weather_data:
        weather, temp, feels_like = weather_data
        print(f"Weather: {weather}")
        print(f"Temperature: {temp}")
        print(f"Feels like: {feels_like}")
    else:
        print("Failed to retrieve weather data")