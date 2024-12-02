import tkinter as tk
from time import *
import random
import math
from tkinter import messagebox 

global paperClips, robots, cash, pcPer, resources, price, pryce, pyrce2, pryce3
paperClips, robots, cash, pcPer, resources, price, pryce, pryce2, pryce3 = 0,0,500,1,0,10, 150, 50, 500

fontSize=13

def robotsfunc():
    global resources, paperClips, pcPer, robots
    if resources >= 1*robots:
        resources-=1*robots
        paperClips+=10*pcPer*robots
    updatestats()
    root.after(1000, robotsfunc)


def open_second_window(): 
    global robots, cash, pcPer, resources,pryce,pryce2
    upgradeui = tk.Toplevel(root) 
    upgradeui.title("Upgrade GUI") 
    upgradeui.geometry("350x200") 
    upgradeui.configure(background="#1f1f1f")
    upgradeui.resizable(False,False)

    def buyrobots():
        global cash, robots, pryce
        if cash >= pryce:
            cash-=pryce
            robots+=1
            pryce+=50
        else:
            messagebox.showerror("Warning", "Not enough Cash available")
        updatestats()
        labelbuyrobot.config(text=f"Buy Robot ${pryce}")
        

    def eff():
        global pcPer, cash,pryce2
        if cash >= pryce2:
            cash-=pryce2
            pcPer+=1
            pryce2+=pryce2*1.5
        else:
            messagebox.showerror("Warning", "Not enough Cash available")
        updatestats()
        labeleff.config(text=f"Increase Efficiency ${int(pryce2)}")
       
    def priceinc():
        global price, cash,pryce3
        if cash >= pryce3:
            cash-=pryce3
            price+=10
            pryce3=pryce3*2
        else:
            messagebox.showerror("Warning", "Not enough Cash available")
        updatestats()
        labelprice.config(text=f"Increase Price ${int(pryce3)}")

    labelbuyrobot=tk.Label(upgradeui, text=f"Buy Robot ${pryce}: ", font= ("helvetica", fontSize), bg="#1f1f1f", fg="white", justify="left")
    buyrobot=tk.Button(upgradeui, text="Purchase", font= ("helvetica", fontSize), bg="#2f2f2f", fg="white", width=10,relief="flat", command=buyrobots)

    labeleff=tk.Label(upgradeui, text=f"Increase Efficiency ${int(pryce2)}: ", font= ("helvetica", fontSize), bg="#1f1f1f", fg="white", justify="left")
    buyeff=tk.Button(upgradeui, text="Purchase", font= ("helvetica", fontSize), bg="#2f2f2f", fg="white", width=10,relief="flat", command=eff)

    labelprice=tk.Label(upgradeui, text=f"Increase Price ${int(pryce3)}: ", font= ("helvetica", fontSize), bg="#1f1f1f", fg="white", justify="left")
    incprice=tk.Button(upgradeui, text="Purchase", font= ("helvetica", fontSize), bg="#2f2f2f", fg="white", width=10,relief="flat", command=priceinc)

    widgets=[
        (labelbuyrobot, 0, 0),
        (buyrobot, 0, 1),
        (labeleff, 1, 0),
        (buyeff, 1, 1),
        (labelprice, 2, 0),
        (incprice, 2, 1)
        ]


    for widget, row, column, in widgets:
        widget.grid(row=row, column=column, padx=10, pady=10, sticky="w")


def updatestats():
    global paperClips, robots, cash, pcPer, resources, price
    stats=[
        (displaypc, paperClips, "", ""),
        (displayrobots, robots, "", ""),
        (displaycash, cash, "$", ""),
        (displaypcper, pcPer*100, "", "%"),
        (displayres, resources, "", ""),
        (displayprice, price, "$", "")
        ]
    print(pcPer)
    for widget, statistic, extra, extra2 in stats:
        widget.configure(state="normal")
        widget.delete(0, tk.END)
        widget.insert(0, extra + str(statistic) + extra2)
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
    if cash >= 100:
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
    

def buyrobot():
    global cash, pcPer
    if cash >= 20:
        cash-=20
        pcPer+=1
        root.update()
    else:
        messagebox.showerror("Warning", "No Cash available")
    updatestats()




def createlabel(parent, text):
    return tk.Label(parent, text=text, font=("helvetica", fontSize), bg="#2f2f2f", fg="white", relief="flat")

root=tk.Tk()
root.title("Paper Clip Game")
root.configure(background="#2f2f2f")
root.resizable(False,False)
root.geometry("700x400")
canvas = tk.Canvas(root, width=700, height=400, bg="#2f2f2f", highlightthickness=0)
canvas.grid(columnspan=100, rowspan=100)
canvas.create_rectangle(350, 400, 700, 0, fill="#1f1f1f", outline="")

labelcurrentpc=createlabel(root, "Current Paper Clips: ")
displaypc=tk.Entry(root, relief="flat", font= ("helvetica", fontSize), bg="#1f1f1f", fg="white", width=12, disabledbackground="#1f1f1f", disabledforeground="white")
displaypc.configure(state="disabled")

labelrobots=createlabel(root, "Current Robots: ")
displayrobots=tk.Entry(root, relief="flat", font= ("helvetica", fontSize), bg="#1f1f1f", fg="white", width=12, disabledbackground="#1f1f1f", disabledforeground="white")
displayrobots.configure(state="disabled")

labelcash=createlabel(root, "Current Cash: ")
displaycash=tk.Entry(root, relief="flat", font= ("helvetica", fontSize), bg="#1f1f1f", fg="white", width=12, disabledbackground="#1f1f1f", disabledforeground="white")
displaycash.configure(state="disabled")

labelpcper=createlabel(root, "Current Efficiency: ")
displaypcper=tk.Entry(root, relief="flat", font= ("helvetica", fontSize), bg="#1f1f1f", fg="white", width=12, disabledbackground="#1f1f1f", disabledforeground="white") 
displaypcper.configure(state="disabled")

labelres=createlabel(root, "Current Resources: ")
displayres=tk.Entry(root, relief="flat", font= ("helvetica", fontSize), bg="#1f1f1f", fg="white", width=12, disabledbackground="#1f1f1f", disabledforeground="white") 
displayres.configure(state="disabled")

labelprice=createlabel(root, "Current Price: ")
displayprice=tk.Entry(root, relief="flat", font= ("helvetica", fontSize), bg="#1f1f1f", fg="white", width=12, disabledbackground="#1f1f1f", disabledforeground="white") 
displayprice.configure(state="disabled")

labelsell=tk.Label(root, text="Sell Paper Clips: ", font= ("helvetica", fontSize), bg="#1f1f1f", fg="white", justify="left")
sellpc=tk.Button(root, text="Sell", font= ("helvetica", fontSize), bg="#2f2f2f", fg="white", width=10, relief="flat", command=sell)

labelupg=tk.Label(root, text="Buy Upgrades: ", font= ("helvetica", fontSize), bg="#1f1f1f", fg="white", justify="left")
openupg=tk.Button(root, text="Upgrade", font= ("helvetica", fontSize), bg="#2f2f2f", fg="white", width=10,relief="flat", command=open_second_window)

labelmake=tk.Label(root, text="Make Paper Clip: ", font= ("helvetica", fontSize), bg="#1f1f1f", fg="white", justify="left")
makepc=tk.Button(root, text="Construct", font= ("helvetica", fontSize), bg="#2f2f2f", fg="white", width=10,relief="flat", command=makepaperclip)

labelbuy=tk.Label(root, text="Buy Resources: ", font= ("helvetica", fontSize), bg="#1f1f1f", fg="white", justify="left")
buyres=tk.Button(root, text="Purchase", font= ("helvetica", fontSize), bg="#2f2f2f", fg="white", width=10,relief="flat", command=buyresource)

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
root.after(1000, robotsfunc)
root.mainloop()
