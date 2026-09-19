import requests


def show_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")
        return

    if response.status_code != 200:
        print("Could not get weather data.")
        return

    data = response.json()

    current = data["current_condition"][0]

    temperature = current["temp_C"]
    temperature_f = current["temp_F"]
    feels_like = current["FeelsLikeC"]
    feels_like_f = current["FeelsLikeF"]
    condition = current["weatherDesc"][0]["value"]
    humidity = current["humidity"]
    wind_speed = current["windspeedKmph"]

    print("-" * 30)
    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature} C / {temperature_f} F")
    print(f"Feels Like: {feels_like} C / {feels_like_f} F")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} km/h")
    print("-" * 30)


while True:
    city = input("Enter city name or 'quit' to stop: ").strip()

    if city == "":
        print("Please enter a city name.")
        continue

    if city.lower() == "quit":
        print("OK, Goodbye!")
        break

    show_weather(city)

