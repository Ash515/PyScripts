import pyautogui
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def takeScreenshot ():
    
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:\Users\Ron\Desktop\Test\screenshot2.png')

myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='green',fg='white',font= 10)
canvas1.create_window(150, 150, window=myButton)

root.mainloop()
