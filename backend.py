import pandas as pd
import sqlite3
import CreateTable as ct
from tkinter import messagebox


# Database connection
with sqlite3.connect("beehives.db") as db:
    cursor = db.cursor()


# Function to  add a beehive to the database
def add_beehive(rowVar,orderVar,typeVar):


    Row = rowVar.get()
    Order = orderVar.get()
    Type = typeVar.get()
    Counter = True

    def add_user_query():
        cursor.execute(f"""
            INSERT INTO user(username,row,hivetype)
            VALUES("{Order}","{Row}","{Type}")
            """)
        db.commit()

        cursor.execute(f"SELECT * FROM user ORDER BY userid DESC LIMIT 1")
        a = cursor.fetchall()
        db.commit()
        ct.create_table(a[0][0])

    for i in view_all():

        if (Order == i[1] and Row == i[2]):
            messagebox.showerror("Error", "You allready have that hive")
            Counter = False
            break

        else: continue
    if Counter == True:
        add_user_query()
    else:
        pass



def find_beehive(rowVar,orderVar):
    Row = rowVar.get()
    Order = orderVar.get()
    query = f"SELECT * FROM user WHERE row = '{Row}' AND username = '{Order}'"

    cursor.execute(query)
    db.commit()
    a = cursor.fetchall()
    print(a)
    return (a)

def find_beehive_byRow(rowVar):
    Row = rowVar.get()
    query = f"SELECT * FROM user WHERE row = '{Row}'"
    cursor.execute(query)
    db.commit()
    a = cursor.fetchall()
    print(a)
    return (a)

def find_beehive_byOrder(orderVar):
    Order = orderVar.get()
    query = f"SELECT * FROM user WHERE username = '{Order}'"
    cursor.execute(query)
    db.commit()
    a = cursor.fetchall()
    print(a)
    return (a)

def search_beehive_byId(idVar):

    id = idVar.get()
    cursor.execute(f"SELECT * FROM user WHERE userid = '{id}'")
    db.commit()
    a = cursor.fetchall()
    print(a)
    return (a)

def view_all():
    cursor.execute("SELECT * FROM user")
    db.commit()
    a = cursor.fetchall()
    return (a)


def delete_hive(idVar):

    cursor.execute(f"DELETE FROM user WHERE userid = '{idVar}' ")
    db.commit()
    a = cursor.fetchall()
    return (a)

def update_hive(rowVar,orderVar,typeVar,idVar):
    Row = rowVar.get()
    Order = orderVar.get()
    Type = typeVar.get()
    Id = idVar.get()

    cursor.execute(f"UPDATE user SET username = '{Order}',row = '{Row}',hivetype = '{Type}' WHERE userid = '{Id}' ")
    db.commit()
    a = cursor.fetchall()
    return(a)


