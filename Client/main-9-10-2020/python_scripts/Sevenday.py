import os
from kivy.app import App
from kivy.lang import Builder


class Sevenday(App):
    def build(self):
        return Builder.load_file(
        os.path.join(dirname(__file__), '../KV_Files/sevenday.kv')
    )
