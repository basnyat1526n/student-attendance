import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from tkcalendar import Calendar
import datetime


class InstructorInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Instructor Attendance Interface")
        self.root.geometry("1200x1000")


        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Dinesh@7',  # Update with your MySQL password
            'database': 'attendance_system'
        }
        self.conn = mysql.connector.connect(**self.db_config)
        self.cursor = self.conn.cursor()

        self.create_widgets()

    def create_widgets(self):
        # Tab control for Registration and Attendance
        self.tab_control = ttk.Notebook(self.root)

        # Student Registration Tab
        self.registration_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.registration_tab, text="Student Registration")

        # Record Attendance Tab
        self.record_attendance_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.record_attendance_tab, text="Record Attendance")

        self.view_attendance_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.view_attendance_tab, text="View saved Attendance")

        self.tab_control.pack(expand=1, fill="both")

        # Registration Tab Layout
        tk.Label(self.registration_tab, text="Student ID:").grid(row=0, column=0, padx=10, pady=10)
        self.student_id_entry = tk.Entry(self.registration_tab)
        self.student_id_entry.grid(row=0, column=1, padx=10, pady=10)


        tk.Label(self.registration_tab, text="class id:").grid(row=1, column=0, padx=10, pady=10)
        self.class_id_entry = tk.Entry(self.registration_tab)
        self.class_id_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.registration_tab, text="Student Name:").grid(row=2, column=0, padx=10, pady=10)
        self.student_name_entry = tk.Entry(self.registration_tab)
        self.student_name_entry.grid(row=2, column=1, padx=10, pady=10)


        tk.Label(self.registration_tab, text="Course:").grid(row=3, column=0, padx=10, pady=10)
        self.course_entry = tk.Entry(self.registration_tab)
        self.course_entry.grid(row=3, column=1, padx=10, pady=10)


        tk.Button(self.registration_tab, text="Register Student", command=self.register_student).grid(
            row=5, column=0, columnspan=2, pady=10)

        # Attendance Tab Layout
        tk.Label(self.record_attendance_tab, text="Class ID:").grid(row=0, column=0, padx=2, pady=5)
        self.class_id_entrys = tk.Entry(self.record_attendance_tab)
        self.class_id_entrys.grid(row=0, column=1, padx=2, pady=5)

        # Create the label and calendar widget
        tk.Label(self.record_attendance_tab, text="Date:").grid(row=2, column=0, padx=10, pady=10)
        self.date_entry = tk.Entry(self.record_attendance_tab, font=("Arial", 12), justify="center")

        # Get the current date and time
        current_date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.date_entry.insert(0, current_date_time)  # Insert it into the entry field

        # Grid the calendar widget
        self.date_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self.record_attendance_tab, text="View Attendance", command=self.view_students).grid(
            row=3, column=1, columnspan=2, pady=10)

        # Inside the create_widgets method (in the View Attendance tab section)
        tk.Label(self.view_attendance_tab, text="Class ID:").grid(row=0, column=0, padx=10, pady=10)
        self.class_id_entryss = tk.Entry(self.view_attendance_tab)
        self.class_id_entryss.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.view_attendance_tab, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=10)
        self.date_entrys = tk.Entry(self.view_attendance_tab)
        self.date_entrys.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.view_attendance_tab, text="View Attendance", command=self.view_saved_attendance).grid(
            row=2, column=0, columnspan=2, pady=10
        )

        # Attendance Treeview
        self.attendance_tree = ttk.Treeview(self.record_attendance_tab, columns=("ID", "Name", "Status","Course"),
                                            show="headings")
        self.attendance_tree.heading("ID", text="Student ID")
        self.attendance_tree.heading("Name", text="Student Name")
        self.attendance_tree.heading("Status", text="Status")
        self.attendance_tree.column("Status", width=80)
        self.attendance_tree.heading("Course", text="Course")
        self.attendance_tree.grid(row=4, column=0, columnspan=2, pady=10)

        self.attendance_tree.bind("<Double-1>", self.toggle_attendance)

        # Save Attendance Button
        tk.Button(self.record_attendance_tab, text="Save Attendance", command=self.save_attendance).grid(
            row=5, column=0, columnspan=2, pady=10)


        # attendance view treeview
        self.attendance_view_tree = ttk.Treeview(self.view_attendance_tab, columns=("ID", "Name", "Status","Course","Date"),
                                            show="headings")
        self.attendance_view_tree.heading("ID", text="Student ID")
        self.attendance_view_tree.heading("Name", text="Student Name")
        self.attendance_view_tree.heading("Status", text="Status")
        self.attendance_view_tree.column("Status", width=80)
        self.attendance_view_tree.heading("Course", text="Course")
        self.attendance_view_tree.heading("Date", text="Date")
        self.attendance_view_tree.grid(row=4, column=0, columnspan=2, pady=10)

        self.attendance_view_tree.bind("<Double-1>", self.toggle_attendance)

    # implementation of register student
    def register_student(self):
        student_id = self.student_id_entry.get()
        class_id= self.class_id_entry.get()
        student_name = self.student_name_entry.get()
        course = self.course_entry.get()

        if not student_id or not student_name:
            messagebox.showerror("Error", "Please enter both student ID and name.")
            return


        try:
            self.cursor.execute("INSERT INTO students (student_id, name,course) VALUES ( %s,%s,%s)", (student_id,student_name,course))
            self.cursor.execute(
                "INSERT INTO attendance (student_id,class_id) VALUES (%s,%s)",
                (student_id,class_id)
            )

            self.conn.commit()
            messagebox.showinfo("Success", f"Student '{student_name}' registered successfully!")
            self.student_id_entry.delete(0, tk.END)
            self.class_id_entry.delete(0, tk.END)
            self.student_name_entry.delete(0, tk.END)
            self.course_entry.delete(0, tk.END)

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")

    def view_students(self):
        class_ids = self.class_id_entrys.get()
        if not class_ids:
            messagebox.showerror("Error", "Please enter a class ID.")
            return

        try:
            self.cursor.execute("""
                SELECT students.student_id, students.name,attendance.present ,students.course
                FROM attendance
                JOIN students ON attendance.student_id = students.student_id
                WHERE attendance.class_id = %s
            """, (class_ids,))

            students = self.cursor.fetchall()

            for item in self.attendance_tree.get_children():
                self.attendance_tree.delete(item)

            for student in students:
                self.attendance_tree.insert("", "end", values=(student[0], student[1],student[2],student[3]))

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")

    # implementation of toggle status
    def toggle_attendance(self, event):
        selected_item = self.attendance_tree.focus()
        current_values = self.attendance_tree.item(selected_item, "values")

        new_status = "Present" if current_values[2] == "Absent" else "Absent"
        self.attendance_tree.item(selected_item, values=(current_values[0], current_values[1], new_status,current_values[3]))

    # implementation of saving attendance
    def save_attendance(self):
        class_ids = self.class_id_entrys.get()  # Ensure you're getting class_id correctly
        date_time = self.date_entry.get()  # Current date and time

        if not class_ids:
            messagebox.showerror("Error", "Please enter a class ID.")
            return

        try:
            # Loop through each item in the attendance tree view
            for item in self.attendance_tree.get_children():
                student_id = self.attendance_tree.item(item)["values"][0]  # Get student_id
                status = self.attendance_tree.item(item)["values"][2]  # Get attendance status
                present_int = 1 if status == "Present" else 0  # Convert status to 1 or 0

                # Update attendance with student_id, present status, class_id, and current date_time
                self.cursor.execute("""
                    UPDATE attendance
                    SET present = %s
                    WHERE student_id = %s AND class_id = %s
                """, (present_int,student_id, class_ids))

                # Update or insert the date field in the students table
                self.cursor.execute("""
                    UPDATE students
                    SET date = %s
                    WHERE student_id = %s
                """, (date_time, student_id))

            self.conn.commit()
            messagebox.showinfo("Success", "Attendance updated successfully!")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")

    # implementation of view the saved data
    def view_saved_attendance(self):
        class_idss = self.class_id_entryss.get()
        date = self.date_entrys.get()

        if not class_idss or not date:
            messagebox.showerror("Error", "Please enter both class ID and date.")
            return

        try:
            query = """
                SELECT 
                    s.student_id,
                    s.name,
                    a.present,
                    s.course,
                    s.date
                FROM 
                    students s
                JOIN 
                    attendance a
                ON 
                    s.student_id = a.student_id
                WHERE 
                    a.class_id = %s AND s.date = %s;
            """
            self.cursor.execute(query, (class_idss, date))
            results = self.cursor.fetchall()

            # Clear existing rows in the treeview
            for item in self.attendance_view_tree.get_children():
                self.attendance_view_tree.delete(item)

            # Insert retrieved rows into the treeview
            for row in results:
                self.attendance_view_tree.insert("", "end", values=row)

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")

    def __del__(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = InstructorInterface(root)
    root.mainloop()
