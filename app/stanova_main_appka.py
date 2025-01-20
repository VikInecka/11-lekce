# Importing all app imports
from stanova_config_appka import *

# Main Window Functions
def neco(weight, activityfactor):    
    bmr=weight*24.2
    cml=bmr*activityfactor
    cmlrounded= round(cml, 1)
    return cmlrounded

def zivot_ty(jaky_vek):
    if jaky_vek == "100 a více":
        penize= "Dostavas pocatecni bonus 100 kč"
    else: 
        penize= "Nemas nic si moc mlady :C"
    return penize
    
def zena(tve_pohl):
    if tve_pohl == "ONA":
        pohlav= "Ahoj ženo"
    elif tve_pohl == "ON":
        pohlav = "Ahoj muži"
    else:
        pohlav= "Ahoj osobo"
    return pohlav





# Main Window Variables
todays_date_str = dt.date.today().strftime("%d-%m-%Y") #this is a string
todays_date_obj = dt.date.today() #this is an object

# Main Window Lists / Dictionaries

