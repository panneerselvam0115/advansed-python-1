from tkinter import *
root=Tk()
root.title("MY APPS")
root.geometry("500x700")

def click():
     a=e3.get()
     b=e4.get()
     c=e5.get()
     total=int(a)+int(b)+int(c)
     average=total/3
     e6.delete(0,END)
     e6.insert(0,str(total))
     e7.delete(0,END)
     e7.insert(0,str(average))
     return

f1=Frame(root)
f1.config(bg="orange")
f1.pack(fill="both",expand=0)
l1=Label(f1,text="TAKSHASHILA UNIVERSITY,",bg="orange",fg="white")
l1.pack()

l2=Label(f1,text="ONGUR,TINDIVANAM,VILLUPURAM",bg="orange",fg="white")
l2.pack()
f2=Frame(root)

f2.config(bg="VIOLET")
f2.pack(fill="both",expand=0)
l3=Label(f2,text="STUDENT MARK LIST")
l3.pack()

f3=Frame(root)
f3.config(bg="WHITE")
f3.pack(fill="both",expand=0)
l4=Label(f3,text="ENROLLMENT NO",bg="pink",fg="black")
l4.pack()
e1=Entry(f3)
e1.pack()

l5=Label(f3,text="NAME",bg="pink",fg="black")
l5.pack()
e2=Entry(f3)
e2.pack()

l6=Label(f3,text="PYTHON",bg="pink",fg="black")
l6.pack()
e3=Entry(f3)
e3.pack()

l7=Label(f3,text="DBMS",bg="pink",fg="black")
l7.pack()
e4=Entry(f3)
e4.pack()

l8=Label(f3,text="XEBIA",bg="pink",fg="black")
l8.pack()
e5=Entry(f3)
e5.pack()

l9=Label(f3,text="TOTAL",bg="pink",fg="black")
l9.pack()
e6=Entry(f3)
e6.pack()

l0=Label(f3,text="AVERAGE",bg="pink",fg="black")
l0.pack()
e7=Entry(f3)
e7.pack()

b1=Button(f3,text="CLICK",command=click)
b1.pack()
