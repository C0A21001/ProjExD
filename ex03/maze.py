import tkinter as tk
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = " "

def main_proc():
    global cx,cy
    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Left":
        cx -=20
    elif key == "Right":
        cx += 20
    canvas.coords("tori",cx,cy)
    root.after(10, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(width = "1500",height = "900",bg = "black")
    canvas.pack()
    key = " "
    cx,cy = 300,400
    image = tk.PhotoImage(file = "fig/8.png")
    canvas.create_image(cx,cy,image = image,tag = "tori")
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()