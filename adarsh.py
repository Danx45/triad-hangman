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
