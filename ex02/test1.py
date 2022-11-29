import tkinter as tk
import tkinter.messagebox as tkm
root = tk.Tk()
root.title("おためしか")
root.geometry("500x200")

def button_click():
    tkm.showwarning("警告","ボタン押したらあかん")

label =  tk.Label(root,
                    text = "ラベルを書いてみた件",
                    font = ("",20)
                    )
label.pack()

button = tk.Button(root, text = "押すな",command=button_click)
button.pack()

entry = tk.Entry(width=30)
entry.insert(tk.END, "fugapiyo")
entry.pack()

root.mainloop()
