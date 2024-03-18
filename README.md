Assignment 3 Q1 - COMP3005

Ahraaz Supra - 101266714

**Video: https://youtu.be/4qStYTnr2zw**

Database Setup:

1. Ensure that PostgreSQL is installed and running on your system.

2. Create a PostgreSQL database. 

3. Use the following SQL command to create the students table:

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

4. Populate the table with initial records using the following SQL command:

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

Application Setup:

1. Ensure Python3 is installed on your system.

2. Install the psycopg2 library using pip:

pip3 install psycopg2-binary

3. In the database.py file, update the connect_db function with your actual database connection details:

connect = psycopg2.connect("dbname='yourDBname' user='postgres' host='localhost' password='yourPassword'")

Replace 'yourDBname' to your Database's name. And replace 'yourPassword' with your actual database password.

Available Functions:

- getAllStudents(): Retrieves and displays all student records.
- addStudent(first_name, last_name, email, enrollment_date): Adds a new student record.
- updateStudentEmail(student_id, new_email): Updates the email address for a specified student.
- deleteStudent(student_id): Deletes a student record.

#test cases you can use

#displays all student records 

getAllStudents()

#adds a new student

addStudent('New', 'Student', 'newStudent@example.com', '2022-02-02')

#updates a student's email

updateStudentEmail(1, 'updatedEmail@example.com')

#deletes a student record

deleteStudent(2)

Files:

database.sql

database.py

README.md
