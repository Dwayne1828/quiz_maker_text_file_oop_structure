import os 
from datetime import datetime
from file_maker import FileMaker
from question_checker import QuestionChecker

#Function to asks the user for questions and answers and writes them to the file
def create_quiz():
    #Get the file name from the user
    file_name = FileMaker().file_maker()
    
    #Starts the Question number at 1
    question_number = QuestionChecker.question_checker(file_name)
    
    #Open the file in append mode to create if exists or create a new one
    with open(file_name, "a") as quiz_file:
        #Get the current date and time
        now = datetime.now()
        current_time_date = now.strftime("%m/%d/%Y %H:%M:%S")

        quiz_file.write(f"Quiz Created - {current_time_date}\n")
        quiz_file.write("\n")

        #While true for a loop to allow the user to decide when to stop entering questions
        while True: 
            question = input("Enter a question: ") 
            quiz_file.write(f"Question {question_number}:\n {question}\n") 
            question_number += 1

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
                print(f"Quiz saved to {file_name}")
                break

create_quiz()

