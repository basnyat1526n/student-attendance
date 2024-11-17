Project student attendance


Introduction:
The student attendance Management System is a software designed and developed to track the students in educational institutions. We have developed this sophisticated software to track the students attendance, the classes the students are enrolled in. It is user friendly, and creates a smooth workflow. The feature we have included in this software are mentioned below:
User Registration: we have created a secure registration for teachers and students. 
Role-Based Login: There are two separate dashboards for teachers and students.
Password Security: we have hashed the password using bycrypt..
Attendance Tracking: Teachers are able to mark and manage the  student attendance records.
Dynamic Dashboard: Customised interfaces for each user role.such as students can check the classes they are enrolled in and in which classes it is being held.
Scalable Database: we used MySQL for efficient data storage.

Technologies: 
The technologies or library we used to create this software are: 
For the backend we used Python.
For Database,  MySQL has been used. 
Authentication: bcrypt (for password hashing)
Frontend GUI: tkinter was used
Version Control: Git and GitHub

Installation
Clone the Repository:
To clone our project from github, the link below could be used to clone the project in your respective computer with the help of the command line or the coding platform being used. 
git clone https://github.com/basnyat1526n/student-attendance.git
Install Dependencies:
For dependency first, ensure the python has been installed and then using the mentioned link command you can download the package for mySQL connector. 
pip install mysql-connector-python.
pip install bcrypt
Set Up the Database
For database we used MySQL, we can install it with the link mentioned
mysql -u root -p attendance_system < schema.sql
Update Database Configuration:
To connect our database to the main code we have included the code where an individual has to put their own credentials(user and password) and connect their own database system they have created in MySQL workbench. 
And to execute the program, we have to run the main.py file.

Student Dashboard
View personal attendance details.
Database Schema: 
For the database of the application we have used following tables,
Users:
id: unique key
username: Student name
password: password(crypted)
role: Role (teacher or student)

Attendance
id: unique key
student_id: unique key referencing users
date: Attendance date
status: Present/Absent

We have included some screen shots of our application, for the ease of user understanding and to make it easy to use.
Login portal:

Here, if you are a new user you can click on register and if you have already been registered then you can put your credentials and login. 
For registration: 
The credentials like username and password needs to be filled. And based on the user, the roles can be selected such as either teacher or student. 
And most importantly the passwords have been hashed with bycrpt program

From the teacher portal, If the new students need to be registered then, the student id is referred to the unique id of the student, class id and course are the class and courses, the student is currently enrolled in, and the student name.
Here you could search the classes if you need to attend. 

After searching the classes, the students enrolled will appear in the class and to mark them either present or absent; double click is necessary on the status of the student. 

To check the record of the student, we have to click on view saved attendace, class id and date needs to be filled, and after clicking on view attendance, students attendance will appear on the screen from the mentioned data. 

Student portal:
When the students have logged into the portal they will be able to see lists of courses they have been enrolled in, on screen. 
 
Future Improvements
Add real-time notifications for attendance updates.
Implement reporting features for attendance summaries.
Enhance UI using modern libraries like PyQt or tkinter.ttk.
Add support for biometric or QR-code-based attendance marking.
New subjects registration system. 
Change the schedule for the classes. 
Change password ater the password has been forgotten. 
Conclusion: 
The student attendance management system is user-friendnly prototype application designed to streamline attendance tracking for teachers and students, by integrating secure login system, role based access, and a scalable database, it ensure efficiency and reliability in managing academic records. Though, there are still alot of things which needs to be improved before publishing it publicly to user. 
