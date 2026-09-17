import tkinter as tk
from tkinter import ttk

class StudentAttendance:
    def __init__(self, root):
        self.root = root
        self.root.title('Student Attendance')
        self.root.geometry('800x600')

        # Create main frames
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(fill='x')

        self.middle_frame = tk.Frame(self.root)
        self.middle_frame.pack(fill='both', expand=True)

        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(fill='x')

        # Create top frame widgets
        self.top_label = tk.Label(self.top_frame, text='Student Attendance', font=('Arial', 24))
        self.top_label.pack(pady=20)

        self.map_button = tk.Button(self.top_frame, text='Map View')
        self.map_button.pack(side='left', padx=10)

        self.list_button = tk.Button(self.top_frame, text='List View')
        self.list_button.pack(side='left', padx=10)

        # Create middle frame widgets
        self.middle_frame_label = tk.Label(self.middle_frame, text='Student Attendance', font=('Arial', 18))
        self.middle_frame_label.pack(pady=20)

        self.attendance_tree = ttk.Treeview(self.middle_frame, selectmode='browse')
        self.attendance_tree.pack(fill='both', expand=True)

        # Create bottom frame widgets
        self.bottom_label = tk.Label(self.bottom_frame, text='Total Students: 0')
        self.bottom_label.pack(side='left', padx=10)

        self.bottom_button = tk.Button(self.bottom_frame, text='Mark Attendance')
        self.bottom_button.pack(side='right', padx=10)

        # Create treeview columns
        self.attendance_tree['columns'] = ('Name', 'Date', 'Status')

        self.attendance_tree.column('#0', width=0, stretch=tk.NO)
        self.attendance_tree.column('Name', anchor=tk.W, width=100)
        self.attendance_tree.column('Date', anchor=tk.W, width=100)
        self.attendance_tree.column('Status', anchor=tk.W, width=100)

        self.attendance_tree.heading('#0', text='', anchor=tk.W)
        self.attendance_tree.heading('Name', text='Name', anchor=tk.W)
        self.attendance_tree.heading('Date', text='Date', anchor=tk.W)
        self.attendance_tree.heading('Status', text='Status', anchor=tk.W)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = StudentAttendance(root)
    app.run()