import platform
import os

global clearCommand

def defineClearCommand():
    if platform.system() == "Windows":
        clearCommand = "cls"
        
    else:
        clearCommand = "clear"    
defineClearCommand()