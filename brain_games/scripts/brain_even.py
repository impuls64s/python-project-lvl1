import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question = ['Question: 15', 'Question: 6', 'Question: 7']
    answer = ['no', 'yes', 'no']

    ii = 0
    for i in question:
        print(i)
        ans = prompt.string('Your answer: ')
        if ans == answer[ii]:
            print('Correct!')
            ii += 1
        else:
            value = (f"'{ans}' is wrong answer ;(."
                     f" Correct answer was '{answer[ii]}'.\n"
                     f"Let's try again, {name}!")
            return print(value)
    return print(f'Congratulations, {name}!')
