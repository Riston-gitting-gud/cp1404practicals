# Modify Existing GUI Program

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build the BoxLayout  App"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greeting button press, updates text of name input to username and greets user"""
        print('greet')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def press_clear(self):
        """Clear name input text"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()


