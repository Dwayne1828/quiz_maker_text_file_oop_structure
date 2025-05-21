import tkinter as tk

class ChoicesRadioBtn:
    def choices_radio_btn(self):
            radio_buttons = []
            rely = 0.4

            while len(radio_buttons) < 4: 
                radio_btn = tk.Radiobutton(self.root, text="", 
                                        variable=self.choosed_answer, 
                                        value=len(radio_buttons), anchor="w", 
                                        font=("Helvetica", 12),
                                            bg="light blue")
                radio_btn.place(relx=0.4, rely=rely)
                radio_btn.config(font=("Arial", 12), wraplength=600)
                radio_buttons.append(radio_btn)
                rely += 0.05
                
            return radio_buttons

