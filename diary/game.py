from Speach import *
from random import choice
import time
a = int(input("Сколько вы хотите раундов?"))
levels = {
    "easy": ["diary", "mouse", "computer"],
    "medium": ["programming", "algorithm", "developer"],
    "hard": ["neural network", "machine learning", "artificial intelligence"]
}
def play_game(level):
    score = 0
    word_score = 0
    words_score = 2
    words = levels.get(level, [])
    for i in range(a):
        random_word = choice(words).capitalize()
        old_word = random_word
        print(f"Произнесите слово {random_word}")
        recog_word = speach().capitalize()
        print(recog_word)
        if random_word == recog_word:
            print("Вы выиграли!")
            score += 1
        else:
            print(f"Ты проиграл! Правильный ответ: {random_word}")
        if random_word != recog_word and random_word == old_word:
            word_score += 1
        if word_score == words_score:
            print("Попытки на это слово окончены!")
            break
        time.sleep(2)
    print(f"Ваш счёт: {score}/{a}")
selected_level = input("Выберите левел {easy/medium/hard}: ").lower()
play_game(selected_level)