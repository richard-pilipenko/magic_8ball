import random
import time
import sys

eight_ball_answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", 
                      "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", 
                      "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", 
                      "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", 
                      "Outlook not so good.", "Very doubtful."]

play = True

def magic_eight_ball():
    response_question = input("You can ask me any yes or no question:\n>>>")
    print('Thinking...')
    time.sleep(random.randint(0, 4))
    print(random.choice(eight_ball_answers))

while play:
    response_name = input("Hello! I am Magic 8 Ball. What is your name?\n>>>")
    time.sleep(random.randint(1, 2))
    print(f"Nice to meet you {response_name}!")
    time.sleep(random.randint(1, 2))
    magic_eight_ball()
    ask_again = input("Would you like to ask again?[Y/N]")
    if not ask_again.lower() == 'y':
        play = 'n'
        sys.exit()

dsada
