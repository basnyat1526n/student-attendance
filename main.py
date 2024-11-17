import mysql.connector
import tkinter as tk
from tkinter import messagebox
import bcrypt
from InstructorInterface import InstructorInterface

from studentInterface import studentInterface

# MySQL Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Dinesh@7',
    'database': 'attendance_system'
}

# Connect to MySQL Database
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

# Register user in the database with hashed password
def register_user(username, password, role):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, hashed_password, role))
        conn.commit()
        messagebox.showinfo("Success", f"{role.capitalize()} '{username}' registered successfully.")
    except mysql.connector.IntegrityError:
        messagebox.showerror("Error", f"Username '{username}' is already taken.")

# Login user and authenticate based on role
def login_user():
    username = entry_username.get()
    password = entry_password.get()

    cursor.execute("SELECT password, role FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
        role = result[1]
        messagebox.showinfo("Success", f"Login successful! Welcome, {role.capitalize()} '{username}'.")
        if role == "teacher":
            teacher_dashboard()
        elif role == "student":
            student_dashboard()
    else:
        messagebox.showerror("Error", "Login failed. Incorrect username or password.")

# Dashboard functions for teacher and student
def teacher_dashboard():
    dashboard = tk.Toplevel(root)
    app = InstructorInterface(dashboard)  # Initialize instructor interface here
    dashboard.title("Teacher Dashboard")
    dashboard.geometry("900x900")

def student_dashboard():
    dashboard = tk.Toplevel(root)
    dashboard.title("Student Dashboard")
    app = studentInterface(dashboard)
    dashboard.geometry("800x600")



# Registration window
def open_registration():
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.geometry("600x400")

    tk.Label(register_window, text="Register New User", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(register_window, text="Username:").pack()
    username = tk.Entry(register_window)
    username.pack()

    tk.Label(register_window, text="Password:").pack()
    password = tk.Entry(register_window, show="*")
    password.pack()

    tk.Label(register_window, text="Role:").pack()
    role = tk.StringVar(value="student")
    role_menu = tk.OptionMenu(register_window, role, "teacher", "student")
    role_menu.pack(pady=5)

    def register():
        register_user(username.get(), password.get(), role.get())
        register_window.destroy()

    tk.Button(register_window, text="Register", command=register, bg="#4CAF50", fg="red").pack(pady=10)

# Close the database connection when the main window is closed
def close_connection():
    cursor.close()
    conn.close()

# Main Application Window
root = tk.Tk()
root.title("Login System")
root.geometry("600x400")
root.config(bg="#f0f0f0")

# Title label
title_label = tk.Label(root, text="Student & Teacher Login", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# Frame for login inputs
login_frame = tk.Frame(root, bg="#f0f0f0")
login_frame.pack(pady=20)

# Username label and entry
tk.Label(login_frame, text="Username:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_username = tk.Entry(login_frame, font=("Arial", 12))
entry_username.grid(row=0, column=1, padx=5, pady=5)

# Password label and entry
tk.Label(login_frame, text="Password:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_password = tk.Entry(login_frame, show="*", font=("Arial", 12))
entry_password.grid(row=1, column=1, padx=5, pady=5)

# Login and Register buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack()

tk.Button(button_frame, text="Login", command=login_user, width=10, bg="#4CAF50", fg="red", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=10)
tk.Button(button_frame, text="Register", command=open_registration, width=10, bg="#2196F3", fg="red", font=("Arial", 12)).grid(row=0, column=1, padx=5, pady=10)

# Ensure database closes on window close
root.protocol("WM_DELETE_WINDOW", lambda: [close_connection(), root.destroy()])

root.mainloop()
