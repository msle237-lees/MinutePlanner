import os
from kivy.app import App
from kivy.lang import Builder


class Dropdown(App):
    def build(self):
        return Builder.load_file(
        os.path.join(dirname(__file__), '../KV_Files/dropdown.kv')
    )
