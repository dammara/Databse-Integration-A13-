# Markhus Dammar
# 30 April 2020
# This program uses SQLite and databases

import sqlite3, time
from sqlite3 import Error


def exit_prog():                                        # Exit Screen
    print("\033[1mGoodbye! \033[0m")
    time.sleep(1)
    exit()


def invalid():                                          # Screen for Invalid input
    print("INVALID CHOICE, TRY AGAIN")
    time.sleep(1.5)


def welcome():                                          # Splash Screen
    print("""\033[1m
    ---------SQLite Database Prog Version 1.0--------- \033[0m
    Welcome. This program will use SQL to create
                  and modify databases.""")
    time.sleep(2)


def choose():                                           # Main Menu where the user selects customer or books
    print(f"""\n
                MAIN MENU 
\033[1m ----ENTER the NUMBER (1, 2, 3)---- \033[0m
    1. Customers
    2. Books
    3. Exit Program
    """)

    method = int(input(">>>"))                          # Method is inputted here

    while method > 3 or method < 1:                     # Invalid Choice
        invalid()
        choose()
    if method == 1:                                     # Creates customer table and prints customer menu
        print("Accessing Customer Menu...")
        time.sleep(1)
        customers()
    elif method == 2:                                   # Creates books table and prints books menu
        print("Accessing Book Menu...")
        time.sleep(1)
        books()
    elif method == 3:
        exit_prog()


def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return conn

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


create_customer_table = """
CREATE TABLE IF NOT EXISTS customer (
  cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  street_address TEXT NOT NULL,
  city TEXT NOT NULL,
  state TEXT NOT NULL,
  zip INTEGER
);
"""

create_books_table = """
CREATE TABLE IF NOT EXISTS book (
  book_id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  isbn INTEGER,
  edition INTEGER,
  price INTEGER,
  publisher TEXT NOT NULL
);
"""


def customers():                                            # Customer Menu Here
    print(f"""\n
                CUSTOMER MENU 
\033[1m ----ENTER the NUMBER (1, 2, 3...)---- \033[0m
    1. Add New Customer
    2. Modify Existing Customer
    3. Print a List of ALL Customers
    4. Delete a Customer
    5. Return to Main Menu
    """)

    c_method = int(input(">>>"))                            # Method is inputted here

    while c_method > 5 or c_method < 1:                     # Invalid Response Check
        invalid()
        customers()
    if c_method == 1:                                       # Add New Customer
        print("\n\033[1mADD NEW CUSTOMER\033[0m")
        cust_id = input("Enter the customer ID >>>")
        first_name = input("Enter First Name >>>")
        last_name = input("Enter Last Name >>>")
        street_address = input("Enter Street Address >>>")
        city = input("Enter City Name >>>")
        state = input("Enter State Initials >>>")
        zip = input("Enter ZIP code >>>")
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO customer (cust_id, first_name, last_name, street_address, city, state, zip)
        VALUES (?, ?, ?, ?, ?, ?, ?)""", (cust_id, first_name, last_name, street_address, city, state, zip))
        connection.commit()
        print("\033[1mNEW CUSTOMER ADDED SUCCESSFULLY!\033[0m")
        time.sleep(1)
        print("\033[1mReturning to CUSTOMER MENU...\033[0m")
        time.sleep(1.5)
        customers()
    elif c_method == 2:                                         # Modify Customer
        print("\n\033[1mMODIFY EXISTING CUSTOMER\033[0m")
        select_customer = "SELECT * from customer"               # PRINTS LIST OF CUSTOMERS
        people = execute_read_query(connection, select_customer)
        for person in people:
            print(person)
        search = input("ENTER the ID of the customer you want to MODIFY >>>")
        nfirst_name = input("Enter new First Name >>>")
        nlast_name = input("Enter new Last Name >>>")
        nstreet_address = input("Enter new Street Address >>>")
        ncity = input("Enter new City Name >>>")
        nstate = input("Enter new State Initials >>>")
        nzip = input("Enter new ZIP code >>>")
        cursor = connection.cursor()                        # Updates customer based on the user input above
        cursor.execute("""                                         
        UPDATE 
         customer
        SET
        first_name = ?,
        last_name = ?,
        street_address = ?,
        city = ?,
        state = ?,
        zip = ?
        WHERE
        cust_id = ?
        """, (nfirst_name, nlast_name, nstreet_address, ncity, nstate, nzip, search)

        )
        connection.commit()
        print("\033[1mCUSTOMER UPDATED SUCCESSFULLY\033[0m")
        time.sleep(1)
        print("\033[1mReturning to CUSTOMER MENU...\033[0m")
        time.sleep(1.5)
        customers()
    elif c_method == 3:                                      # Shows list of all customers
        select_customer = "SELECT * from customer"
        people = execute_read_query(connection, select_customer)
        for person in people:
            print(person)
        time.sleep(4)
        print("\033[1mReturning to CUSTOMER MENU...\033[0m")
        time.sleep(1.5)
        customers()
    elif c_method == 4:                                  # Deletes a customer
        select_customer = "SELECT * from customer"
        people = execute_read_query(connection, select_customer)
        for person in people:
            print(person)
        print("\n\033[1mDELETE EXISTING CUSTOMER\033[0m")
        searching = str(input("ENTER the ID of the customer you want to DELETE >>>"))
        sure = input(f"Are you sure you want to delete customer {searching}? (y/n)")
        if sure == 'yes' or sure == 'Yes' or sure == 'y' or sure == 'Y':
            cursor = connection.cursor()
            cursor.execute("DELETE FROM customer WHERE cust_id=?", (searching,))
            connection.commit()
            print("\033[1mCUSTOMER DELETED SUCCESSFULLY!\033[0m")
            time.sleep(1)
            print("\033[1mReturning to CUSTOMER MENU...\033[0m")
            time.sleep(1.5)
            customers()
        else:
            print("\033[1mDELETION ABORTED, Returning to CUSTOMER MENU...\033[0m")
            time.sleep(1.5)
            customers()
    elif c_method == 5:
        print("\033[1mReturning to Main Menu...\033[0m")
        time.sleep(1.5)
        choose()


def books():                                                        # Book Menu Here
    print(f"""\n
                BOOK MENU 
\033[1m ----ENTER the NUMBER (1, 2, 3...)---- \033[0m
    1. Add New Book
    2. Modify Existing Book
    3. Print a List of ALL Books
    4. Delete a Book
    5. Return to Main Menu
    """)

    b_method = int(input(">>>"))                                # Method is inputted here

    while b_method > 5 or b_method < 1:                         # Invalid Check
        invalid()
        books()
    if b_method == 1:                                           # Add New Book
        print("\n\033[1mADD NEW BOOK\033[0m")
        book_id = input("Enter the book ID >>>")
        title = input("Enter the book title >>>")
        author = input("Enter Author's first/last name >>>")
        isbn = input("Enter book ISBN >>>")
        edition = input("Enter book edition >>>")
        price = input("Enter price >>>$")
        publisher = input("Enter publisher >>>")
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO book (book_id, title, author, isbn, edition, price, publisher)
        VALUES (?, ?, ?, ?, ?, ?, ?)""", (book_id, title, author, isbn, edition, price, publisher))
        connection.commit()
        print("\033[1mNEW BOOK ADDED SUCCESSFULLY!\033[0m")
        time.sleep(1)
        print("\033[1mReturning to BOOK MENU...\033[0m")
        time.sleep(1.5)
        books()
    elif b_method == 2:                                     # MODIFY EXISTING BOOKS
        print("\n\033[1mMODIFY EXISTING BOOK\033[0m")
        select_book = "SELECT * from book"                   # PRINTS LIST OF BOOKS
        thebooks = execute_read_query(connection, select_book)
        for book in thebooks:
            print(book)
        search = input("ENTER a book ID >>>")
        ntitle = input("Enter new book title >>>")
        nauthor = input("Enter new Author's first/last name >>>")
        nisbn = input("Enter new ISBN >>>")
        nedition = input("Enter new edition >>>")
        nprice = input("Enter new price >>>$")
        npublisher = input("Enter new publisher >>>")
        cursor = connection.cursor()
        cursor.execute("""
        UPDATE 
         book
        SET
        title = ?,
        author = ?,
        isbn = ?,
        edition = ?,
        price = ?,
        publisher = ?
        WHERE
        book_id = ?
        """, (ntitle, nauthor, nisbn, nedition, nprice, npublisher, search)

        )
        connection.commit()
        print("\033[1mBOOK UPDATED SUCCESSFULLY!\033[0m")
        time.sleep(1)
        print("\033[1mReturning to BOOK MENU...\033[0m")
        time.sleep(1.5)
        books()
    elif b_method == 3:
        select_book = "SELECT * from book"                      # PRINTS LIST OF BOOKS
        thebooks = execute_read_query(connection, select_book)
        for book in thebooks:
            print(book)
        time.sleep(4)
        print("\033[1mReturning to BOOK MENU...\033[0m")
        time.sleep(1.5)
        books()
    elif b_method == 4:                                          # Deletes from book
        select_book = "SELECT * from book"                          # PRINTS LIST OF BOOKS
        thebooks = execute_read_query(connection, select_book)
        for book in thebooks:
            print(book)
        print("\n\033[1mDELETE EXISTING BOOK\033[0m")
        bsearching = str(input("ENTER the ID of the book you want to DELETE >>>"))
        bsure = input(f"Are you sure you want to delete book {bsearching}? (y/n)")
        if bsure == 'yes' or bsure == 'Yes' or bsure == 'y' or bsure == 'Y':
            cursor = connection.cursor()
            cursor.execute("DELETE FROM book WHERE book_id=?", (bsearching,))
            connection.commit()
            print("\033[1mBOOK DELETED SUCCESSFULLY!\033[0m")
            time.sleep(1)
            print("\033[1mReturning to BOOK MENU...\033[0m")
            time.sleep(1.5)
            books()
        else:
            print("\033[1mDELETION ABORTED, Returning to BOOK MENU...\033[0m")
            time.sleep(1.5)
            books()
    elif b_method == 5:
        print("Returning to Main Menu...")
        time.sleep(1)
        choose()


                                                                    # START
print("Creating Prerequisites...")
time.sleep(1)
print("Connect to SQLite database:")
connection = create_connection("assignment13")
time.sleep(1)
print("Running query to create the person table...")
execute_query(connection, create_customer_table)
time.sleep(1)
print("Running query to create the books table...")
execute_query(connection, create_books_table)
time.sleep(2)
welcome()
choose()

