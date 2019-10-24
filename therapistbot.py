#Therapistbot
#Therapistbot

#Default data
inpatient = 0

suicidalsigns = list()
suicidalsigns = ['suicidal', 'die', 'death', 'suicide']

#Greeting
print('Hello. My name is Carol and I am your new therapist, what is your name?')
print()
name = input('You: ')
print()

#Therapistphrases
therapistphrase = ('I see...', ('How did that make you feel, ' + str(name) + '?'), 'Do you want to have it this way?', 'What makes you feel like that?')
maxval = len(therapistphrase) - 1

print('Carol: I see, ' + str(name) + ', nice to meet you.')
print('       So how are you today, ' + str(name) + '?')
print()

#Major loop
while True:

    from random import randint
    randomtherapistphrase = therapistphrase[randint(0, maxval)]
    if inpatient > 0:
        print('*You are currently locked in a psychiatric unit*')

    message = str(input('You: '))
    print()

    if message == 'no':
        print('Carol: Well will you do anything about it?')
        print()
        willu = input('You: ')
        print()
        if willu == 'no':
            print('Carol: ' + str(randomtherapistphrase))
            print()
            continue

    for a in suicidalsigns:
        if a in message:
            print('That really worries me, ' + str(name) + ', we will now put you inpatient')
            inpatient += 1
            print()

    else:
        print('Carol: ' + str(randomtherapistphrase))
        print()
