while True:
    if guess not in player.word:
        player.guessed_letters.add(guess)
        player.attempts_left -= 1
        print(f"Lives left: {player.attempts_left}")
        print(f"Incorrect guessed letters: {player.guessed_letters}")
        if player.attempts_left == 0:
            print(f"You've lost! Correct word was '{player.word}'.")
            break
    guess = input("Guess another letter: ")
