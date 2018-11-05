def open_file(file):
    """Opens text file, makes list, and removes extraneous characters in each word."""
    #  whole_file shows list with new line formatting
    whole_file = open(file, 'r')
    # readlines shows file with /n (new line) characters showing
    open_file = whole_file.readlines()
    # replace and lower: replaces \n with empty space, converts to lower case
    open_file = [word.replace('\n', '').lower() for word in open_file]
    return open_file


def filter_easy_words(open_file):
    """Pulls words of 4-6 characters out of whole list and puts in 'Easy' list."""
    easy_list = [word for word in open_file if len(
        word) >= 4 and len(word) <= 6]
    return easy_list


def filter_normal_words(open_file):
    """Pulls words of 6-8 characters out of whole list and puts in 'Normal' list."""
    normal_list = [word for word in open_file if len(
        word) >= 6 and len(word) <= 8]
    return normal_list


def filter_hard_words(open_file):
    """Pulls words of 8-10 characters out of whole list and puts in 'Hard' list."""
    hard_list = [word for word in open_file if len(word) >= 8]
    return hard_list


def choose_mode():
    """Asks user to choose Easy, Normal, or Hard mode; selects a random word from the corresponding list; counts and tells the user how many letters are in the word, and instructs the user to supply 1 letter guess per round."""
    user_choice = input(
        "Welcome to Mystery Word Game. Please choose your level of difficulty: easy, normal, or hard.")
    easy = "easy" or "Easy" or "EASY"
    normal = "normal" or "Normal" or "NORMAL"
    hard = "hard" or "Hard" or "HARD"
    import random
    if user_choice == easy:
        easy_word = random.choice(easy_list)
        print(easy_word)
        print("The word has " + str(len(easy_word)) + " letters. You may guess 1 letter per round. Good luck!")
        return easy_word
    elif user_choice == normal:
        normal_word = random.choice(normal_list)
        print(normal_word)
        print("The word has " + str(len(normal_word)) + " letters.  You may guess 1 letter per round. Good luck!")
        return normal_word
    elif user_choice == hard:
        hard_word = random.choice(hard_list)
        print(hard_word)
        print("The word has " + str(len(hard_word)) + " letters. You may guess 1 letter per round. Good luck!")
        return hard_word
    # word = easy_word or normal_word or hard_word
    # print(word)
    # return word


# word = easy_word or normal_word or hard_word


def guesses(word):
    """# accept upper or lower case letters; convert upper case letters to lower case
# tell user it's invalid if they enter more that one letter and let them try again
# tell user if their guess appears in the words."""
    guess = input("Guess a letter.")
    guess = guess.lower()
    if guess in word:
        print("You guessed the right letter!") 
    elif guess not in word:
        print("Sorry, that is incorrect. You have x guesses left.")
    # print(word)


open_file = open_file('words.txt')
easy_list = filter_easy_words(open_file)
normal_list = filter_normal_words(open_file)
hard_list = filter_hard_words(open_file)
word = choose_mode()
# word = easy_word or normal_word or hard_word
guesses(word)




# display partially guessed word as well as blanks (ie, B _ _ B A _ D)
# give user 8 guesses
# remind user how many guesses are left after each round
# take away one guess when only guess is incorrect
# don't take away guess if they repeat a letter they've already guessed;
#  print message saying they've already guessed that letter and ask them to try again
# game ends when user guesses all letters or runs out of guesses
# reveal word if user runs out of guesses
# ask user if they'd like to play again
# if y, repeat game
