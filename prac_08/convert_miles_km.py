# Miles to Kilometres Converter

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKmConverter(App):
    """A Kivy App for converting miles to kilometres"""
    km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file"""
        Window.size = (200, 100)
        self.title = "Convert miles to km"
        self.km = '54.71756'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, value):
        """Handle up/down button press, update the text input with new value and call calculation function."""
        current_miles = self.validate_miles()
        updated_miles = current_miles + value
        self.root.ids.input_miles.text = str(updated_miles)
        self.handle_conversion()

    def handle_conversion(self):
        """Handle calculations for miles-to-kilometres conversions"""
        try:
            current_miles = self.validate_miles()
            current_km = current_miles * MILES_TO_KM
            self.root.ids.output_km.text = str(current_km)
        except ValueError:
            pass

    def validate_miles(self):
        """Validate miles entered by checking for error"""
        try:
            current_miles = float(self.root.ids.input_miles.text)
            return current_miles
        except ValueError:
            return 0


MilesToKmConverter().run()
