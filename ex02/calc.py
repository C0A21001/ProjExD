import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    #tkm.showinfo(txt,f"{txt}のボタンがクリックされました")
    if txt == "+":
        entry.insert(tk.END,"+")
    elif txt == "=":
        ans = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)

    else:
        entry.insert(tk.END,f"{txt}")

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
button = tk.Button(root,text="+",font=("",30),width=4,height=2)
button.grid(row=4,column=1)
button.bind("<1>", button_click)
button = tk.Button(root,text="=",font=("",30),width=4,height=2)
button.grid(row=4,column=2)
button.bind("<1>", button_click)
root.mainloop()