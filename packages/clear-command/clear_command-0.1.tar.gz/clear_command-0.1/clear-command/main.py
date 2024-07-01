import platform
import os

def setClearCommand():
    global clearCommand

    if platform.system() == "Linux" or platform.system() == "Darwin":
        clearCommand = "clear"

    elif platform.system() == "Windows":
        clearCommand = "cls"
    
    else:
        clearCommand = "clear"    