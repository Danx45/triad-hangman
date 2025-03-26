import random

with open("easy.txt", 'r') as file:
    words = file.read().splitlines() 
    word = random.choice(words)
        
def hangman():
     
    attempts_left = 6
    current_state = ['_'] * len(word)
    guessed_letters = []

    while '_' in current_state and attempts_left > 0:
        print(f"\nCurrent word: {' '.join(current_state)}")
        print(f"Incorrect guessed letters: {guessed_letters}")
        print(f"Lives left: {attempts_left}")

        try:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                raise ValueError("\nPlease enter only one character.")
            if not guess.isalpha():
                raise ValueError("\nPlease enter a letter from A-Z.")
            if guess in guessed_letters:
                raise ValueError("\nYou've already guessed that letter.")
        except ValueError as e:
            print(f"\nInvalid input: {e}")
            continue

        if guess not in word:
            guessed_letters.append(guess)
            attempts_left -= 1
        else:
            for index, letter in enumerate(list(word)):
                if letter == guess:
                    current_state[index] = guess

        if attempts_left == 0:
            print(f"\nYou've lost! Correct word was '{word}'.")
        
        if '_' not in current_state:
            print(f'\nGood job! The word was "{word}"!')

        



if __name__ == '__main__':
    hangman()
