from tkinter import messagebox, filedialog

class StartQuiz:
    def __init__(self, root):
        self.root = root

    def start_quiz_with_file(self):
        # Open a file dialog to select a quiz file
        file_path = filedialog.askopenfilename(title="Select Quiz File", 
                                               filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        
        if file_path:
            return file_path
        else:
            result = messagebox.askyesno("No File Selected", "You must select a quiz file to start.\n Do you wish to Continue?")
            if result:
                return self.start_quiz_with_file()
            else: 
                self.root.quit()
                return None
                