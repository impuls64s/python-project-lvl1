import prompt
import random


value = []


def prime():
    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            value.append(i)


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    prime()
    i = 0
    while i < 3:
        rn = random.randrange(2, 100)
        print('Question: ' + str(rn))
        answer_true = ''
        for n in value:
            if n == rn:
                answer_true = 'yes'
                break
            else:
                answer_true = 'no'
        answer = prompt.string('Your answer: ')
        if answer == answer_true:
            print('Correct!')
            i += 1
        else:
            val = (f"'{answer}' is wrong answer ;(."
                   f" Correct answer was '{answer_true}'.\n"
                   f"Let's try again, {name}!")
            return print(val)
    return print(f'Congratulations, {name}!')
