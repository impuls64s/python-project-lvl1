import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('What number is missing in the progression?')
    random_len = random.choice(range(5, 11))
    shag = [2, 3, 5]
    i = 0
    while i < 3:
        rs = random.randrange(100)
        spisok = list(range(rs, rs + random_len * shag[i], shag[i]))
        random_char_i = random.randrange(len(spisok))
        answer_true = spisok[random_char_i]
        spisok[random_char_i] = '..'
        value = ''
        for n in spisok:
            value += str(n) + ' '
        print('Question: ' + value)
        answer = prompt.string('Your answer: ')
        if int(answer) == int(answer_true):
            print('Correct!')
            i += 1
        else:
            value = (f"'{answer}' is wrong answer ;(."
                     f" Correct answer was '{answer_true}'.\n"
                     f"Let's try again, {name}!")
            return print(value)
    return print(f'Congratulations, {name}!')
