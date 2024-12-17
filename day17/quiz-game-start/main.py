from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = []
for obj in question_data:
    questions.append(Question(obj['text'],obj['answer']))

quizz_brain = QuizBrain(questions)

while quizz_brain.still_has_questions():
    answer = quizz_brain.next_question()
print(f"You have completed the quiz!\nYour score was: {quizz_brain.score}/{quizz_brain.question_number}")
