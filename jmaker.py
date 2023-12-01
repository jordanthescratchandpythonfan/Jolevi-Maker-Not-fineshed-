import tkinter as tk
from tkinter import messagebox
import platform
import sys
import os

if platform.system() == "Windows":
    messagebox.showerror("Oh shoot!", "We see your on windows and this might not work, Becuase it might not go to the right dir's as it should")
elif  platform.system() == "Linux":
    messagebox.showerror("Oh shoot!", "This window is not useful so you can skip")
elif  platform.system() == "Darwin":
   message.showerror("Oh shoot!", "IThis wont work go on a different os")
   sys.exit()


def JM_MP():
    MPW = tk.Tk()
    MPW.title("Make the project")
    MPW.geometry("200x200")
    MPW.resizable(False, False)
    tk.Label(MPW, text="Make a project").pack()
    JM_E_N = tk.Entry(MPW).pack()
    tk.Button(MPW, text="Make the project").pack()
    MPW.mainloop()


app = tk.Tk()
app.title("Jolevi Maker")
app.geometry("400x400")
app.resizable(False, False)

tk.Label(app, text="Jolevi Maker Dashbard").pack()
tk.Button(app, text="Make a project", command=JM_MP).pack()
tk.Button(app, text="Open project").pack()

app.mainloop()
