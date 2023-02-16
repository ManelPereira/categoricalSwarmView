
import tkinter as tk
from engine import BaseEngine
#from category import Category
#from particle import Particle
center = (600,600)


def restart(canvas):
    canvas.delete("all")
    center = (int(canvas.cget("width"))/2,int(canvas.cget("height"))/2)
    config = {'radius':200, 'center':center}
    en = BaseEngine(90,categories,config,canvas)
    en.update()
    return True
categories = {}

for i in range(12):
    categories[f"Category {i}"] = 1/12

en = "sgt"
def main():

    # Tkinter Window
    root_window = tk.Tk()

    # Window Settings
    root_window.title('Application Title')
    root_window.geometry('1900x1080')
    root_window.configure(background = '#353535')
    #create 12 categories



    canvas = tk.Canvas(root_window, height=700, width=700, bg='#fefefe')
    canvas.pack(side=tk.TOP)
    center = (int(canvas.cget("width"))/2,int(canvas.cget("height"))/2)

    config = {'radius':200, 'center':center}
    en = BaseEngine(90,categories,{'radius':200, 'center':center},canvas)
    en.speed(1)
    #create a circle with 200 radius
    canvas.create_oval(center[0]-config["radius"],center[1]-config["radius"],center[0]+config["radius"],center[1]+config["radius"])
    
    # Text
    tk.Label(root_window, text='Hello World', fg='White', bg='#353535').pack()

    tk.Button(root_window, text='Start', width=10, command=lambda: restart(canvas)).pack(side=tk.BOTTOM)
    

    # Exit Button
    tk.Button(root_window, text='Exit', width=10, command=root_window.destroy).pack(side=tk.BOTTOM)
    en.update()
    #en.move_all_to()
    # Main loop
    root_window.mainloop()

if __name__ == '__main__':
    main()

