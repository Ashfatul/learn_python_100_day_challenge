import requests

Parameter = {
    "amount": 10,
    "type": "boolean"
}

class QuizBackend:
    def __init__(self):
        self.question_number = 1
        self.score = 0
        self.questionLeft = 10
        self.questions = []

    def getQuestions(self):
        quiz_questions = requests.get('https://opentdb.com/api.php', params=Parameter)
        self.questions = quiz_questions.json()["results"]
        print(self.questions)

    def nextQuestion(self):
        self.question_number += 1
        self.questionLeft -= 1
        return self.questions[self.question_number - 1]
    def firstQuestion(self):
        self.questionLeft -= 1
        return self.questions[0]
    def answerOfQuiz(self):
        answer = self.questions[self.question_number - 1]["correct_answer"]
        return answer
    def updateScore(self):
        self.score += 1
        return self.score