# Dynamic Labels

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.name_to_label = ['johnny joestar', 'joseph joestar', 'jotaro joestar']

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create buttons from data and add them to the GUI"""
        for name in self.name_to_label:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
