import random
import time

attempts = 6

def pick_word(file):
    try:
        with open(file) as words:
            lines = words.readlines()
            if lines:
                random_line = random.choice(lines)
                word = random_line.strip().lower()
                return word
            else:
                return "File is empty."
            
    except FileNotFoundError:
        print("ERROR: FILE NOT FOUND")
        return None

def word_to_blank(word, current_state):
    for char in current_state:
        print(char,end=" ")
    print()

def search_letter(word, current_state, guessed_letters):
    global attempts

    print("Guessed letters-", " ".join(guessed_letters))
    letter = input("Enter a letter: ").lower()
    
    if letter in guessed_letters:
        print()
        print("You've already guessed that letter. Try again.")
        return False
    
    guessed_letters.append(letter)
    " ".join(guessed_letters)
    print()

    print()
    if letter in word:
        print("Letter Found!")
        time.sleep(.1)

        for i,char in enumerate(word):
            if char == letter:
                current_state[i] = letter
                
    else:
        attempts -= 1
        print("Letter not found. Attempts remaining:",attempts)

    if "_" not in current_state:
        print("Congratulations, You've guessed the word:", word)
        return True
    
    elif attempts <= 0:
        print("Sorry, you've run out of attempts. The word was:", word)
        return True
    
    return False

def main():
    word = pick_word("data/words.txt")
    if not word:
        return
    
    current_state = ["_"] * len(word)
    guessed_letters = []
    while True:
        word_to_blank(word, current_state)
        if search_letter(word, current_state, guessed_letters):
            break

if __name__ == "__main__":
    main()
