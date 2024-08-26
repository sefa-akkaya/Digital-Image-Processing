from tkinter import Tk
from tkinter.filedialog import askopenfilename

def foto_yukle():
    Tk().withdraw()  
    filename = askopenfilename()
    return filename
