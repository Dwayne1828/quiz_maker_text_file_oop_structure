from file_maker import FileMaker
from question_checker import QuestionChecker
from current_datetime import DateTime

class QuizCreate:
    def __init__(self):
        self.file_name = FileMaker().file_maker()                                  #Get the file name from the user
        self.question_number = QuestionChecker.question_checker(self.file_name)     #Starts the Question number at 1
        
        #Get the current date and time
        DateTime.current_datetime(self.file_name) #Write the date and time to the file

    #Method to asks the user for questions and answers and writes them to the file
    def quiz_content(self):
        #Open the file in append mode to create if exists or create a new one
        with open(self.file_name, "a") as quiz_file:
            #While true for a loop to allow the user to decide when to stop entering questions
            while True: 
                question = input("Enter a question: ") 
                quiz_file.write(f"Question {self.question_number}:\n {question}\n") 
                self.question_number += 1

                #Ask the user for choices 
                for option in ["a", "b", "c", "d"]: 
                    choice = input(f"Enter choice {option}: ")
                    quiz_file.write(f"Choice {option}: {choice}\n")
                    
                #Ask the user for the correct answer
                while True:
                    answer = input("Enter the correct answer (a, b, c, d): ")
                    if answer in ["a", "b", "c", "d"]:
                        quiz_file.write(f"Answer: {answer}\n")
                        quiz_file.write("\n")
                        break
                    else:
                        print("Invalid answer. Please enter a, b, c, or d.")
                        continue
                    
                #Ask the user if they want to add another question
                another = input("Do you want to add another question? (yes/no): ")
                if another.lower().strip() != "yes":
                    print("Quiz created successfully!")
                    print(f"Quiz saved to {self.file_name}")
                    break