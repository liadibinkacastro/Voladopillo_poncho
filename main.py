import os, math, random
from PIL import Image as PilImage
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.core.window import Window

Window.clearcolor = (0x30/255, 0x27/255, 0x02/255, 1)

def ruta_recurso(nombre):
    base = os.path.dirname(os.path.abspath(__file__))
    for ext in [".png", ".jpg", ".jpeg", ""]:
        ruta = os.path.join(base, nombre + ext)
        if os.path.exists(ruta):
            return ruta
    return os.path.join(base, nombre + ".png")

def quitar_negro(img):
    img = img.convert("RGBA")
    datos = []
    for r,g,b,a in img.getdata():
        if r < 35 and g < 35 and b < 35:
            datos.append((0,0,0,0))
        else:
            datos.append((r,g,b,a))
    img.putdata(datos)
    return img

def pil_a_textura(pil_img):
    pil_img = pil_img.convert("RGBA")
    w,h = pil_img.size
    tex = Texture.create(size=(w,h), colorfmt='rgba')
    tex.blit_buffer(pil_img.tobytes(), colorfmt='rgba', bufferfmt='ubyte')
    tex.flip_vertical()
    return tex

class PilloApp(App):
    def build(self):
        self.img_cara = quitar_negro(PilImage.open(ruta_recurso("aguila"))).resize((300,300))
        self.img_sello = quitar_negro(PilImage.open(ruta_recurso("sello"))).resize((300,300))

        root = FloatLayout()
        self.moneda = Image(size_hint=(None,None), size=(250,250),
                            pos_hint={'center_x':0.5, 'center_y':0.65})
        root.add_widget(self.moneda)

        self.boton = Button(text="Lanzar Volado",
                            size_hint=(None,None), size=(220,60),
                            pos_hint={'center_x':0.5, 'center_y':0.2},
                            background_normal='', background_color=(0x55/255, 0x1B/255, 0x05/255, 1),
                            font_size=18, bold=True, italic=True)
        self.boton.bind(on_press=lambda x: self.lanzar())
        root.add_widget(self.boton)
        self.lanzar()
        return root

    def lanzar(self):
        self.es_aguila = random.choice([True, False])
        self.angulo = 0
        Clock.unschedule(self.animar)
        Clock.schedule_interval(self.animar, 0.02)

    def animar(self, dt):
        self.angulo += 30
        if self.angulo >= 720:
            Clock.unschedule(self.animar)
            final = self.img_cara if self.es_aguila else self.img_sello
            self.moneda.texture = pil_a_textura(final)
            return
        factor = abs(math.cos(math.radians(self.angulo)))
        base = (self.img_cara if self.es_aguila else self.img_sello) if self.angulo % 180 < 90 else (self.img_sello if self.es_aguila else self.img_cara)
        w,h = base.size
        nuevo_ancho = max(1, int(w * factor))
        temp = base.resize((nuevo_ancho, h))
        final = PilImage.new("RGBA", (w,h), (0,0,0,0))
        final.paste(temp, ((w-nuevo_ancho)//2, 0))
        self.moneda.texture = pil_a_textura(final)

PilloApp().run()
