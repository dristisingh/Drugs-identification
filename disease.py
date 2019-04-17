from tkinter import *
from tkinter import Tk,ttk
import sqlite3
#from PIL import ImageTk, Image
con=sqlite3.Connection('records')
root4=Tk()
def fun1():
    root4.destroy()
    root=Tk()
    root.configure(background='violet')
    root.title('Diseases&Drug database')
    Label(root,text='Welcome',font='times 30 bold italic').grid(row=0,column=0)
    Label(root,text='Enter your details correctly',font='times 30 bold italic').grid(row=1,column=0)
    Label(root,text='Name',font='times 20',bg='orange').grid(row=2,column=0)
    e=Entry(root).grid(row=2,column=1)
    Label(root,text='Age',font='times 20',bg='blue').grid(row=3,column=0)
    f=Entry(root).grid(row=3,column=1)
    Label(root,text='Sex',font='times 20',bg='light green').grid(row=4,column=0)
   
    v1=StringVar()
    box=ttk.Combobox(root,textvariable=v1,state='readonly')
    box['values']=('F','M')
    box.grid(row=4,column=1)
    def dis():
        root1=Tk()
        root1.configure(background='sky blue')
        cur=con.cursor()
        cur.execute("create table if not exists diseasedata(Disease varchar(50),Drugs varchar(50))")
        Label(root1,text='Disease',bg='yellow').pack()
        e=Entry(root1)
        e.pack()
        Label(root1,text='Drugs',bg='maroon').pack()
        f=Entry(root1)
        f.pack()
        def wish1():
            a=[e.get(),f.get()]
            cur.execute("insert into diseasedata values(?,?)",a)
            con.commit()
        Button(root1,text='Insert',bg='green',command=wish1).pack()
        Label(root1,text='Enter Disease to fetch record',bg='pink').pack()
        j=Entry(root1)
        j.pack()
        def search():
            a=j.get()
            cur.execute('select Drugs from diseasedata where Disease=?',(a,))
            b=cur.fetchall()
            b=b[0][0]
            Label(root1,text=b,relief='ridge',font='times 10 bold italic',bg='white').pack()
        Button(root1,text='Show',bg='orange',command=search).pack()
        def all():
            cur.execute('select * from diseasedata ')
            b=cur.fetchall()
            Label(root1,text=b,relief='ridge',font='times 10 bold italic',bg='white').pack()
        Button(root1,text='Show All',bg='purple',command=all).pack()
        Button(root1,text='EXIT',bg='red',command=root1.destroy).pack()
    Button(root,text='submit',command=dis).grid(row=5,column=2)
a=PhotoImage(file='img.gif')
lb=Label(root4,image=a)
lb.after(500,fun1)
lb.pack()

root4.mainloop()
