import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import *
#from tkinter.constants import CENTER
import psycopg2
win=tk.Tk()
win.geometry('1000x1000')
win.config(bg='teal')
win.title("DBMS ASSIGNMENT UE19CS301")
lbl=ttk.Label(win,text="Enter your query:").grid(column=0,row=0)
#lbl.Place(relx= .5, rely= .5, anchor= CENTER)
def select():
    query=name.get()
    x.set(query)
    conn=psycopg2.connect(database="courier_db", user='postgres', password='chapusrs', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    cursor.execute(query)
    row=cursor.fetchall()
    s=str()
    for i in row:
        s=s+str(i)+'\n'
    mytext.set(s)
    listbox=Listbox(win)
    listbox.insert(10,str(row))
    #listbox.pack()
    return 
def insert():
    query=name.get()
    conn=psycopg2.connect(database="courier_db", user='postgres', password='chapusrs', host='127.0.0.1', port= '5432')
    cur=conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()
    pass
def update():
    query=name.get()
    conn=psycopg2.connect(database="courier_db", user='postgres', password='chapusrs', host='127.0.0.1', port= '5432')
    cur=conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()
    pass
name=StringVar()
mytext=StringVar()
x=StringVar()
entered=ttk.Entry(win,width=100,textvariable=name).grid(column=0,row=2)
button1=ttk.Button(win,text='select',command=select).grid(row=2, column=6)
button2=ttk.Button(win,text='insert',command=insert).grid(row=2, column=10)
button3=ttk.Button(win,text='update',command=insert).grid(row=2, column=14)
y=Label(win, text="", textvariable=x).grid(row=10,column=0)
result=Label(win, text="", textvariable=mytext).place(x=10,y=100)
b2 = tk.Button(win, text="Exit from Query Box!!", command=win.destroy).place(x=10, y=500)
win.mainloop()
