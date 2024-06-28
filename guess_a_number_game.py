from random import randint
# from art import logo
# 1 function = difficulty level
# difficulty level()    easy/hard
#check answer(answer turn , difficulty)
# game()
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess,answer,turns):
    if guess> answer:
        print("Too high.")
        return turns -1
    elif guess < answer:
        print("Too Low.")
        return turns-1
    else:
        print(f"You got it! The answer is{answer}.")

    # Make function to set differently
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #choosing a random number between 1 and 100
    print("Welcome to the number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    # print(f"Psst, the correct answer is {answer}.")

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number
        guess = int(input("Make a guess:  "))

        # Track the number of turns and reduce by 1 if they get wrong
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("""You have run out of guesses, you lose.""")
            return
        elif guess != answer:
            print("Guess again.")

game()



