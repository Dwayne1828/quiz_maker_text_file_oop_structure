import tkinter as tk
from tkinter import messagebox, filedialog
from quiz_manager_oop import QuizManage

class StartQuiz:
    def start_quiz_with_file(root):
        # Open a file dialog to select a quiz file
        file_path = filedialog.askopenfilename(title="Select Quiz File", 
                                            filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        
        if file_path:
            QuizManage(root, file_path)
            root.title("Quiz")
            root.geometry("800x450")
            root.configure(bg="light blue")
            root.deiconify()
            root.mainloop()
        else:
            result = messagebox.askyesno("No File Selected", "You must select a quiz file to start.\n Do you wish to Continue?")
            if result:
                StartQuiz.start_quiz_with_file(root)
            else: 
                root.quit()
                

root = tk.Tk()
root.withdraw()
if __name__ == "__main__":
    StartQuiz.start_quiz_with_file(root)



