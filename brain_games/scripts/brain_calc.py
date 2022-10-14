import prompt
import random
from operator import add, sub, mul


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('What is the result of the expression?')
    i = 0
    while i < 3:

        random1 = random.randrange(30)
        random2 = random.randrange(30)

        op_str = ['+', '-', '*']
        op_int = [add, sub, mul]
        random_char = random.randrange(0, 3)

        print(f"Question: {random1} {op_str[random_char]} {random2}")
        answer_true = op_int[random_char](random1, random2)
        answer = prompt.string('Your answer: ')
        if answer_true == int(answer):
            print('Correct!')
            i += 1
        else:
            value = (f"'{answer}' is wrong answer ;(."
                     f" Correct answer was '{answer_true}'.\n"
                     f"Let's try again, {name}!")
            return print(value)
    return print(f'Congratulations, {name}!')
