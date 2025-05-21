import tkinter as tk
from tkinter import messagebox
from quiz_manager_oop import QuizManage
from start_quiz import StartQuiz

root = tk.Tk()
root.withdraw()

if __name__ == "__main__":
    start_quiz = StartQuiz(root)
    file_path = start_quiz.start_quiz_with_file()
    if file_path:  
        QuizManage(root, file_path)
        root.title("Quiz")
        root.geometry("800x450")
        root.configure(bg="light blue")
        root.deiconify()
        root.mainloop()
    else:
        root.destroy()





