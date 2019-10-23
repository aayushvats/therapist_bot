#Therapistbot
suicidal = 'i wanna die'

inpatient = 0

print('Hello. My name is Carol and I am your new therapist, what is your name?')
print('Type your reply below:')
name = input()

therapistphrase = ('I see...', ('How did that make you feel, ' + str(name) + '?'), 'Do you want to have it this way?', 'What makes you feel like that?')
maxval = len(therapistphrase) - 1
print(maxval)

print('I see, ' + str(name) + ', nice to meet you.')
print('So how are you today, ' + str(name) + '?')

while True:
    if inpatient > 0: 
        print('*You are currently locked in a psychiatric unit*')
    print('Type your reply below:')
    message = input()

    if message == 'no':
        print('Well will you do anything about it?')
        willu = input()
        if willu == 'no':
            continue

    if message == suicidal:
        print('That really worries me, ' + str(name) + ', we will now put you inpatient')
        inpatient += 1
        
    
    else:
        from random import randint
        print(therapistphrase[randint(0, maxval)])

    
    

