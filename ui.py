from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Quizinterface():
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain

        # creating window
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # creating canvas, labels, buttons etc.
        self.score_label = Label(text="Score: ", fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     font=("Arial", 20, "italic"),
                                                     text="Some question text",
                                                     fill=THEME_COLOR,
                                                     width=280)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)


        t_image = PhotoImage(file="images/true.png")
        self.t_button = Button(image=t_image, highlightthickness=0,command=self.true_pressed)
        self.t_button.grid(row=2, column=0)

        f_image = PhotoImage(file="images/false.png")
        self.f_button = Button(image=f_image, highlightthickness=0,command=self.false_pressed)
        self.f_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="END of Quiz")
            self.t_button.config(state="disabled")
            self.f_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

