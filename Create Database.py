import sqlite3

with sqlite3.connect("beehives.db") as db:
    cursor = db.cursor()

cursor.execute("ALTER TABLE user ADD UNIQUE username ")
db.commit()
#a = cursor.execute("SELECT * FROM user")
#print(cursor.fetchall())

#c = cursor.execute("""UPDATE user SET notes = "Test 3" WHERE username = '3'""")

# a = cursor.execute("SELECT * FROM user")
# print(cursor.fetchall())
# #b = cursor.execute("DELETE FROM user")
# #db.close()






