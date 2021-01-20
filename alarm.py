import tkinter as tk
from tkinter import ttk
import time, os, datetime

#basic configuration
root = tk.Tk()
root.title("")
root.geometry("480x240")
root.config(background="grey")
root.iconbitmap("K.ico")




def submit():
    print(datetime.time.hour)
    print(datetime.time.minute)
    print(time_entry.get())
    print(msg_entry.get())




#text Boxes and Frames
f = tk.Frame(root, bg="gray", height=20, width=20)
f.pack(side=tk.TOP)

f1 = tk.Frame(root, bg="white")
f1.pack(side=tk.TOP)

time = tk.StringVar()
time.set('')

time_entry = ttk.Entry(f1, justify =tk.CENTER, textvariable = time, font=('Microsoft Yahei Light' , 40))
time_entry.pack(side=tk.TOP)


f = tk.Frame(root, bg="gray", height=20, width=20)
f.pack(side=tk.TOP)

f2 = tk.Frame(root, bg="white")
f2.pack(side=tk.TOP)

message = tk.StringVar()

msg_entry = ttk.Entry(f2, justify =tk.CENTER, textvariable =message, font=('Microsoft Yahei Light' , 40))
msg_entry.pack()


f = tk.Frame(root, bg="gray", height=20, width=20)
f.pack(side=tk.TOP)

button_frame = tk.Frame(root, bg="white", height=20, width=20)
button_frame.pack(side=tk.TOP)

btn = ttk.Button(button_frame, text = 'Submit', command =submit)
btn.pack()

root.mainloop()