import os
from kivy.app import App
from kivy.lang import Builder


class TodayList(App):
    def build(self):
        return Builder.load_file(
        os.path.join(dirname(__file__), '../KV_Files/todaylist.kv')
    )
