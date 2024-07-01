import platform
import os

global clearCommand

if platform.system() == "Windows":
    clearCommand = "cls"
    
else:
    clearCommand = "clear"    