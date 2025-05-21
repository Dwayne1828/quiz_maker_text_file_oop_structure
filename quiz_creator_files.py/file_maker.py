import os

class FileMaker:
    def file_maker(self):
        while True:   
            file_name = input("Enter the file name for your quiz: ").strip()
            #Check if the file name ends with .txt, if not add it
            if not file_name.endswith(".txt"):
                file_name += ".txt"

            #Check if the file already exists, if it does ask the user if they want to edit it or create a new one
            if os.path.exists(file_name): 
                edit = input("File already exists. Do you wish to edit the file? (yes/no): ")
                if edit.lower().strip() == "yes": 
                    return file_name
                elif edit.lower().strip() == "no": 
                    ask_again = input("Do you want to create a new file? (yes/no): ")
                    if ask_again.lower().strip() == "yes": 
                        continue
                    else: 
                        print("Exiting...")
                        exit()
            #If the file does not exist, return the file name       
            else: 
                return file_name