from tkinter import *
root=Tk()
root.title("eb bill")
root.geometry("500x700")
def click():
     a=e3.get()
     b=e4.get()
     tot=int(b)-int(a)
     unit=tot*5
     e5.delete(0,END)
     e5.insert(0,str(tot))
     e6.delete(0,END)
     e6.insert(0,str(unit))
     return
f1=Frame(root)
f1.config(bg="orange")
f1.pack(fill="both",expand=0)
l1=Label(f1,text="GOVERNMENT OF TAMILNADU",bg="orange",fg="white",font=("arial",18,"bold"))
l1.pack()
l2=Label(f1,text="ELECTRICITY BOARD",bg="BLUE")
l2.pack()

f2=Frame(root)
f2.config(bg="BLACK")
f2.pack(fill="both",expand=0)

l3=Label(f2,text="EB NUMBER")
l3.pack()
e1=Entry(f2)
e1.pack()

l4=Label(f2,text="CUSTOMER NAME")
l4.pack()
e2=Entry(f2)
e2.pack()

l5=Label(f2,text="PREVIOUS UNIT")
l5.pack()
e3=Entry(f2)
e3.pack()

l6=Label(f2,text="CURRENT UNIT")
l6.pack()
e4=Entry(f2)
e4.pack()

l7=Label(f2,text="UNIT USED THIS MONTH")
l7.pack()
e5=Entry(f2)
e5.pack()

l8=Label(f2,text="AMOUNT TO BE PAID")
l8.pack()
e6=Entry(f2)
e6.pack()
b1=Button(f2,text="CLICK",command=click)
b1.pack()
root.mainloop()
