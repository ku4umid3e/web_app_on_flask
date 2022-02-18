import requests
import os


def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": os.getenv("KEY"),
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lung": "ru"
            }
    try:
        result = requests.get(weather_url, params=params)
        weather = result.json()
        if "data" in weather:
            print("if ok")
            if "current_condition" in weather["data"]:
                print("if two ok")
                try:
                    print("try ok")
                    return weather["data"]["current_condition"][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False
    return False


if __name__ == "__main__":
    print(weather_by_city("st petersburg, russia"))
