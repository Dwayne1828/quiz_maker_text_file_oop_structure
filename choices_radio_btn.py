import tkinter as tk

class ChoicesRadioBtn:
    def __init__(self, root, choosed_answer):
        self.root = root
        self.choosed_answer = choosed_answer
        self.radio_buttons = []

    def create_radio_buttons(self):
        rely = 0.4

        while len(self.radio_buttons) < 4:
            radio_btn = tk.Radiobutton(self.root, text="", 
                                       variable=self.choosed_answer, 
                                       value=len(self.radio_buttons), anchor="w", 
                                       font=("Helvetica", 12),
                                       bg="light blue")
            radio_btn.place(relx=0.4, rely=rely)
            radio_btn.config(font=("Arial", 12), wraplength=600)
            self.radio_buttons.append(radio_btn)
            rely += 0.05

        return self.radio_buttons
