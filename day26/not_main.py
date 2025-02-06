#LISTAS Y DICCIONARIOS POR COMPRENSION
import random

mult = [num*2 for num in [1,2,3,4] if num%2 == 0]
print(mult)

names = ["Igna", "manu", "Fer"]
scores = {student:random.randint(1,100) for student in names}
print(scores)

passed = {student:mark for (student,mark) in scores.items() if mark >= 60}
print(passed)