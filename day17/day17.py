class Question:
    """Creates the question for our game"""
    def __init__(self, text, answer = None):
        self.text = text
        self.answer = answer





quest1 = Question("Nombre: ", False)
quest2 = Question("jola")
quest1.follow(quest2)
print(quest2.followers, quest1.following)