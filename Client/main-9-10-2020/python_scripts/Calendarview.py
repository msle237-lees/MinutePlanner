import os
from kivy.app import App
from kivy.lang import Builder
from KivyCalendar import CalendarWidget

class Calendarview(App):
    def build(self):
        return Builder.load_file(
        os.path.join(dirname(__file__), '../KV_Files/calendarview.kv')
    )
