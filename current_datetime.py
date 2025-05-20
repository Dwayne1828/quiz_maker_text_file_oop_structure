from datetime import datetime

class DateTime:
    def current_datetime(file_name):
        with open(file_name, "a") as quiz_file:
                #Get the current date and time
                now = datetime.now()
                current_time_date = now.strftime("%m/%d/%Y %H:%M:%S")

                quiz_file.write(f"Quiz Created - {current_time_date}\n")
                quiz_file.write("\n")