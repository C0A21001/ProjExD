import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    if entry.get() == "0":
        entry.delete(0,tk.END)
    btn = event.widget
    txt = btn["text"]
    if txt == "+":
        entry.insert(tk.END,"+")
    elif txt == "=":
        ans = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
    elif txt == "-":
        entry.insert(tk.END,"-")
    elif txt == "×":
        entry.insert(tk.END,"*")
    elif txt == "÷":
        entry.insert(tk.END,"/")
    elif txt == "c":
        entry.delete(0,tk.END)
        entry.insert(tk.END,"0")
    elif txt == "x²":
        nom = eval(entry.get())
        entry.delete(0,tk.END)
        ans = nom**2
        entry.insert(tk.END,ans)
    elif txt == "±":
        nom = eval(entry.get())
        entry.delete(0,tk.END)
        ans = -1*nom
        entry.insert(tk.END,ans)
    else:
        entry.insert(tk.END,f"{txt}")

root = tk.Tk()
root.title("電卓")
root.geometry("290x500")
entry = tk.Entry(justify="right",width = 10,font=("",40))
entry.insert(tk.END,"0")
entry.grid(columnspan = 4)
r = 225
c = 0
for i in range(9,-1,-1):
    button = tk.Button(root,text=f'{i}',font=("",30),width=3,height=1)
    button.bind("<1>", button_click)
    button.place(x=c, y = r)
    c+=73
    if c%3 == 0:
        r+=70
        c=0
button = tk.Button(root,text="+",font=("",30),width=3,height=1)
button.place(x=219,y=365)
button.bind("<1>", button_click)
button = tk.Button(root,text="=",font=("",30),width=3,height=1)
button.place(x=219,y=435)
button.bind("<1>", button_click)
button = tk.Button(root,text="-",font=("",30),width=3,height=1)
button.place(x=219,y=295)
button.bind("<1>", button_click)
button = tk.Button(root,text="×",font=("",30),width=3,height=1)
button.place(x=219,y=225)
button.bind("<1>", button_click)
button = tk.Button(root,text="÷",font=("",30),width=3,height=1)
button.place(x=219,y=155)
button.bind("<1>", button_click)
button = tk.Button(root,text="c",font=("",30),width=3,height=1)
button.place(x=0,y=155)
button.bind("<1>", button_click)
button = tk.Button(root,text=".",font=("",30),width=3,height=1)
button.place(x=73,y=435)
button.bind("<1>", button_click)
button = tk.Button(root,text="x²",font=("",30),width=3,height=1)
button.place(x=73,y=155)
button.bind("<1>", button_click)
button = tk.Button(root,text="±",font=("",30),width=3,height=1)
button.place(x=146,y=435)
button.bind("<1>", button_click)
root.mainloop()