from builtins import type
from tkinter import  *
import backend as be
from tkinter import messagebox
import CreateTable as ct
import tkinter.font as tkFont


app = Tk()
app.geometry("420x350")
app.configure(bg="#F4D03F")
app.title("Beekeeping Records")

background_image=PhotoImage(file = 'C://Users//bojan//PycharmProjects//BeeKeeping//png//1465582248.png')
background_label = Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#_____________Variables____________________
rowVar = StringVar(app)
orderVar = StringVar(app)
typeVar = StringVar(app)
notesVar = StringVar(app)
idVar = StringVar(app)


#Hive entry information, row, number, type
rowTitle = Label(app, text='Row Number:', bg='#F4D03F')
rowTitle.place(x=20,y=30)
row = Entry(app, textvariable = rowVar, width = 20)
row.place(x=20,y=50)

orderNumTitle = Label(app, text='Order Number:', bg='#F4D03F')
orderNumTitle.place(x=20,y=80)
orderNum = Entry(app, textvariable = orderVar, width = 20)
orderNum.place(x=20,y=100)

typeTitle = Label(app, text='Hive Type:', bg='#F4D03F')
typeTitle.place(x=20,y=130)



id_number = Label(app, text='ID Number:', bg='white')
id_number.place(x=300,y=45, width = 74)
id_entry= Entry(app, textvariable = idVar, bg='white', font = 100,width = 6)
id_entry.place(x=300,y=74)



helv18 = tkFont.Font(family="Helvetica",size=18,weight="bold")
list_display = Listbox(app,height = 4, width = 16, font = helv18)
list_display.place(x=10,y=220)
list_display.insert(END)


helv8 = tkFont.Font(family="Helvetica",size=7,weight="normal")
description = Label(app, text = 'ID Order Row Hive type', font = helv8).place(x=12,y=200)


# Hive type dropdown
choices = { 'Langstroth','Dadant-Blatt','Farrar','Nucleus'}
typeVar.set('') # set the default option

popupMenu = OptionMenu(app, typeVar, *choices)
popupMenu.place(x=20,y=150, width = 130)


def find_button():
    list_display.delete(0,END)
    if rowVar.get() !='' and orderVar.get() != '':
        for item in be.find_beehive(rowVar,orderVar):
            list_display.insert(END,item)
    elif rowVar.get() !='' and orderVar.get() == '':
        for item in be.find_beehive_byRow(rowVar):
            list_display.insert(END,item)
    elif rowVar.get() =='' and orderVar.get() != '':
        for item in be.find_beehive_byOrder(orderVar):
            list_display.insert(END,item)
    else:
        messagebox.showerror("Wrong Combination", "Please enter valid Row and Order")

def clear_fields():
    rowVar.set('')
    orderVar.set('')
    typeVar.set('')

#On click action, when hive is selected, fields are filled
def list_set(self):
    active_hive = list_display.get(ACTIVE)
    rowVar.set(active_hive[2])
    orderVar.set(active_hive[1])
    typeVar.set(active_hive[3])
    idVar.set(active_hive[0])

def view_all_button():
    list_display.delete(0,END)
    for item in be.view_all():
        list_display.insert(END,item)

def delete_hive_button():
    active_hive = list_display.get(ACTIVE)
    for item in be.delete_hive(active_hive[0]):
        list_display.insert(END,item)
    view_all_button()
    clear_fields()
    ct.remove_table(active_hive[0])


def update_hive_button():
    list_display.delete(0, END)
    for item in be.update_hive(rowVar,orderVar,typeVar,idVar):
        list_display.insert(END, item)
    view_all_button()

#New Window
def open_beehive():


    active_hive = list_display.get(ACTIVE)
    newWindow = Toplevel(app)
    newWindow.title(f"Hive {active_hive}")
    newWindow.geometry("550x300")

    noteVar = StringVar(newWindow)

    text_show = f'Hive {active_hive[1]} on row {active_hive[2]} - {active_hive[3]}'
    title = Label(newWindow,text=text_show, font = 5).place(x=10,y=10)

    id_new_win = Label(newWindow,text = f"Hive ID: {active_hive[0]}", font = 5).place(x=250, y = 10)

    list_display1 = Listbox(newWindow, height=10, width=42)
    list_display1.place(x=10, y=90)

    def update_note_list():
        list_display1.delete(0, END)
        for item in ct.view_all_notes(active_hive[0]):
            list_display1.insert(END,item)
    update_note_list()

    def add_new_note():
        ct.add_note(noteVar,active_hive[0])
        update_note_list()
        noteVar.set('')

    def remove_note():
        active_note = list_display1.get(ACTIVE)
        ct.remove_note(active_hive[0],active_note[0])
        update_note_list()
        noteVar.set('')

    def update_notef():
        active_note = list_display1.get(ACTIVE)
        ct.update_note(active_hive[0],noteVar.get(),active_note[0])
        update_note_list()

    add_note = Button (newWindow,text='Add Note', command = add_new_note).place(x=280, y= 120, width = 80)
    remove_note = Button (newWindow,text='Remove Note', command = remove_note).place(x=370, y= 120, width = 80)
    update_note = Button (newWindow, text = 'Update Note', command = update_notef).place(x = 460, y = 120, width = 80)
    add_note_entry = Entry(newWindow, textvariable = noteVar,font = 4, width = 23).place(x=280, y= 90)



def search_byId():
    list_display.delete(0, END)
    for item in be.search_beehive_byId(idVar):
        list_display.insert(END, item)

def add_button():
    be.add_beehive(rowVar, orderVar, typeVar)
    view_all_button()
    clear_fields()

addHiveBtn = Button(app, text='Add BeeHive', command=add_button )
addHiveBtn.place(x=170,y=45, width = 100)


view_hive = Button(app, text='Find BeeHive', command = find_button )
view_hive.place(x=170, y=75, width = 100)

view_hive_byId = Button(app, text='Search by ID', command = search_byId )
view_hive_byId.place(x=300, y=109, width = 77)

view_all = Button(app, text='View All', command = view_all_button )
view_all.place(x=170, y=105, width = 100)

delete = Button(app, text='Delete BeeHive', command = delete_hive_button)
delete.place(x=170, y=135, width = 100)

update = Button(app, text = 'Update BeeHive', command = update_hive_button)
update.place(x=170, y=165, width = 100)

open_hive = Button(app, text = 'Open BeeHive', command = open_beehive)
open_hive.place(x=290, y=245,width = 100, height = 48)


list_display.bind('<Button-1>',list_set)





app.mainloop()
