import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = " "

def main_proc():
    global mx,my#移動キーを変更
    if key == "w":
        my -= 1
    elif key == "s":
        my += 1
    elif key == "a":
        mx -= 1
    elif key == "d":
        mx += 1
    if maze_lst[mx][my] == 1:
        if key == "w":
            my += 1
        elif key == "s":
            my -= 1
        elif key == "a":
            mx += 1
        elif key == "d":
            mx -= 1
    cx,cy = mx*100+50,my*100+50
    canvas.coords("tori",cx,cy)
    if mx == 13 and my == 7:
        tkm.showinfo("クリア","ゴール！")#ゴール時に表示
        mx = 1
        my = 1
        cx,cy = mx*100+50,my*100+50
        canvas.coords("tori",cx,cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(width = "1500",height = "900",bg = "black")
    canvas.pack()
    maze_lst = mm.make_maze(15,9)
    mm.show_ｓmaze(canvas,maze_lst)
    key = " "
    mx,my = 1,1
    cx,cy = mx*100+50,my*100+50
    image = tk.PhotoImage(file = "fig/8.png")
    canvas.create_image(cx,cy,image = image,tag = "tori")
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()