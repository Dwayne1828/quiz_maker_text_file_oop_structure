import os 

class QuestionChecker:
    def question_checker(file_name):
        #Check if the file exists, if not return 0
        if not os.path.exists(file_name): 
            return 1
        
        with open(file_name, "r") as quiz_file: 
            lines = quiz_file.readlines()
            for line in reversed(lines):
                if line.startswith("Question"):
                    #Get the question number from the line
                    try:   
                        question_number = int(line.split()[1].strip(":"))
                        return question_number + 1
                    except (ValueError, IndexError):
                        continue
        
        return 1 