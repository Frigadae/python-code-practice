import tkinter
import os

def main():
    window = tkinter.Tk()
    window.title('tkinter Window')
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    windowWidth = 400
    windowHeight = 300
    window.geometry(str(windowWidth) + "x" + str(windowHeight) + "+" + str((screenWidth//2)-windowWidth//2) + "+" + str((screenHeight//2)-windowHeight//2))
    window.mainloop()

main()