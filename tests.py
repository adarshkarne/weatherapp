import unittest
from weatherapp import WeatherApp

class TestWeatherApp(unittest.TestCase):
    def setUp(self):
        self.api_key = "b20946bc33844363394cf938006f2b23"
        self.weather_app = WeatherApp(self.api_key)

    def test_get_weather_valid_city(self):
        cities = ["London", "New York", "Tokyo", "Paris", "Sydney", "Berlin", "Moscow", "Dubai", "Rome", "Toronto", "Beijing", "Los Angeles", "Cairo", "Rio de Janeiro", "Mumbai"]
        for city in cities:
            with self.subTest(city=city):
                weather_info = self.weather_app.get_weather(city)
                self.assertIsNotNone(weather_info)
                self.assertEqual(len(weather_info), 4)
                self.assertIsInstance(weather_info[0], str)  # city name
                self.assertIsInstance(weather_info[1], str)  # country code
                self.assertIsInstance(weather_info[2], float)  # temperature
                self.assertIsInstance(weather_info[3], str)  # weather description

    def test_get_weather_invalid_city(self):
        invalid_cities = ["InvalidCityName1", "InvalidCityName2", "InvalidCityName3"]
        for city in invalid_cities:
            with self.subTest(city=city):
                weather_info = self.weather_app.get_weather(city)
                self.assertIsNone(weather_info)

if __name__ == "__main__":
    unittest.main()
