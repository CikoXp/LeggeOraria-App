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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ids.topbar.type_height = "large"

    def cls_and_clean(self):
        self.ids.mru_distance.text = "0"
        self.ids.mru_i_distance.text = "0"
        self.ids.mru_speed.text = "0"
        self.ids.mru_time.text = "0"
        self.ids.mru_i_time.text = "0"
        self.ids.mrua_acceleration.text = "0"
        self.ids.mrua_i_speed.text = "0"
        self.ids.mrua_f_speed.text = "0"
        self.ids.mrua_f_time.text = "0"
        self.dial.dismiss()
        self.dial = None
    
    def dial_call(self, res):
        sound = SoundLoader.load('./src/audios/click-on.wav')
        if not self.dial:
            self.dial = MDDialog(
            auto_dismiss=False,
            size_hint_x=(.8),
            title='Result:',
            text="Your unknown value is: %s" % (res),
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: self.cls_and_clean()
                ),
            ],
        )
        self.dial.open()
        sound.play()

    def do_mru_math(self, s, si, v, t, ti):
        if s == "0":
            res = MRU().mru_s(float(si), float(v), float(t), float(ti))
        elif v == "0":
            res = MRU().mru_v(float(s), float(si), float(t), float(ti))
        elif t == "0":
            res = MRU().mru_t(float(s), float(si), float(v), float(ti))
        else:
            res = "Insufficient or incorrect data!"
        return self.dial_call(res)
    
    def do_mrua_math(self, a, s, si, v, vi, vf, t, ti, ts):
        print(a, s, si, v, vi, vf, t, ti, ts)
        res = "Function works good!"
        return self.dial_call(res)

class LeggeOrariaApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        return MS()

if __name__ == '__main__':
    LeggeOrariaApp().run()
