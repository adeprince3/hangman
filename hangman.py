import random

def hangman():
    words = ['dog', 'girl', 'contemplation', 'extravegence', 'enamored']
    word = words[random.randint(0, 4)]
    wrong = 0
    stages = ['',
             '__________           ',
             '|          |         ',
             '|          0         ',
             '|         /|\        ',
             '|         / \        ',
             '|                    '
             ]
    remaining_letters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Welcome to Hangman')
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Guess a letter: '
        char = input(msg)
        if char in remaining_letters:
            char_index = remaining_letters.index(char)
            board[char_index] = char
            remaining_letters[char_index] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        stage = wrong + 1
        print('\n'.join(stages[0: stage]))
        if '_' not in board:
            print('You win!')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You lose! It was {}.'.format(word))