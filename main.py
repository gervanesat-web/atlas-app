from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Line
import random

# Basit bir "kod yağmuru" efekti için sınıf
class CodeRain(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = []
        self.start_rain()

    def start_rain(self):
        Window.bind(on_resize=self._update_canvas)
        Clock.schedule_interval(self._update_canvas, 0.05)

    def _update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(0, 1, 0.5, 0.3) # Yarı şeffaf turkuaz-yeşil kod rengi
            self.cols = []
            for i in range(0, int(Window.width), 20):
                self.cols.append(i)
            for x in self.cols:
                y = random.randint(0, int(Window.height))
                char_count = random.randint(5, 15)
                for _ in range(char_count):
                    text = "".join([random.choice("01{}[]()<>?+-/*=") for _ in range(3)])
                    Label(text=text, pos=(x, y), font_size=12, color=(0, 1, 0.5, 0.3))
                    y -= 15

# Ana Uygulama Ekranı
class AtlasRoot(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 1. Arka Plan (Kod Yağmuru)
        self.code_rain = CodeRain()
        self.add_widget(self.code_rain)

        # 2. Merkez Gezegen (Animasyonlu Dünya)
        # NOT: Buraya gerçekten dönen bir gif dosyası koymak istersen,
        # 'source' kısmını gif dosyasının adıyla değiştir (örn. 'source': 'earth_spin.gif')
        # Şimdilik mavi bir daireyi simülasyon olarak kullanıyoruz.
        self.earth = Image(
            source='https://upload.wikimedia.org/wikipedia/commons/2/2c/Rotating_earth_%28large%29.gif', # Canlı gif örneği
            size_hint=(0.6, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(self.earth)

        # 3. Üst Bilgi Etiketi
        self.label = Label(
            text='[color=00FFFF]ATLAS[/color] | Sistem Aktif',
            markup=True,
            font_size=32,
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            color=(1, 1, 1, 1)
        )
        self.add_widget(self.label)

        # 4. Kontrol Düğmesi (Şeffaf ve Gölgeli)
        self.action_button = Button(
            text='Komut Ver',
            font_size=24,
            size_hint=(0.8, 0.15),
            pos_hint={'center_x': 0.5, 'center_y': 0.15},
            background_color=(0, 0.7, 0.7, 0.4), # Yarı şeffaf turkuaz düğme
            background_normal='',
            border=(10, 10, 10, 10),
            color=(0, 1, 1, 1)
        )
        self.action_button.bind(on_press=self.on_button_click)
        self.add_widget(self.action_button)

        # 5. Dinleme Durumu Etiketi
        self.status_label = Label(
            text='Gezegen taranıyor...',
            font_size=16,
            pos_hint={'center_x': 0.5, 'center_y': 0.75},
            color=(0.5, 1, 1, 0.7)
        )
        self.add_widget(self.status_label)

    def on_button_click(self, instance):
        self.status_label.text = 'Ses dinleniyor...'

class AtlasApp(App):
    def build(self):
        return AtlasRoot()

if __name__ == '__main__':
    AtlasApp().run()
