### GUI imports
from guizero import *
from main import *

### GUI functions
def my_first_gui_function():
    text_welcome.value = "Ahoj můj milý <3"
    try:
        weight=float(txtbox_weight.value)
        activityfactor=float(txtbox_af.value)
        cmlrounded= neco(weight, activityfactor)
        text_cml.value = cmlrounded
        text_cml.value = "Tvůj denní výdaj je:" + cmlrounded
    except ValueError:
        text_cml.value = "Musíš dát číslo"
        return


### GUI App
app = App(title="My App", width=775, height=650)

## Window 1
window1 = Box(app, visible=True)

# Welcome text
text_welcome = Text(window1, text=(f"Ahoj miláčku <3"))

# Input activity factor
text_af = Text(
    window1,
    text=(
        "        Kolik jsi cvičil hodin?"
    )
)
txtbox_af = TextBox(window1)

# Input weight
text_weight = Text(
    window1,
    text=(f"kolik vážíš??? (kg):")
)
txtbox_weight = TextBox(window1)

# Output calorie maintenance level
text_cml = Text(window1, text ="")

# tlačítečko
button = PushButton(window1, command=my_first_gui_function)

# Display an image
image_widget = Picture(
    window1,
    image="resources/images/calculating_cml.png",
    width=680,
    height=480,
    align="bottom"
)

















app.display()

