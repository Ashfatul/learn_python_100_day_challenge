from tkinter import *
from tkinter import messagebox
import quizBackend, time

class QuizInterface:
    def __init__(self, quizBrain) -> None:
        self.window = Tk()
        self.window.title("True False Quiz")
        self.window.config(padx=20, pady=20, bg="black")

        helpBtn = Button(text="Help?", bg="white", fg="black", highlightthickness=0,bd=0, command=self.showHelp)
        helpBtn.grid(column=1, row=0)
        
        self.score = Label(text="Score: 0", fg="white", bg="black", justify="right")
        self.score.grid(column=2, row=0)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=1, row=1, columnspan=2, pady=20)

        self.quiz_text = self.canvas.create_text(150, 125, text="This is where quiz question will show up", font=("Arial", 16), fill="black", width=280)

        self.trueBtn = Button(text="Correct", bg="#50BC8E", fg="white", highlightthickness=0,bd=0, command=lambda: self.checkAns("True"))
        self.trueBtn.grid(column=1, row=2, padx=0, pady=20)
        self.falseBtn = Button(text="Wrong", bg="#F56761", fg="white", highlightthickness=0,bd=0, command=lambda: self.checkAns("False"))
        self.falseBtn.grid(column=2, row=2, padx=0, pady=20)

        self.quizBox = quizBrain()
        self.quizBox.getQuestions()

        self.canvas.itemconfig(self.quiz_text, text=f"Q{self.quizBox.question_number}." + self.quizBox.firstQuestion()["question"])
        
        self.status = Label(text="", fg="white", bg="black", font=("Arial", 20, "italic"), justify="center")
        self.status.grid(column=1, row=3, columnspan=2)


        self.window.mainloop()

    def checkAns(self, userAns):

        if self.quizBox.questionLeft >= 1:
            if userAns == self.quizBox.answerOfQuiz():
                self.score.config(text=f"Score: {self.quizBox.updateScore()}")
            self.canvas.itemconfig(self.quiz_text, text=f"Q{self.quizBox.question_number + 1}." + self.quizBox.nextQuestion()["question"])
        else:
            self.canvas.itemconfig(self.quiz_text, text=f"Quiz End\n\n Your Final Score is \n\n {self.quizBox.score}/10", justify="center")

            self.trueBtn.config(text="Restart", command=self.restart)
            self.falseBtn.config(text="Exit", command=self.window.destroy)

    def showHelp(self):
        messagebox.showinfo("How to Play", "This is a random quiz game where you will be asked 10 correct or wrong questions.\n\nAnswer by clicking on the respective button and move to next question.\n\nFinally you will be shown your final score and you have the option to restart and exit the application. We will be implementing a 60s timing function soon.\n\n Enjoy :)")

    def restart(self):
        self.window.title("Restarting...")
        self.quizBox = quizBackend.QuizBackend()
        self.quizBox.getQuestions()
        self.canvas.itemconfig(self.quiz_text, text=f"Q{self.quizBox.question_number}." + self.quizBox.firstQuestion()["question"])
        self.score.config(text="Score: 0")
        self.trueBtn.config(text="Correct", command=lambda: self.checkAns("True"))
        self.falseBtn.config(text="Wrong", command=lambda: self.checkAns("False"))
        self.window.title("True False Quiz")
        

quiz_interface = QuizInterface(quizBackend.QuizBackend)
