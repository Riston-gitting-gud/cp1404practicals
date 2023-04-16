# Hex Colours


COLOUR_AND_CODE = {"Aliceblue": "#0048ba", "Antiquewhite": "#faebd7", "Aqua": "#00ffff", "Bistre": "#3d2b1f",
                   "Black": "#000000", "Carmine": "#960018", "Fulvous": "#e48400", "Goldenrod1": "ffc125",
                   "Indigo": "4b0082", "Magenta3": "cd00cd"}

colour_name = input("Enter a colour name: ").title()
while colour_name != "":
    print(f"The code for {colour_name} is {COLOUR_AND_CODE.get(colour_name)}")
    colour_name = input("Enter a colour name: ").title()



