
# friendshipquiz

firstname = "John"
middlename = "Mark"
lastname = "Smith"
age = "16"
favorite_color = "Blue"
favorite_food = "Pizza"

questions = [
    ("What is birthdayboy's first name? ", firstname),
    ("What is birthdayboy's middle name? ", middlename),
    ("What is birthdayboy's last name? ", lastname),
    ("What is birthdayboy's age? ", age),
    ("What is birthdayboy's favorite color? ", favorite_color),
    ("What is birthdayboy's favorite food? ", favorite_food),
]

score = 0

for question, answer in questions:
    if input(question).strip().lower() == answer.lower():
        score += 1

if score == 0:
    print("You got all the answers wrong! Are you sure you guys are friends?")
elif score == len(questions):
    print("You got all the answers right! You guys are totally best friends!")
else:
    print("You got half of the answers right! You guys are....friends i think.")