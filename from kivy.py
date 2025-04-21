from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class TareasApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.input = TextInput(hint_text="Escribe una tarea", size_hint_y=0.1)
        self.boton = Button(text="Agregar tarea", size_hint_y=0.1)
        self.boton.bind(on_press=self.agregar_tarea)

        self.scroll = ScrollView()
        self.lista = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.lista.bind(minimum_height=self.lista.setter('height'))
        self.scroll.add_widget(self.lista)

        self.add_widget(self.input)
        self.add_widget(self.boton)
        self.add_widget(self.scroll)

    def agregar_tarea(self, instance):
        tarea = self.input.text.strip()
        if tarea:
            etiqueta = Label(text=tarea, size_hint_y=None, height=40)
            self.lista.add_widget(etiqueta)
            self.input.text = ""

class MiApp(App):
    def build(self):
        return TareasApp()

MiApp().run()