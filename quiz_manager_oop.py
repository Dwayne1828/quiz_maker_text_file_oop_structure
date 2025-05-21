import tkinter as tk
from tkinter import messagebox
from choices_radio_btn import ChoicesRadioBtn
from quiz_reader import QuizReader
from start_quiz import StartQuiz

class QuizManage():
    def __init__(self, root, file_name): 
        self.file_name = file_name #Initialize the file name
        
        self.root = root
        self.choosed_answer = tk.IntVar(master=root)
        
        self.question_no = 0
        self.correct_ans = 0
        self.wrong_ans = 0
        self.question_reader = QuizReader(self.file_name) #Creates an instance of the QuizReader class
        self.questions = self.question_reader.quiz_reader() #Calls the quiz_reader method to read the quiz file and store the questions

        self.display_question = tk.Label(self.root, text="Ready?", font=("Helvetica", 25, "bold"), 
                                         fg="blue", bg="light blue") #Creates a label to display the quiz questions
        self.display_question.place(relx=0.5, rely=0.4, anchor="center")
        self.display_question.config(font=("Arial", 16), wraplength=700) #Sets the font and wrap length for the label
        
        self.next_button = tk.Button(self.root, text="Let's Go!", command=self.next_question, 
                                     bg="#4caf50", fg="white", font=("Helvetica", 12)) #Creates a button to navigate to the next question
        self.next_button.place(relx=0.5, rely=0.6, anchor="center")
        self.next_button.config(font=("Arial", 10), width=10, height=2) #Sets the font, width, and height for the button

        
    def next_question(self):
        if self.question_no < len(self.questions):   
            self.next_button.config(text="Continue", command=self.current_check_answer, 
                                    bg="blue", fg="white", font=("Helvetica", 12)) #Changes the button text to "Next"
            self.next_button.place(relx=0.5, rely=0.7, anchor="center") #Places the button in the center of the window
            
            self.radio_btn = ChoicesRadioBtn(self.root, self.choosed_answer)
            self.radio_btn = self.radio_btn.create_radio_buttons()
            self.options_question_no()
            
            self.display_question.config(text=self.questions[self.question_no]["question"].strip(), 
                                         font=("Helvetica", 14), wraplength=600, bg="light blue", fg="#222")
            self.display_question.place(relx=0.5, rely=0.3, anchor="center") #Displays the question in the label
            self.question_no += 1


    def current_check_answer(self):
        if self.choosed_answer.get() == -1:  # Check if no answer is selected
            messagebox.showinfo("No Selection", "Please select an answer before proceeding.")
            return

        self.check_answer() #Calls the check_answer method to check if the answer is correct

    
    def check_answer(self):
        answer_mapping = {"a": 0, "b": 1, "c": 2, "d": 3}  # Map string answers to indices
        
        try:
            selected_answer = self.choosed_answer.get()  # Get the selected answer as an integer
            correct_answer = answer_mapping[self.questions[self.question_no - 1]["answer"]]  # Map correct answer to index

            self.root.after(1000, self.advance_question)  # Delay before moving to the next question

            if selected_answer == correct_answer:
                self.radio_btn[selected_answer].config(fg="green") # Highlight correct answer
                self.correct_ans += 1  
            else:
                self.radio_btn[selected_answer].config(fg="red")  # Highlight incorrect answer
                self.radio_btn[correct_answer].config(fg="green") # Highlight the correct answer
                self.wrong_ans += 1 
        except (KeyError, IndexError):
            messagebox.showinfo("Error", "An error occurred while checking the answer.")


    def advance_question(self):
        if self.question_no < len(self.questions):  
            self.display_question.config(text=self.questions[self.question_no]["question"].strip(), 
                                         font=("Helvetica", 14), wraplength=600, bg="light blue", fg="#222") #Displays the question
            self.options_question_no()
            self.question_no += 1
        else:
            self.display_question.config(text="Quiz Completed!", font=("Helvetica", 25), bg="light blue")
            self.display_question.place(relx=0.5, rely=0.4, anchor="center")
            self.next_button.config(text="Finish", command=self.root.quit, bg="green", fg="white")
            self.next_button.place(relx=0.5, rely=0.6, anchor="center")
            
            for btn in self.radio_btn:
                btn.place_forget()
            
            self.quiz_result() #Calls the quiz_result method to display the result
            self.ask_to_restart()


    def ask_to_restart(self):
        from start_quiz import StartQuiz
        result = messagebox.askyesno("Quiz Finished", "Do you want to choose a new file?")
        
        if result:
            for widget in self.root.winfo_children():
                widget.destroy()

            restart_quiz = StartQuiz(self.root)
            restart_quiz.start_quiz_with_file()
        else:
            self.root.quit()


    def quiz_result(self):
        score = f"Your score: {self.correct_ans}/{len(self.questions)}\n Wrong: {self.wrong_ans}" #Calculates the number of correct answers
        messagebox.showinfo(f"Quiz Result", f"{score}") #Displays the result in a message box


    def options_question_no(self):
        radio_button = 0
        self.choosed_answer.set(-1)  # Reset the selected answer

        for choices in self.questions[self.question_no]["choices"]:
            self.radio_btn[radio_button]['text'] = choices.split(": ")[1].strip()
            self.radio_btn[radio_button].config(fg="black")   # Set the text of the radio button
            radio_button += 1