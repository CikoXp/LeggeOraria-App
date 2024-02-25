from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.audio import SoundLoader
from src.pkgs.mru_math import MRU

from kivy.core.window import Window
Window.size = (400, 700)

class MS(MDScreen):
    dial = None

    def cls_and_clean(self):
        self.ids.distance.text = "0"
        self.ids.speed.text = "0"
        self.ids.time.text = "0"
        self.ids.i_distance.text = "0"
        self.ids.i_time.text = "0"
        self.dial.dismiss()
        self.dial = None

    def do_math(self, s, v, t, si, ti):
        res = 0
        sound = SoundLoader.load('./src/audios/click-on.wav')
        if s == "0" and v == "0" or s == "0" and t == "0" or v == "0" and t == "0":
            print("No more than one value can be unknown!")
        elif s == "0" and v != "0" and t != "0":
            res = MRU().mru_s(float(v), float(t), float(si), float(ti))
        elif s != "0" and v == "0" and t != "0":
            res = MRU().mru_v(float(s), float(t), float(si), float(ti))
        elif s != "0" and v != "0" and t == "0":
            res = MRU().mru_t(float(s), float(v), float(si), float(ti))
        if not self.dial:
            self.dial = MDDialog(
            auto_dismiss=False,
            size_hint_x=(.8),
            title='Result:',
            text="Your unknown value is: %s" % (res),
            buttons=[
                MDFlatButton(
                    text="OK",
                    # theme_text_color="Custom",
                    # text_color=MDApp().theme_cls.primary_color,
                    on_release=lambda x: self.cls_and_clean()
                ),
            ],
        )
        self.dial.open()
        sound.play()


class LeggeOrariaApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        return MS()

if __name__ == '__main__':
    LeggeOrariaApp().run()
