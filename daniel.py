while '_' in current_state:
    for index, letter in enumerate(list(word)):
        if letter == input_letter:
            current_state[index] = input_letter
    print(current_state)
    if '_' in current_state: 
        input_letter = input("idk: ")
    else:
        print(f'Good job! The word was "{word}"!')
