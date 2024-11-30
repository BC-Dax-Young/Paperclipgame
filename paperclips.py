import tkinter as tk
from time import *
import random
import math
from tkinter import messagebox 

global paperClips, robots, cash, pcPer, resources, price
paperClips, robots, cash, pcPer, resources, price = 0,0,500,0,0,10


def open_second_window(): 
    global robots, cash, pcPer, resources
    upgradeui = tk.Toplevel(root) 
    upgradeui.title("Upgrade GUI") 
    upgradeui.geometry("300x200") 
    upgradeui.configure(background="#1f1f1f")
    upgradeui.resizable(False,False)

    labelbuyrobot=tk.Label(upgradeui, text="Buy Robot $150: ", font= "helvetica", bg="#1f1f1f", fg="white", justify="left")
    buyrobot=tk.Button(upgradeui, text="Purchase", font= "helvetica", bg="#2f2f2f", fg="white", width=10,relief="flat", command=buyrobots)



    widgets=[
        (labelbuyrobot, 0, 0),
        (buyrobot, 0, 1)
        ]


    for widget, row, column, in widgets:
        widget.grid(row=row, column=column, padx=10, pady=10, sticky="w")


def updatestats():
    global paperClips, robots, cash, pcPer, resources, price
    stats=[
        (displaypc, paperClips, ""),
        (displayrobots, robots, ""),
        (displaycash, cash, "$"),
        (displaypcper, pcPer, ""),
        (displayres, resources, ""),
        (displayprice, price, "$")
        ]

    for widget, statistic, extra in stats:
        widget.configure(state="normal")
        widget.delete(0, tk.END)
        widget.insert(0, extra + str(statistic))
        widget.configure(state="disabled")

def sell():
    global paperClips, cash, price
    if paperClips >= 1:
        cash+=(paperClips*10)
        paperClips-=paperClips
        
    else:
        messagebox.showerror("Warning", "No Paper Clips to sell")
    updatestats()
    
def buyresource():
    global cash, resources
    if cash >= 1:
        cash-=100
        resources+=10
    else:
        messagebox.showerror("Warning", "You have no money!")
    updatestats()

def makepaperclip():
    global resources, paperClips, pcPer
    if resources >= 1:
        resources-=1
        paperClips+=10*pcPer
    else:
        messagebox.showerror("Warning", "No Resources available")
    updatestats()
    
def buyrobots():
    global cash, robots
    if cash >= 150:
        cash-=150
        robots+=1
    else:
        messagebox.showerror("Warning", "Not enough Cash available")
    updatestats()

def buyrobot():
    global cash, pcPer
    if cash >= 20:
        cash-=20
        pcPer+=1
    else:
        messagebox.showerror("Warning", "No Cash available")
    updatestats()

def priceinc():
    pass


def createlabel(parent, text):
    return tk.Label(parent, text=text, font="Helvetica", bg="#2f2f2f", fg="white", relief="flat")

root=tk.Tk()
root.title("Paper Clip Game")
root.configure(background="#2f2f2f")
root.resizable(False,False)
root.geometry("700x400")
canvas = tk.Canvas(root, width=700, height=400, bg="#2f2f2f", highlightthickness=0)
canvas.grid(columnspan=100, rowspan=100)
canvas.create_rectangle(350, 400, 700, 0, fill="#1f1f1f", outline="")

labelcurrentpc=createlabel(root, "Current Paper Clips: ")
displaypc=tk.Entry(root, relief="flat", font= "helvetica", bg="#1f1f1f", fg="white", width=12, disabledbackground="#1f1f1f", disabledforeground="white")
displaypc.configure(state="disabled")

labelrobots=createlabel(root, "Current Robots: ")
displayrobots=tk.Entry(root, relief="flat", font= "helvetica", bg="#1f1f1f", fg="white", width=12, disabledbackground="#1f1f1f", disabledforeground="white")
displayrobots.configure(state="disabled")

labelcash=createlabel(root, "Current Cash: ")
displaycash=tk.Entry(root, relief="flat", font= "helvetica", bg="#1f1f1f", fg="white", width=12, disabledbackground="#1f1f1f", disabledforeground="white")
displaycash.configure(state="disabled")

labelpcper=createlabel(root, "Current Efficiency: ")
displaypcper=tk.Entry(root, relief="flat", font= "helvetica", bg="#1f1f1f", fg="white", width=12, disabledbackground="#1f1f1f", disabledforeground="white") 
displaypcper.configure(state="disabled")

labelres=createlabel(root, "Current Resources: ")
displayres=tk.Entry(root, relief="flat", font= "helvetica", bg="#1f1f1f", fg="white", width=12, disabledbackground="#1f1f1f", disabledforeground="white") 
displayres.configure(state="disabled")

labelprice=createlabel(root, "Current Price: ")
displayprice=tk.Entry(root, relief="flat", font= "helvetica", bg="#1f1f1f", fg="white", width=12, disabledbackground="#1f1f1f", disabledforeground="white") 
displayprice.configure(state="disabled")

labelsell=tk.Label(root, text="Sell Paper Clips: ", font= "helvetica", bg="#1f1f1f", fg="white", justify="left")
sellpc=tk.Button(root, text="Sell", font= "helvetica", bg="#2f2f2f", fg="white", width=10, relief="flat", command=sell)

labelupg=tk.Label(root, text="Buy Upgrades: ", font= "helvetica", bg="#1f1f1f", fg="white", justify="left")
openupg=tk.Button(root, text="Upgrade", font= "helvetica", bg="#2f2f2f", fg="white", width=10,relief="flat", command=open_second_window)

labelmake=tk.Label(root, text="Make Paper Clip: ", font= "helvetica", bg="#1f1f1f", fg="white", justify="left")
makepc=tk.Button(root, text="Construct", font= "helvetica", bg="#2f2f2f", fg="white", width=10,relief="flat", command=makepaperclip)

labelbuy=tk.Label(root, text="Buy Resources: ", font= "helvetica", bg="#1f1f1f", fg="white", justify="left")
buyres=tk.Button(root, text="Purchase", font= "helvetica", bg="#2f2f2f", fg="white", width=10,relief="flat", command=buyresource)

spacer=tk.Label(root, text="", bg="#2f2f2f")

widgets=[
    (labelcurrentpc, 0, 0),
    (displaypc, 0, 1),
    (labelrobots, 1, 0),
    (displayrobots, 1, 1),
    (labelcash, 2, 0),
    (displaycash, 2, 1),
    (labelpcper, 3, 0),
    (displaypcper, 3, 1),
    (labelsell, 0, 3),
    (sellpc, 0, 4),
    (labelupg, 1, 3),
    (openupg, 1, 4),
    (labelmake, 2, 3),
    (makepc, 2, 4),
    (labelres, 4, 0),
    (displayres, 4, 1),
    (labelbuy, 3, 3),
    (buyres, 3, 4),
    (displayprice, 5, 1),
    (labelprice, 5, 0),
]

for widget, row, column, in widgets:
    widget.grid(row=row, column=column, padx=10, pady=10, sticky="w")

spacer.grid(row=0, column=2, padx=30, pady=10)
root.grid_rowconfigure(1, minsize=20)
updatestats()
root.mainloop()
