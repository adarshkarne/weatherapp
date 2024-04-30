import requests
from flask import Flask, render_template, request

app = Flask(__name__)

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    def get_weather(self, city):
        result = requests.get(self.url.format(city, self.api_key))
        if result.status_code == 200:
            print(result.json())
            data = result.json()
            city_name = data['name']
            country = data['sys']['country']
            temp_kelvin = data['main']['temp']
            temp_celsius = temp_kelvin - 273.15
            weather = data['weather'][0]['main']
            return city_name, country, temp_celsius, weather
        else:
            return None

weather_app = WeatherApp(api_key="b20946bc33844363394cf938006f2b23")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_info = weather_app.get_weather(city)
        if weather_info:
            city_name, country, temp_celsius, weather = weather_info
            return render_template('index.html', city=city_name, country=country, temp=temp_celsius, weather=weather)
        else:
            return render_template('index.html', error="Cannot find {}".format(city))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
