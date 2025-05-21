import tkinter as tk
from tkinter import messagebox
from quiz_manager_oop import QuizManage
from start_quiz import StartQuiz

root = tk.Tk()
root.withdraw()
file_path = StartQuiz(root)
file_path = file_path.start_quiz_with_file()
QuizManage(root, file_path)
root.title("Quiz")
root.geometry("800x450")
root.configure(bg="light blue")
root.deiconify()
root.mainloop()

if __name__ == "__main__":
    StartQuiz.start_quiz_with_file(root)



