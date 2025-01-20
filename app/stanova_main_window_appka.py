### GUI imports
from guizero import *
from stanova_main_appka import *

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
    
def dary_ty():
    vek= combo.value
    nic= zivot_ty(vek)
    text_4.value = nic

def pohlavi():
    po= choice.value
    nicc= zena(po)
    text_5.value = nicc  
    

### GUI App
app = App(layout="auto", title ="My App", width= 775, height= 650 )
text_1 = Text(app, text="Vítáme vás na nejlepší stránce na světě")
text_2 = Text (app, text="Nejdříve zadejte pohlaví")
choice = ButtonGroup(app, options=["ON", "ONA", "Jiné"])
text_3 = Text(app, text="A váš věk?")
combo = Combo(app, options=["60-70", "70-95", "100 a více"], command = dary_ty )
text_4 = Text(app)
text_5 = Text(app)


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

