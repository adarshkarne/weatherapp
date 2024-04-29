import requests 
from tkinter import *
from tkinter import messagebox 

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        
        self.app = Tk()
        self.app.title("Weather App")
        self.app.geometry("300x200")
        
        self.create_widgets()

    def create_widgets(self):
        self.city_entry = Entry(self.app, width=30)
        self.city_entry.pack(pady=10)

        self.search_btn = Button(self.app, text="Search Weather", width=15, command=self.search)
        self.search_btn.pack()

        self.location_lbl = Label(self.app, text="Location", font=('Helvetica', 20))
        self.location_lbl.pack(pady=5)

        self.temperature_lbl = Label(self.app, text="", font=('Helvetica', 14))
        self.temperature_lbl.pack()

        self.weather_lbl = Label(self.app, text="", font=('Helvetica', 14))
        self.weather_lbl.pack()

    def get_weather(self, city):
        result = requests.get(self.url.format(city, self.api_key))
        if result.status_code == 200:
            data = result.json()
            city_name = data['name']
            country = data['sys']['country']
            temp_kelvin = data['main']['temp']
            temp_celsius = temp_kelvin - 273.15
            weather = data['weather'][0]['main']
            return city_name, country, temp_celsius, weather
        else:
            return None

    def search(self):
        city = self.city_entry.get()
        weather_info = self.get_weather(city)
        if weather_info:
            city_name, country, temp_celsius, weather = weather_info
            self.location_lbl.config(text="{}, {}".format(city_name, country))
            self.temperature_lbl.config(text="{:.1f}°C".format(temp_celsius))
            self.weather_lbl.config(text=weather)
        else:
            messagebox.showerror('Error', "Cannot find {}".format(city))

if __name__ == "__main__":
    api_key = "b20946bc33844363394cf938006f2b23"
    weather_app = WeatherApp(api_key)
    weather_app.app.mainloop()
