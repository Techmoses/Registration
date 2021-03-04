#Registration From in Python

from tkinter import *
import sqlite3
root = Tk()
root.geometry("500x500")
root.title("Registration From")

# Full name = StringVar()
# Email = StringVar()
# Var = Int Var()
# c = StringVar()
# Varl = IntVar()

def database():
    name1 =entry2.get()
    email=entry3.get()
    gender=Var.get()
    country=c.get()
    prog1=Var1.get()
    prog2=Var2.get()
    conn =sqlite3.connect('databaseregistration.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student(Fullname TEXT,Email TEXT,Gender TEXT,Country TEXT,Programming1 TEXT,Programming2 TEXT)')
    cursor.execute('INSERT INTO Student(FullName,Email,Gender,Country,Programming1,Programming2)VALUES(?,?,?,?,?,?)',(name1,email,gender,country,prog1,prog2,))
    
    conn.commit()
    entry2.delete(0,END)
    entry3.delete(0,END)

    

label1=Label(root,text="Registration From",width=20,font=("bold",20))
label1.place(x=90,y=53)

label2=Label(root,text="Fullname",width=20,font=("bold",10))
label2.place(x=80,y=130)

entry2=Entry(root,width=30)
entry2.place(x=240,y=130)

label3=Label(root,text="Email",width=20,font=("bold",10))
label3.place(x=68,y=180)

entry3=Entry(root,width=30)
entry3.place(x=240,y=180)

label4=Label(root,text="Gender",width=20,font=("nold",10))
label4.place(x=67,y=230)

Var=StringVar()
Radiobutton(root,text="male",padx=5,variable=Var,value='male').place(x=235,y=230)
Radiobutton(root,text="Female",padx=20,variable=Var,value='female').place(x=290,y=230)

label5=Label(root,text="Country",width=20,font=("bold",10))
label5.place(x=70,y=280)
list1=['Nigeria','India','America','English','SouthAfrica','Itian','Germen','WestIndies']
c=StringVar()

droplist=OptionMenu(root,c,*list1)
droplist.config(width=15)
c.set("Select your Country")
droplist.place(x=240,y=280)

label6=Label(root,text="Programming",width=20,font=("bold",10))
label6.place(x=85,y=330)
Var1=IntVar()

Checkbutton(root,text="python",variable=Var1).place(x=235,y=330)

Var2=IntVar()

Checkbutton(root,text="java",variable=Var2).place(x=300,y=330)



Button(root,text="Submit",width=30,bg='brown',fg="white",command=database).place(x=180,y=380)

root.mainloop()
