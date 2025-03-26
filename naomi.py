        while '_' in player.current_state:
            for index, letter in enumerate(list(player.word)):
                if letter == guess:
                    player.current_state[index] = guess
            print(player.current_state)
            if '_' in player.current_state:
                if guess not in player.word:
                    player.guessed_letters.add(guess)
                    player.attempts_left -= 1
                    print(f"Lives left: {player.attempts_left}")
                    print(f"Incorrect guessed letters: {player.guessed_letters}")
                    if player.attempts_left == 0:
                        print(f"You've lost! Correct word was '{player.word}'.")
                        return
                guess = input("Guess another letter: ")
            else:
                print(f'Good job! The word was "{player.word}"!')
