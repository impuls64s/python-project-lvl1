#!/usr/bin/env python3

from ..cli import welcome_user


def brain_games():
    print("Welcome to the Brain Games!")
    welcome_user()


def main():
    brain_games()


if __name__ == '__main__':
    main()
