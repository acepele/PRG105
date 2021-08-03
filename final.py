from tkinter import *
import random
import time

root = Tk()
root.geometry("890x580+0+0")
root.title("Coffee bar project")
root.configure(background='grey')

Tops = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)  # https://pythonguides.com/python-tkinter-frame/

f1 = Frame(root, width=900, height=700, relief=SUNKEN)

f2 = Frame(root, width=400, height=700, relief=SUNKEN)

f3 = Frame(root, width=400, height=700, relief=SUNKEN)

Tops.pack(side='top')
f1.pack(side='left')
f2.pack(side='right')

localtime = time.asctime(time.localtime(time.time()))  # https://www.tutorialspoint.com/python/python_date_time.htm

lbl_info = Label(Tops, font=('aria', 50, 'bold'), text="Arekla Coffee Bar", fg="Red", bd=10, anchor='w')
lbl_info.grid(row=0, column=0)
lbl_info = Label(Tops, font=('aria', 20), text=localtime, fg="steel blue", anchor='w')
lbl_info.grid(row=1, column=0)


def ref():
    x = random.randint(12980, 50876)
    randomref = str(x)
    rand.set(randomref)

    macchiato = float(Macchiato.get())
    latte = float(Latte.get())
    espresso = float(Espresso.get())
    lemonade = float(Lemonade.get())
    tea = float(Tea.get())
    choccolate = float(Choccolate.get())

    costofmacchiato = macchiato * 3
    costoflatte = latte * 2
    costofespresso = espresso * 2.5
    costoflemonade = lemonade * 1
    costoftea = tea * 2
    costofchoccolate = choccolate * 5

    cost_of_drinks = ((costofmacchiato + costoflatte + costofespresso
                       + costoflemonade + costoftea + costofchoccolate))
    pay_tax = ((costofmacchiato + costoflatte + costofespresso
                + costoflemonade + costoftea + costofchoccolate) * 0.33)
    total_cost = (costofmacchiato + costoflatte + costofespresso
                  + costoflemonade + costoftea + costofchoccolate)
    ser_charge = ((costofmacchiato + costoflatte + costofespresso
                   + costoflemonade + costoftea + costofchoccolate) / 99)

    Service_Charge.set(ser_charge)
    cost.set(cost_of_drinks)
    Tax.set(pay_tax)
    Subtotal.set(total_cost)


def bexit():
    root.destroy()


def reset():
    rand.set("")
    Macchiato.set("")
    Latte.set("")
    Espresso.set("")
    Tea.set("")
    Lemonade.set("")
    Choccolate.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Tax.set("")
    cost.set("")


rand = StringVar()
Macchiato = StringVar()
Latte = StringVar()
Espresso = StringVar()
Tea = StringVar()
Lemonade = StringVar()
Choccolate = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
cost = StringVar()

# https://www.tutorialspoint.com/python/tk_label.htm

lbl_reference = Label(f1, font=('aria', 16, 'bold'), text="Order No.", fg="brown", bd=20, anchor='w')
lbl_reference.grid(row=0, column=0)
txt_reference = Entry(f1, font=('ariel', 16, 'bold'), textvariable=rand, bd=6,
                      insertwidth=6, bg="green", justify='right')
txt_reference.grid(row=0, column=1)

lbl_macchiato = Label(f1, font=('aria', 16, 'bold'), text=" Macchiato ", fg="blue", bd=10, anchor='w')
lbl_macchiato.grid(row=2, column=0)
txt_macchiato = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Macchiato, bd=6,
                      insertwidth=4, bg="white", justify='right')
txt_macchiato.grid(row=2, column=1)

lbl_latte = Label(f1, font=('aria', 16, 'bold'), text="Latte ", fg="blue", bd=10, anchor='w')
lbl_latte.grid(row=3, column=0)
txt_latte = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Latte, bd=6,
                  insertwidth=4, bg="white", justify='right')
txt_latte.grid(row=3, column=1)

lbl_espresso = Label(f1, font=('aria', 16, 'bold'), text="Espresso ", fg="blue", bd=10, anchor='w')
lbl_espresso.grid(row=4, column=0)
txt_espresso = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Espresso, bd=6,
                     insertwidth=4, bg="white", justify='right')
txt_espresso.grid(row=4, column=1)

lbl_tea = Label(f1, font=('aria', 16, 'bold'), text="Tea ", fg="blue", bd=10, anchor='w')
lbl_tea.grid(row=5, column=0)
txt_tea = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Tea, bd=6,
                insertwidth=4, bg="white", justify='right')
txt_tea.grid(row=5, column=1)

lbl_lemonade = Label(f1, font=('aria', 16, 'bold'), text=" Lemonade", fg="blue", bd=10, anchor='w')
lbl_lemonade.grid(row=6, column=0)
txt_lemonade = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Lemonade, bd=6,
                     insertwidth=4, bg="white", justify='right')
txt_lemonade.grid(row=6, column=1)

lbl_choccolate = Label(f1, font=('aria', 16, 'bold'), text="Choccolate", fg="blue", bd=10, anchor='w')
lbl_choccolate.grid(row=1, column=0)
txt_choccolate = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Choccolate, bd=6,
                       insertwidth=4, bg="white", justify='right')
txt_choccolate.grid(row=1, column=1)

lblcost = Label(f1, font=('aria', 16, 'bold'), text="Cost", fg="black", bd=10, anchor='w')
lblcost.grid(row=2, column=2)
txtcost = Entry(f1, font=('ariel', 16, 'bold'), textvariable=cost, bd=6,
                insertwidth=4, bg="white", justify='right')
txtcost.grid(row=2, column=3)

lblService_Charge = Label(f1, font=('aria', 16, 'bold'), text="Service Charge", fg="black", bd=10, anchor='w')
lblService_Charge.grid(row=3, column=2)
txtService_Charge = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Service_Charge, bd=6,
                          insertwidth=4, bg="white",
                          justify='right')
txtService_Charge.grid(row=3, column=3)

lblTax = Label(f1, font=('aria', 16, 'bold'), text="Tax", fg="black", bd=10, anchor='w')
lblTax.grid(row=4, column=2)
txtTax = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Tax, bd=6,
               insertwidth=4, bg="white", justify='right')
txtTax.grid(row=4, column=3)

lblSubtotal = Label(f1, font=('aria', 16, 'bold'), text="Subtotal", fg="black", bd=10, anchor='w')
lblSubtotal.grid(row=5, column=2)
txtSubtotal = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Subtotal, bd=6,
                    insertwidth=4, bg="white",
                    justify='right')
txtSubtotal.grid(row=5, column=3)

lblTotal = Label(f1, font=('aria', 16, 'bold'), text="Total", fg="green", bd=10, anchor='w')
lblTotal.grid(row=6, column=2)
txtTotal = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Total, bd=6,
                 insertwidth=4, bg="green", justify='right')
txtTotal.grid(row=6, column=3)
# ----------------------------Buttons-------------------
lblTotal = Label(f1, text="---------------------", fg="white")
lblTotal.grid(row=7, columnspan=3)

btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="TOTAL", bg="red",
                  command=ref)
btnTotal.grid(row=8, column=1)

btnreset = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="RESET", bg="red",
                  command=reset)
btnreset.grid(row=8, column=2)

btnbexit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10,
                  text="EXIT", bg="yellow", command=bexit)

btnbexit.grid(row=8, column=3)


def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="***************", fg="white", anchor='w')
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor='w')
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Macchiato", fg="blue", anchor='w')
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="3$", fg="blue", anchor='w')
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Latte ", fg="blue", anchor='w')
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2$", fg="blue", anchor='w')
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Espresso ", fg="blue", anchor='w')
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2.5$", fg="blue", anchor='w')
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tea ", fg="blue", anchor='w')
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2$", fg="blue", anchor='w')
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lemonade", fg="blue", anchor='w')
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1$", fg="blue", anchor='w')
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Choccolate", fg="blue", anchor='w')
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="5$", fg="blue", anchor='w')
    lblinfo.grid(row=6, column=3)

    roo.mainloop()


btnprice = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="PRICE", bg="red",
                  command=price)
btnprice.grid(row=8, column=0)

root.mainloop()

# https://www.tutorialspoint.com/python/tk_grid.htm
# https://www.pythontutorial.net/tkinter/tkinter-grid/
# https://realpython.com/python-gui-tkinter/
# https://www.datacamp.com/community/tutorials/gui-tkinter-python
