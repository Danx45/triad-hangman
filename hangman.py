import random

def choose_word():
    while True:
        difficulty = input("Select difficulty level (easy, medium, hard): ").lower()
        if difficulty not in ['easy', 'medium', 'hard']:
            print("Invalid input! Please choose 'easy', 'medium', or 'hard'.")
            continue

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
            return None
        
def hangman():
     
    word = choose_word()
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
            if guess in guessed_letters or guess in current_state:
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
