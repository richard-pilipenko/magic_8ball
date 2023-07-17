import random

eight_ball_answers = {'Affirmative': ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'You may rely on it.', 
                      'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.'], 
                      'Non-commital': ['Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 
                      'Concentrate and ask again.'], 'Negative': ['Don\'t count on it.', 'My reply is no.', 'My sources say no.', 
                      'Outlook not so good.', 'Very doubtful.']}

answer_key = ['Affirmative', 'Non-commital', 'Negative']

def get_eightball_answer(key):
    answer = get_random_choice(key)
    reply_choice = get_reply(eight_ball_answers[answer])
    print(answer)
    print(eight_ball_answers[answer][reply_choice])
    
    


def get_random_choice(key):
    return random.choice(key)

def get_reply(list):
    return random.randrange(0, len(list))

print('Ask')
usr_input = input('')
get_eightball_answer(answer_key)