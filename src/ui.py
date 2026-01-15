from kivy.config import Config
Config.set('graphics', 'width', '360')   
Config.set('graphics', 'height', '540')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.core.text import LabelBase

LabelBase.register(
    name="Meitei",
    fn_regular="fonts/NotoSansMeeteiMayek-Medium.ttf"
)
Builder.load_file("src/ui.kv")

weather_data = {
    "today": {
        "tempMax": 32,
        "tempMin": 28,
        "rain": 150,
        "humidity": 65,
        "wind_speed": 14
    },
    "tomorrow": {
        "tempMax": 30,
        "tempMin": 25,
        "rain": 120,
        "humidity": 58,
        "wind_speed": 10
    },
    "day_after": {
        "tempMax": 29,
        "tempMin": 24,
        "rain": 134,
        "humidity": 70,
        "wind_speed": 18
    }
}

class WeatherUI(BoxLayout):
    today_tempMax = NumericProperty(0)
    today_tempMin = NumericProperty(0)
    tomorrow_tempMax = NumericProperty(0)
    tomorrow_tempMin = NumericProperty(0)
    day_after_tempMax = NumericProperty(0)
    day_after_tempMin = NumericProperty(0)
    # change this for integer
    today_rain = NumericProperty(0)
    tomorrow_rain = NumericProperty(0)
    day_after_rain = NumericProperty(0)

    lang = StringProperty("en")

    translations = {
        "en": {
            "title": "Sangai Weather",
            "forecast": "Weather Forecast",
            "today": "TODAY",
            "temp": "Temperature",
            "rain": "Rainfall",
            "more": "More Info"
        },
        "mni": {    
            "title": "ꯁꯥꯡꯒꯥꯏ ꯋꯦꯗꯔ",
            "forecast": "ꯋꯦꯗꯔ ꯐꯣꯔꯀꯥꯁ꯭ꯇ",
            "today": "ꯅꯨꯡꯁꯤ",
            "temp": "ꯍꯤꯟꯅꯩ",
            "rain": "ꯂꯩꯔꯥꯟ",
            "more": "ꯍꯣꯠꯅ ꯑꯃꯇ"
        }
    }

    def t(self, key):
        return self.translations[self.lang][key]

    def switch_lang(self):
        self.lang = "mni" if self.lang == "en" else "en"

    def get_data(self):
        return weather_data
    
    def set_data(self):
        self.today_tempMax = self.get_data()["today"]["tempMax"]
        self.today_tempMin = self.get_data()["today"]["tempMin"]
        self.today_rain = self.get_data()["today"]["rain"]
    
    
    def send_location(self):
        pass


    def show_details(self, day):
        

        text = (
            f"Humidity: {self.get_data()[day]['humidity']}%\n"
            f"Wind Speed: {self.get_data()[day]['wind_speed']} km/h\n"
        )

        Popup(
            title="Weather Details",
            content=Label(text=text),
            size_hint=(.8,.4)
        ).open()


class WeatherApp(App):
    def build(self):
        return WeatherUI()
    def on_start(self):
        self.root.set_data()


if __name__ == "__main__":
    WeatherApp().run()
