from tkinter import *

window=Tk()

def kg_convert():
    print(e1_value.get())
    grams=float(e1_value.get())*1000
    pounds=float(e1_value.get())*2.20462
    ounces=float(e1_value.get())*35.274
    t1.delete("1.0", END)
    t1.insert(END, grams, " grams")
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", END)
    t3.insert(END, ounces)

k=Label(window, text="Kg")
k.grid(row=0,column=1)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=2)

b1 = Button(window, text = "Convert", command=kg_convert)
b1.grid(row=0,column=3)

g=Label(window, text="grams")
g.grid(row=1,column=1)

p=Label(window, text="pounds")
p.grid(row=1,column=2)

o=Label(window, text="ounces")
o.grid(row=1,column=3)

t1=Text(window, height=1,width=10)
t1.grid(row=2,column=1)

t2=Text(window, height=1,width=10)
t2.grid(row=2,column=2)

t3=Text(window, height=1,width=10)
t3.grid(row=2,column=3)

window.mainloop()
