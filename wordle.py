def choose_length(length):
    if length == "4":
        with open("4.txt") as file:
            return file
    elif length == "5":
        with open("5.txt") as file:
            return file
    elif length == "6":
        with open("6.txt") as file:
            return file
    elif length == "7":
        with open("7.txt") as file:
            return file
    elif length == "8":
        with open("8.txt") as file:
            return file
    else:
        print("Not a valid length. Choose a length 4-8.")

def choose_word(file,length):
    num_of_words = readlines()

def main():
    length = input("Choose a length for wordle (4-8): ")
    choose_length(length)

if __name__ == "__main__":
    main()
    
    
    
            
