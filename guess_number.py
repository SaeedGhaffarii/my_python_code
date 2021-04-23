# from random import randint
#
# EASY_LEVEL = 10
# HARD_LEVEL = 5
#
#
# def check_answer(guess, answer, turns):
#     if guess > answer:
#         print("Too high")
#         return turns - 1
#     elif guess < answer:
#         print("Too low")
#         return turns - 1
#     else:
#         print(f"You got it.the answer is {answer}")
#
#
# def set_difficulty():
#     level = input("Choose difficulty , 'hard' or 'easy'.")
#     if level == 'hard':
#         return HARD_LEVEL
#     else:
#         return EASY_LEVEL
#
#
# def game():
#     print("Welcome to the Number guessing.")
#     print("I'm thinking of number between 1 and 100.")
#     answer = randint(1, 100)
#     print(f"psst,the correct answer is {answer}")
#     turns = set_difficulty()
#     guess = 0
#     while guess != answer:
#         print(f"You have {turns} attempt remaining to guess the number.")
#         guess = int(input("Make a guess :"))
#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print("You've run out of guesses.You lose")
#             return
#         elif guess != answer:
#             print("Guess again.")
#
#
# game()
