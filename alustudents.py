#!/usr/bin/env python3

#importing the necessary libraries for the task
import mysql.connector
from mysql.connector import Error

#Creating the connection to my database
try:

    my_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "alu"
        )

#Creating a cursor to allow me interact within mysql database

    cursor = my_db.cursor()
    def add_student(name, surname, age, course, marks):

        my_queries = ''' INSERT INTO alustudents (Name, Surname, Age, Course, Marks) VALUES
            (%s, %s, %s, %s, %s)'''
        my_data =(name, surname, age, course, marks)
        try:


           cursor.execute(my_queries, my_data)
           my_db.commit()
           print("Student added succesfully")
        except Error as e:
            print(f"Failed to add student with error: {e}")
            my_db.rollback()

    name = input("Enter your name:")
    surname = input("Enter your surname:")
    age = int(input("Enter your age number:"))
    course = input("Enter a course you are taking:")
    marks = int(input("Enter your marks:"))

    add_student(name, surname, age, course, marks)

except Error as e:
    print(f"failed to connect to the database due to this error: {e}")

finally:
    if "cursor" in locals() and cursor:
        cursor.close()

    if "my_db" in locals() and my_db:
        my_db.close()

    print("Database connection closed.")
