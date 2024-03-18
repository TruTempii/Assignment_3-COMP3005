#Assignment 3 Q1 - COMP3005
#Ahraaz Supra - 101266714

#importing PostgreSQL library
import psycopg2

#function to connect to the database
def connect_db():
    try:
        #connecting to the database using given parameters for authentication
        connect = psycopg2.connect("dbname = 'School' user = 'postgres' host = 'localhost' password = '000111'")
        return connect
    except Exception as e:
        #if there was an error, print the exception
        print("Database connection failed: {}".format(e))

#function to get all the students
def getAllStudents():
    #connecting to the database
    connect = connect_db()
    #cursor object to traverse through database
    current = connect.cursor()
    #executing query
    current.execute("SELECT * FROM students ORDER BY student_id ASC")
    #getting all rows of the query
    rows = current.fetchall()
    #printing each row of the query
    for row in rows:
        print(row)
    #closing cursor object
    current.close()
    #closing connection to the database
    connect.close()

#function to add a student
def addStudent(first_name, last_name, email, enrollment_date):
    #connecting to the database
    connect = connect_db()
    #cursor object to traverse through database
    current = connect.cursor()
    #executing query
    current.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date))
    #saving changes
    connect.commit()
    #closing cursor object
    current.close()
    #closing connection to the database
    connect.close()

#function to update a student's email
def updateStudentEmail(student_id, new_email):
    #connecting to the database
    connect = connect_db()
    #cursor object to traverse through database
    current = connect.cursor()
    #executing query
    current.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    #saving changes
    connect.commit()
    #closing cursor object
    current.close()
    #closing connection to the database
    connect.close()

#function to delete a student
def deleteStudent(student_id):
    #connecting to the database
    connect = connect_db()
    #cursor object to traverse through database
    current = connect.cursor()
    #executing query
    current.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    #saving changes
    connect.commit()
    #closing cursor object
    current.close()
    #closing connection to the database
    connect.close()

#test cases you can use
    
#getAllStudents()
#addStudent('New', 'Student', 'newStudent@example.com', '2022-02-02')
#updateStudentEmail(1, 'updatedEmail@example.com')
#deleteStudent(2)
