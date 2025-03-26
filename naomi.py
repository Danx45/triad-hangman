while True:
    if guess not in player.word:
        player.guesses_letters.add(guess)
        player.attemps_left -= 1
        print("Lives left: {player.atemps_left}")
        print("Incorrect guessed letters: {player.guessed_letters}")
    if player.attemps_left == 0:
        print(f"You've lost! Correct word was '{player.word}'.")
    break
    guess = input("Guess another letter: ")
