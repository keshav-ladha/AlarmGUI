import tkinter as tk
from tkinter import ttk ,messagebox
import time, os

#basic configuration
root = tk.Tk()
root.title("")
root.geometry("480x240")
root.config(background="grey")
root.iconbitmap("K.ico")


def submit():
    # print(f"Time Set To {time_entry.get()} and Reminder set as {msg_entry.get()}")
    alarm_time = time_entry.get()
    a = msg_.get()
    print(a)
    root.destroy()
    while True:
        current_time = time.strftime("%H:%M")
        if alarm_time == current_time:
            os.startfile('ringtone.mp3')
            print("-"*60)
            print("REMINDER")
            print("OF")
            print(f"{a}")
            print("-"*60)
            break

#text Boxes and Frames
f = tk.Frame(root, bg="gray", height=20, width=20)     #a small box of gray color that separates the boxes
f.pack(side=tk.TOP)

f1 = tk.Frame(root, bg="white")       #frame in which time entry text box resides
f1.pack(side=tk.TOP)

time_user = tk.StringVar()      #string variable for time 
time_user.set('')               #setting the value to Null to get a clean interface in GUI

#ttk.Entry Boxes are modern Entry Boxes
time_entry = ttk.Entry(f1, justify =tk.CENTER, textvariable = time_user, font=('Microsoft Yahei Light' , 40))
time_entry.pack(side=tk.TOP)

f = tk.Frame(root, bg="gray", height=20, width=20)#same frame to create a gap
f.pack(side=tk.TOP)

f2 = tk.Frame(root, bg="white") #frame in which we set the time message
f2.pack(side=tk.TOP)

message = tk.StringVar()           #user reminder message variable

#same ttk.Entry Boxes
msg_ = ttk.Entry(f2, justify =tk.CENTER, textvariable =message, font=('Microsoft Yahei Light' , 40))
msg_.pack()

#frame to separate the boxes 
f = tk.Frame(root, bg="gray", height=20, width=20)
f.pack(side=tk.TOP)

#frame that consists of button to submit
button_frame = tk.Frame(root, bg="white", height=20, width=20)
button_frame.pack(side=tk.TOP)

#Submit Button
btn = ttk.Button(button_frame, text = 'Submit', command =submit)
btn.pack()

root.mainloop()