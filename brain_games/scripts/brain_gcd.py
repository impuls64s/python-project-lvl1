import prompt
import random
import math


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        random1 = random.randrange(100)
        random2 = random.randrange(100)
        print(f"Question: {random1} {random2}")
        answer = prompt.string('Your answer: ')
        answer_true = math.gcd(random1, random2)
        if answer_true == int(answer):
            print('Correct!')
            i += 1
        else:
            value = (f"'{answer}' is wrong answer ;(."
                     f" Correct answer was '{answer_true}'.\n"
                     f"Let's try again, {name}!")
            return print(value)
    return print(f'Congratulations, {name}!')
