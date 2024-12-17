class QuizBrain:

    def __init__(self,questions):
        self.questions = questions
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def check_answer(self,answer_user, correct_answer):
        if answer_user == correct_answer:
            self.score +=1
            print("Correct!")
        else: print("Incorrect :( ")
        print(f"Score: {self.score}/{self.question_number}\n")

    def next_question(self):
        question = self.questions[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text}(True/False): ").capitalize()
        self.check_answer(answer,question.answer)


