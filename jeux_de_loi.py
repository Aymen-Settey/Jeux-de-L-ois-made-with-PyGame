from curses.textpad import rectangle
from email.mime import image
from tkinter import *
import random
from tkinter.font import BOLD
from tkinter.messagebox import *

def avance():
    val = random.randint(1,6)
    text.delete(0,"end")
    text.insert(0,val)
    


tk = Tk()
tk.title("jeu de lois")
#tk.geometry("1080x1920")

filename = PhotoImage(file="\\Users\\messi\\OneDrive\\Bureau\\python projects\\gameee.png")

c = Canvas(tk,height=1000,width=1500)
pion = c.create_oval(320,520,380,560,fill="black")
i = c.create_image(0,-100,image=filename,anchor=NW)
c.pack()

"""bgr = Label(tk,bg="black",image=filename,relief=RAISED)
bgr.place(y=0,x=0,relheight=1,relwidth=1)
fo = Label(tk,text="Lets play",bg="black",font=('Arial',30,"bold"),fg="#FF0000")
fo.place(x=700,y=0)"""

text = Entry(tk,width=50)
text.place(x=150,y=700)
btn = Button(tk,text="lancer",command=avance)
btn.place(x=250,y=750)




tk.mainloop()