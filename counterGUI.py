from tkinter import *

counter = 0
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()

root = Tk()
root.title("Counting Seconds")
label = Label(root, fg="dark green")
label.pack()

counter_label(label)

quitbutton = Button(root, text='Quit', width=25, bg="red", fg="black", command=root.destroy)
quitbutton.pack()


root.mainloop()
