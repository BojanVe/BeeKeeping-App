import sqlite3
import backend as backe
# with sqlite3.connect("beehives.db") as db:
#     cursor = db.cursor()
#
with sqlite3.connect("beehive_note.db") as db:
    cursor = db.cursor()

def create_table(id):
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS userid{id}(
    noteid INTEGER PRIMARY KEY,
    note VARCHAR(20) NOT NULL
    )
    ''')

def remove_table(orderVar):
    cursor.execute(f"DROP TABLE userid{orderVar}")
    db.commit()


def view_all_notes(idVar):
    cursor.execute(f"SELECT * FROM userid{idVar}")
    db.commit()
    a = cursor.fetchall()
    return (a)
    print(a)

def add_note(noteVar,orderVar):

    note = noteVar.get()

    cursor.execute(f"""
        INSERT INTO userid{orderVar}(note)
        VALUES("{note}")
        """)
    db.commit()
def remove_note(idVar,noteVar):

    cursor.execute(f"DELETE FROM userid{idVar} WHERE noteid = {noteVar} ")
    db.commit()

def update_note(orderVar,noteVar,noteid):
    cursor.execute(f"UPDATE userid{orderVar} SET note = '{noteVar}' WHERE noteid = '{noteid}'")
    db.commit()
    view_all_notes(orderVar)


