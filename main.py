words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

answers = {}
correct_answers = 0


hards = {"Легкий": words_easy, "Средний": words_medium, "Сложный": words_hard}


user_input = input("Выберите уровень сложности: Легкий, Средний, Сложный: ")


work_dict = hards[user_input.lower().title().strip()]


for key, item in work_dict.items():
    print(f"{key}, {len(item)} букв, начинается на {item[0]}")
    answer_input = input().strip().lower()
    if answer_input == item:
        answers[key] = True
        correct_answers += 1
        print(f"Верно. {key} - это {item}")
    else:
        answers[key] = False
        print(f"Неверно. {key} - это {item}")

print("Правильно отвечены слова:")
for k, v in answers.items():
    if v == True:
       print(k)
    continue
print("Неправильные отвечены слова:")
for k, v in answers.items():
    if v == False:
        print(k)



correct_answers = levels[correct_answers]
print(f"Ваш ранг:\n{correct_answers}")
