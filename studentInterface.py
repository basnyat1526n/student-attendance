import tkinter as tk
from tkinter import ttk

class studentInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Routine")
        self.root.geometry("800x400")

        # Create School Routine Treeview
        self.create_routine_treeview()

    def create_routine_treeview(self):
        # Define columns for the Treeview
        columns = ("day", "subject", "time", "teacher", "location")

        # Set up the Treeview with columns
        self.routine_tree = ttk.Treeview(self.root, columns=columns, show="headings")

        # Define column headings
        self.routine_tree.heading("day", text="Day")
        self.routine_tree.heading("subject", text="Subject")
        self.routine_tree.heading("time", text="Time")
        self.routine_tree.heading("teacher", text="Teacher")
        self.routine_tree.heading("location", text="Location")

        # Define column widths
        self.routine_tree.column("day", width=100)
        self.routine_tree.column("subject", width=150)
        self.routine_tree.column("time", width=100)
        self.routine_tree.column("teacher", width=150)
        self.routine_tree.column("location", width=100)

        # Pack the Treeview
        self.routine_tree.pack(fill="both", expand=True)

        # Add some dummy data to the routine
        routine_data = [
            ("Monday", "Mathematics", "9:00 AM - 10:00 AM", "Mr. Smith", "Room 101"),
            ("Monday", "English", "10:15 AM - 11:15 AM", "Ms. Johnson", "Room 102"),
            ("Tuesday", "Science", "9:00 AM - 10:00 AM", "Dr. White", "Room 201"),
            ("Tuesday", "History", "10:15 AM - 11:15 AM", "Mr. Brown", "Room 202"),
            ("Wednesday", "Art", "9:00 AM - 10:00 AM", "Ms. Green", "Room 103"),
            ("Wednesday", "Physical Education", "10:15 AM - 11:15 AM", "Coach Blue", "Gym"),
            ("Thursday", "Mathematics", "9:00 AM - 10:00 AM", "Mr. Smith", "Room 101"),
            ("Thursday", "Chemistry", "10:15 AM - 11:15 AM", "Dr. Black", "Lab 1"),
            ("Friday", "Biology", "9:00 AM - 10:00 AM", "Dr. Gray", "Room 104"),
            ("Friday", "Music", "10:15 AM - 11:15 AM", "Ms. Melody", "Room 105"),
        ]

        # Insert dummy data into the Treeview
        for entry in routine_data:
            self.routine_tree.insert("", "end", values=entry)


# Run the Student Dashboard application
if __name__ == "__main__":
    root = tk.Tk()
    app = studentInterface(root)
    root.mainloop()
