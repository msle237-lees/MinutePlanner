from kivy.app import App
from kivy.lang import Builder


class Alltime(App):
    def build(self):
        return Builder.load_file(
        os.path.join(dirname(__file__), '../KV_Files/alltime.kv')
    )
