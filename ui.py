from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=40, pady=30, bg=THEME_COLOR)

        self.label=Label(text="Score:0" ,fg="white", bg=THEME_COLOR, font=("Arial", 15, "bold"))
        self.label.grid(column=1, row=0)
        
        
        self.canvas=Canvas(width=300, height=250, bg="white")
        self.question_text=self.canvas.create_text( 
            150,
            125,
            width=280,
            text="Text",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
            )
        self.canvas.grid(row=1, column=0,columnspan=2, pady=50)


       
    
        my_image1 = PhotoImage(file="images/true.png")
        self.button1 = Button(image=my_image1, highlightthickness=0, command=self.true_pressed)
        self.button1.grid(row=2,column=0)

        my_image2 = PhotoImage(file="images/false.png")
        self.button2 = Button(image=my_image2, highlightthickness=0, command=self.false_pressed)
        self.button2.grid(row=2,column=1)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Final Score:{self.quiz.score}. \n\nYou have reached the end of the quiz.")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")


        self.window.after(1000, self.get_next_question)
        
        


