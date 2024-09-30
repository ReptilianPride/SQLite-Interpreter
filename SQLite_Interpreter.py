import sqlite3
import os
import time
from tabulate import tabulate

def connect_db(db_name):
    return sqlite3.connect(db_name)

def executeQuery(connection,query):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        if query.strip().lower().startswith('select'):
            rows=cursor.fetchall()
            if rows:
                col_names=[description[0] for description in cursor.description]
                print(tabulate(rows,headers=col_names,tablefmt='fancy_grid'))
                print(f'{len(rows)} rows and {len(col_names)} columns')
            connection.commit()
    except sqlite3.Error as e:
        print("SQLite Error::: ",e)
    finally:
        cursor.close()

def main():
    print("SQLite Interpreter by ReptilianPride\n")
    db_name=input("Enter DB file location(Leave empty for :memory:):~")
    if not db_name:
        db_name=':memory:'
    
    connection=connect_db(db_name)

    print('''
    Available Commands:\n
          'exit' - To exit from terminal\n
          'clear' - To clear terminal\n
    ''')

    while True:
        query=input('sqlite>')
        if query.lower()=='exit':
            break
        elif query.lower()=='clear':
            if(os.name=='nt'):
                os.system('cls')
            else:
                os.system('clear')
            continue
            
        executeQuery(connection,query)

    print('\nClosing connection SQLite...\n')
    print('Check me out on github:')
    print('https://github.com/ReptilianPride')
    time.sleep(3)

if __name__ == "__main__":
    main()