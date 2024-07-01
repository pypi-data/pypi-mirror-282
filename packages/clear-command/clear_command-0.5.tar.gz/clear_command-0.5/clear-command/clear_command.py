import platform

def clearCommand():
    if platform.system() == "Windows":
        return "cls"
    else:
        return "clear"
