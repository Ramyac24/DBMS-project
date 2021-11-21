import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
from tkinter import *
import pandas as pd
from pandastable import Table, TableModel
import psycopg2
 
class Application(tk.Frame):
    
    def __init__(self, root):
        self.root = root
        self.initialize_user_interface()

    def clearTreeview(self) :
        for i in self.tree.get_children():
            self.tree.delete(i)
     
    def initialize_user_interface(self):
        # Configure the root object for the Application
        self.root.title("Courier Management System")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(background="cyan")
        self.name=StringVar()
        self.x=StringVar()
       
    
        
        # Define the different GUI widgets
        self.name_label = tk.Label(self.root, text="Enter your query :")
        self.name_entry = tk.Entry(self.root, width = 100, textvariable=self.name)
        self.name_label.grid(row=1, column=0, padx = 20, pady = 20, sticky=tk.W)
        self.name_entry.grid(row=1, columnspan=7, padx = 20, pady = 20)
  
        self.submit_button = tk.Button(self.root, text="select", command=self.select)
        self.submit_button.grid(row=3, column=1, padx=20)

        self.insert_button = tk.Button(self.root, text="insert", command=self.insert)
        self.insert_button.grid(row=3, column=2, padx=20)

        self.update_button = tk.Button(self.root, text="update", command=self.update)
        self.update_button.grid(row=3, column=3, padx=20)

        self.delete_button = tk.Button(self.root, text="delete", command=self.delete)
        self.delete_button.grid(row=3, column=4, padx=20)
 
        
 
        # Set the treeview
        self.tree = ttk.Treeview(self.root, columns=(0,1,2,3,4,5,6,7,8))
        
        self.tree.grid(row=5,columnspan=5, padx = 10, pady = 10)
        
        
        self.exit_button = tk.Button(self.root, text="Exit", command=self.close)
        self.exit_button.grid(row=7, columnspan=3, padx = 10, pady = 10)

 
        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#0', stretch=tk.NO, width=90)
        self.tree.column('#1', stretch=tk.NO, width=90)
        self.tree.column('#2', stretch=tk.NO, width=90)
        self.tree.column('#3', stretch=tk.NO, width=90)
        self.tree.column('#4', stretch=tk.NO, width=90)
        self.tree.column('#5', stretch=tk.YES)
        self.tree.column('#6', stretch=tk.YES)
        self.tree.column('#7', stretch=tk.YES)
        self.tree.column('#8', stretch=tk.YES)
 
    def close(self):
            self.root.destroy()

    def insert(self):
            query=name.get()
            conn=psycopg2.connect(database="courier_db", user='postgres', password='rajeshwari', host='127.0.0.1', port= '5432')
            cur=conn.cursor()
            cur.execute(query)
            conn.commit()
            conn.close()
            pass


    def update(self):
            query=name.get()
            conn=psycopg2.connect(database="courier_db", user='postgres', password='rajeshwari', host='127.0.0.1', port= '5432')
            cur=conn.cursor()
            cur.execute(query)
            conn.commit()
            conn.close()
            pass
    def delete(self):
            query=name.get()
            conn=psycopg2.connect(database="courier_db", user='postgres', password='rajeshwari', host='127.0.0.1', port= '5432')
            cur=conn.cursor()
            cur.execute(query)
            conn.commit()
            conn.close()
            pass
 
    def select(self):
        
            self.clearTreeview()
            query=self.name.get()
            self.x.set(query)
            conn=psycopg2.connect(database="courier_db", user='postgres', password='rajeshwari', host='127.0.0.1', port= '5432')
            my_table = pd.read_sql(query, conn) 
            pd.set_option('display.max_rows', 500)
            pd.set_option('display.max_columns', 500)
            pd.set_option('display.width', 1000)
            (rows, cols) = my_table.shape
            
            headings = tuple([i for i in range(0,cols)])
            
            for i in headings :
                self.tree.heading(f'#{i}', text = my_table.columns[i])
            for row in range(1,rows) :
                record = []
                for col in range(0,cols) :
                    record.append(my_table.iloc[row,col])
                self.tree.insert('', 0, text=record[0], values = record[1:])

                
                	    
app = Application(tk.Tk())

app.root.mainloop()
