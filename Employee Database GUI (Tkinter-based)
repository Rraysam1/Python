# Ray Sam
# 05-14-2025
# Employee Database

import tkinter as tk
from tkinter import ttk, messagebox
import pickle

class EmployeeEntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("New Employee Entry")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        self.employee_data = {}
        self.current_id = 1
        self.filename = "employees.dat"
        self.current_index = 0  # To track the current position when navigating records
        self.id_list = []

        self.load_data_from_file()

        # Colors
        self.bg_color = "#e8f5e9"
        self.widget_bg = "#f5f5f5"
        self.accent_color = "#81c784"
        self.text_color = "#333333"
        
        self.root.configure(bg=self.bg_color)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('.', background=self.bg_color, foreground=self.text_color)
        self.style.configure('TLabel', background=self.bg_color, font=('Arial', 11))
        self.style.configure('TButton', font=('Arial', 11), padding=5,
                             background=self.accent_color, foreground='white')
        self.style.configure('TEntry', font=('Arial', 11), padding=5,
                             fieldbackground=self.widget_bg, foreground=self.text_color)
        self.style.map('TButton', background=[('active', '#66bb6a'), ('pressed', '#4caf50')])

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="New Employee Entry", font=('Arial', 16, 'bold')).pack(pady=15)

        form_frame = ttk.Frame(self.root)
        form_frame.pack(pady=10)

        self.entries = {}
        fields = [
            "First Name", "Last Name", "Address", "City", "State",
            "Zip", "Phone Number", "Hourly Rate", "Normal Hours"
        ]

        for i, field in enumerate(fields):
            ttk.Label(form_frame, text=f"{field}:").grid(row=i, column=0, padx=5, pady=5, sticky='e')
            entry = ttk.Entry(form_frame, width=25)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[field.lower().replace(" ", "_")] = entry

        # Button frames
        button_frame1 = ttk.Frame(self.root)
        button_frame1.pack(pady=10)
        ttk.Button(button_frame1, text="Save", command=self.save_data).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame1, text="Clear", command=self.clear_form).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame1, text="Load Data", command=self.load_data_to_form).grid(row=0, column=2, padx=5)
        ttk.Button(button_frame1, text="Close", command=self.root.quit).grid(row=0, column=3, padx=5)

        button_frame2 = ttk.Frame(self.root)
        button_frame2.pack(pady=10)
        ttk.Button(button_frame2, text="First", command=self.show_first_record).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame2, text="Previous", command=self.show_previous_record).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame2, text="Next", command=self.show_next_record).grid(row=0, column=2, padx=5)
        ttk.Button(button_frame2, text="Last", command=self.show_last_record).grid(row=0, column=3, padx=5)

        self.entries["first_name"].focus()

    def save_data(self):
        employee = {}
        for field, entry in self.entries.items():
            employee[field] = entry.get()

        if not employee["first_name"] or not employee["last_name"]:
            messagebox.showwarning("Validation Error", "First Name and Last Name are required.")
            return

        try:
            if employee["hourly_rate"]:
                float(employee["hourly_rate"])
            if employee["normal_hours"]:
                float(employee["normal_hours"])
        except ValueError:
            messagebox.showwarning("Validation Error", "Hourly Rate and Normal Hours must be numeric.")
            return

        self.employee_data[self.current_id] = employee
        self.current_id += 1
        self.save_data_to_file()
        messagebox.showinfo("Success", "Employee data saved.")
        self.clear_form()

    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.entries["first_name"].focus()

    def save_data_to_file(self):
        try:
            with open(self.filename, 'wb') as file:
                pickle.dump(self.employee_data, file)
        except Exception as e:
            messagebox.showerror("Error", f"Error saving data: {str(e)}")

    def load_data_from_file(self):
        try:
            with open(self.filename, 'rb') as file:
                self.employee_data = pickle.load(file)
                if self.employee_data:
                    self.current_id = max(self.employee_data.keys()) + 1
                    self.id_list = sorted(self.employee_data.keys())
        except FileNotFoundError:
            self.employee_data = {}
        except Exception as e:
            messagebox.showerror("Error", f"Error loading file: {str(e)}")

    def load_data_to_form(self):
        if not self.employee_data:
            messagebox.showinfo("No Data", "No employee data found.")
            return
        self.id_list = sorted(self.employee_data.keys())
        self.current_index = 0
        self.display_record(self.id_list[self.current_index])

    def display_record(self, emp_id):
        if emp_id not in self.employee_data:
            return
        employee = self.employee_data[emp_id]
        for field, entry in self.entries.items():
            entry.delete(0, tk.END)
            entry.insert(0, employee.get(field, ""))

    def show_first_record(self):
        if not self.id_list:
            return
        self.current_index = 0
        self.display_record(self.id_list[self.current_index])

    def show_last_record(self):
        if not self.id_list:
            return
        self.current_index = len(self.id_list) - 1
        self.display_record(self.id_list[self.current_index])

    def show_next_record(self):
        if not self.id_list or self.current_index >= len(self.id_list) - 1:
            messagebox.showinfo("End", "No more records.")
            return
        self.current_index += 1
        self.display_record(self.id_list[self.current_index])

    def show_previous_record(self):
        if not self.id_list or self.current_index <= 0:
            messagebox.showinfo("Start", "This is the first record.")
            return
        self.current_index -= 1
        self.display_record(self.id_list[self.current_index])

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeEntryApp(root)
    root.mainloop()
