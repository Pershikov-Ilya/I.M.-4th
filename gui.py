import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog, simpledialog
from back import SimpleFileSystem


class FileSystemGUI:
    def __init__(self, root):
        self.fs = SimpleFileSystem("my_files")

        self.root = root
        self.root.title("Simple File System GUI")

        # Set the window size and center it on the screen
        window_width = 600
        window_height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        # Set a nice background color
        root.configure(bg='lightblue')

        # Use ttk for modern widgets
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12), padding=10)

        # Buttons
        self.create_button = ttk.Button(root, text="Create File", command=self.create_file)
        self.create_button.pack(pady=5)

        self.read_button = ttk.Button(root, text="Read File", command=self.read_file)
        self.read_button.pack(pady=5)

        self.write_button = ttk.Button(root, text="Write File", command=self.write_file)
        self.write_button.pack(pady=5)

        self.delete_button = ttk.Button(root, text="Delete File", command=self.delete_file)
        self.delete_button.pack(pady=5)

        self.search_button = ttk.Button(root, text="Search File", command=self.search_file)
        self.search_button.pack(pady=5)

        self.info_button = ttk.Button(root, text="Show Info", command=self.show_info)
        self.info_button.pack(pady=5)

        # Treeview for displaying files
        self.tree_frame = ttk.Frame(root)
        self.tree_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set)

        # Define columns
        self.file_tree['columns'] = ("file_name",)

        # Format columns
        self.file_tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column
        self.file_tree.column("file_name", anchor=tk.W, width=300)

        # Create headings
        self.file_tree.heading("#0", text="", anchor=tk.W)  # Hide the first column heading
        self.file_tree.heading("file_name", text="Files:", anchor=tk.W)

        self.file_tree.pack(fill=tk.BOTH, expand=True)

        self.tree_scroll.config(command=self.file_tree.yview)

        # Load initial file list
        self.update_file_list()

    def create_file(self):
        file_name = simpledialog.askstring("Create File", "Enter file name:", parent=self.root)
        if file_name:
            result = self.fs.create_file(file_name)
            messagebox.showinfo("Create File", result, parent=self.root)
            self.update_file_list()

    def read_file(self):
        file_name = simpledialog.askstring("Read File", "Enter file name:", parent=self.root)
        if file_name:
            content = self.fs.read_file(file_name)
            messagebox.showinfo("Read File", content, parent=self.root)

    def write_file(self):
        file_name = simpledialog.askstring("Write File", "Enter file name:", parent=self.root)
        if file_name:
            content = simpledialog.askstring("Write File", "Enter content:", parent=self.root)
            if content is not None:
                result = self.fs.write_file(file_name, content)
                messagebox.showinfo("Write File", result, parent=self.root)

    def delete_file(self):
        file_name = simpledialog.askstring("Delete File", "Enter file name:", parent=self.root)
        if file_name:
            result = self.fs.delete_file(file_name)
            messagebox.showinfo("Delete File", result, parent=self.root)
            self.update_file_list()

    def search_file(self):
        query = simpledialog.askstring("Search File", "Enter filename or content to search:", parent=self.root)
        if query:
            result = self.fs.search_file(query)
            messagebox.showinfo("Search File", result, parent=self.root)

    def show_info(self):
        info = self.fs.show_info()
        messagebox.showinfo("Show Info", info, parent=self.root)

    def update_file_list(self):
        for item in self.file_tree.get_children():
            self.file_tree.delete(item)

        files_list = self.fs.list_files()

        for file in files_list:
            self.file_tree.insert("", tk.END, values=(file,))