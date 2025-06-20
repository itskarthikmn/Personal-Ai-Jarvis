import csv
import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)
query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)


    # # to insert values in sys_command and web_command
# query = "INSERT INTO sys_command VALUES (null,'Visual Studio Code', 'C:\\Users\\Karthik M N\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code')"
# cursor.execute(query)
# conn.commit()
# query = "INSERT INTO web_command VALUES (null,'whatsapp web','https://web.whatsapp.com/')"
# cursor.execute(query)
# conn.commit()

    # #to delete unwonted tables
# query = "DELETE FROM web_command WHERE name='whatsapp'"
# cursor.execute(query)
# conn.commit()



    # #testing module
# app_name = "Visual Studio Code"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])


    # #to create contacts table
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name VARCHAR(200), Phone VARCHAR(255), email VARCHAR(255) NULL)''') 



    # # to insert multiple contacts
# desired_columns_indices = [0, 18]
 
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'Phone') VALUES (null, ?,? );''', tuple(selected_data))

    # # Commit changes and close connection
# conn.commit()
# conn.close()
# print("Data inserted successfully") 



    # # to insert single contact
# query = "INSERT INTO contacts VALUES (null,'pawan', '1234567890', 'null')"
# cursor.execute(query)
# conn.commit() 



    # # to set query
# query = 'Darshan'
# query = query.strip().lower()  # Added parentheses to call the method


    # #to fetch contact from data base
# cursor.execute("SELECT Phone FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", 
#                ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])