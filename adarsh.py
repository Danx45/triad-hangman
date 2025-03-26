import random

# Function to choose a word based on difficulty
def choose_word(difficulty='easy'):
    try:
        # File selection based on difficulty
        if difficulty == 'easy':
            filename = "easy.txt"
        elif difficulty == 'medium':
            filename = "medium.txt"
        elif difficulty == 'hard':
            filename = "hard.txt"
        
        # Reading the word file
        with open(filename, 'r') as file:
            words = file.read().splitlines()
            return random.choice(words)
    except FileNotFoundError:
        print(f"Error! {filename} not found. Please make sure the file exists.")
        return None

# Hangman game function
def hangman():
    # Get difficulty level
    difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()
    
    # Set the number of attempts based on difficulty
    if difficulty == 'easy':
        attempts = 6
    elif difficulty == 'medium':
        attempts = 8
    elif difficulty == 'hard':
        attempts = 10
    else:
        print("Invalid difficulty. Defaulting to 'easy'.")
        attempts = 6

    # Choose the word
    word = choose_word(difficulty)
    if word is None:
        return
    
    word_list = list(word)
    guessed_word = ['_'] * len(word_list)
    wrong_letters = set()
    guessed_letters = set()

    while attempts > 0 and '_' in guessed_word:
        print(f"\nCurrent word: {' '.join(guessed_word)}")
        print(f"Wrong letters: {' '.join(sorted(wrong_letters))}")
        print(f"Lives left: {attempts}")

        # Get user input
        try:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                raise ValueError("Please enter only one character.")
            if not guess.isalpha():
                raise ValueError("Please enter a letter from A-Z.")
            if guess in guessed_letters:
                raise ValueError("You've already guessed that letter.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue

        guessed_letters.add(guess)

        # Check if guess is in the word
        if guess in word_list:
            for index, char in enumerate(word_list):
                if char == guess:
                    guessed_word[index] = guess
        else:
            if guess not in wrong_letters:
                wrong_letters.add(guess)
                attempts -= 1
                print(f"\nWrong guess! You have {attempts} attempts left.")

    # Game outcome
    if '_' not in guessed_word:
        print(f"\nCongratulations! You guessed the word: '{word}'.")
    else:
        print("\nGame over! You ran out of attempts.")
        print(f"The word was: '{word}'")

# Run the game
if __name__ == '__main__':
    hangman()
