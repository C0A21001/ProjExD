import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"{txt}のボタンがクリックされました")

root = tk.Tk()
root.title("")
root.geometry("300x500")
entry = tk.Entry(justify="right",width = 10,font=("",40))
entry.insert(tk.END,"")
entry.grid(columnspan = 4)
r = 1
c = 0
for i in range(9,-1,-1):
    button = tk.Button(root,text=f'{i}',font=("",30),width=4,height=2)
    button.bind("<1>", button_click)
    button.grid(row=r, column = c)
    c+=1
    if c%3 == 0:
        r+=1
        c=0
root.mainloop()