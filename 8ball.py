import random
import time
import sys

eight_ball_answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", 
                      "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", 
                      "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", 
                      "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", 
                      "Outlook not so good.", "Very doubtful."]

user_name = ""
first_question = True

print("THE MAGIC 8 BALL")

def magic_eight_ball():
    global first_question
    global user_name
    if first_question == True: 
        response_question = input("Ask me any yes or no question.\n>>> ")
        first_question = False
    else:
        response_question = input("Fire away.\n>>> ")
    print(f"{user_name} asks: {response_question}")
    print("Fortune telling in progress...")
    time.sleep(random.randint(1, 4))
    print(random.choice(eight_ball_answers))

     
while True:
    if len(user_name) == 0: user_name = input("Welcome! I am Magic 8 Ball. Please enter your name.\n>>> ")
    magic_eight_ball()
    ask_again = input("Do you have another question?[Y/N]\n>>> ")
    if not ask_again.lower() == "y": time.sleep(1), print("Bye!"), sys.exit()
