while '_' in current_state:
    for index, letter in enumerate(list(word)):
        if letter == input_letter:
            current_state[index] = input_letter
    print(current_state)
    if '_' in current_state: 
        input_letter = input("idk: ")
    else:
        print(f'Good job! The word was "{word}"!')


import random


def choose_word(difficulty='easy'):

    try:
        if difficulty == 'easy':
            filename = "easy.txt"

        elif difficulty == 'medium':
            filename = "medium.txt"

        elif difficulty == 'hard':
            filename = "hard.txt"

        with open(filename, 'r') as file:
            words = file.read().splitlines() 
            return random.choice(words)
        
    except FileNotFoundError:
        print(f"Error! {filename} not found. Please make sure the file exists.")
    
def hangman():

    difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()
    
    if difficulty == 'easy':
        attempts = 6

    elif difficulty == 'medium':
        attempts = 8
        
    elif difficulty == 'hard':
        attempts = 10
    
    word = choose_word(difficulty)

    word_list = list(word)
    guessed_word = ['_'] * len(word_list)
    wrong_letters = []

    while attempts > 0 and '_' in guessed_word:
        print(f"\nCurrent word: {' '.join(guessed_word)}")
        print(f"Wrong letters: {' '.join(wrong_letters)}")
        
        guessed_letter = input("Guess a letter: ").lower()

        if guessed_letter in word_list:
            for index, char in enumerate(word_list):
                    if char == guessed_letter:
                        guessed_word[index] = guessed_letter
        
        else:
                attempts -= 1
                print(f"\nWrong guess! You have {attempts} attempts left.")

                if guessed_letter not in wrong_letters:
                     wrong_letters.append(guessed_letter)


    if '_' not in guessed_word:
            print(f"\nCongratulations! You guessed the word: '{word}'. ")
    else:
            print("\nGame over! You ran out of attempts.")
            print(f"The word was: '{word}'")

if __name__ == '__main__':
    hangman()
