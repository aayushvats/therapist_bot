#Therapistbot
#!/Python26/python
print('Content-type: text/html\r\n\r')

inpatient = 0
blankinput = 0
caroldead = False

#Collecting name
print('Carol: Hello. My name is Carol and I am your new therapist, what is your name?')
print()
name = input('Your name: ')
print()

#Phrases
therapistphrase = ('I see...', ('How did that make you feel, ' + str(name) + '?'), 'Do you want to have it this way?', 'What makes you feel like that?')
therapistphrasemax = len(therapistphrase) - 1

blankinputphrase = [('It will not get better if you do not talk to me, ' + str(name) + '.'), ('What is on your mind?'), 'You need to talk about this, you know.', ('I am just trying to help you, ' + str(name) + '. I cannot do that if you do not talk to me.')]
blankinputphrasemax = len(blankinputphrase) -1

#React words
suicidalsigns = list()
suicidalsigns = ['suicidal', 'die', 'death', 'suicide', 'kill']

questiontocarol = list()
qustiontocarol = ['you', '?']

killscarol = list()
killscarol = ['kills carol', 'kills Carol', 'Killsl carol', 'Kills Carol']

#Greeting
print('Carol: I see, ' + str(name) + '. Nice to meet you.')
print('       So how are you today, ' + str(name) + '?')
print()

#Major loop
while True:
    #Random phrases
    from random import randint
    randomtherapistphrase = therapistphrase[randint(0, therapistphrasemax)]
    randomblankinputphrase = blankinputphrase[randint(0, blankinputphrasemax)]

    if inpatient > 0:
        print('*You are currently locked in a psychiatric unit*')

    message = str(input('You: '))
    print()

    if message == 'no':
        print('Carol: Well will you do anything about it?')
        print()
        willu = input('You: ')
        print()

    if message == '':
            print('Carol: ' + str(randomblankinputphrase))

    for a in killscarol:
        if a in message:
            caroldead = True

    if caroldead == True:
        for i in range(100):
            print('hOw Did tHAt mAKe yOU FeEl??')
            from time import sleep
            sleep(0.01)
        break

    for a in suicidalsigns:
        if a in message:
            if inpatient == 0:
                print('Carol: You saying that really worries me, ' + str(name) + ', we will now put you inpatient')
                print()
                inpatient += 1
                break

            if inpatient > 0:
                print('Carol: We will not let you out of here if you keep saying those things, ' + str(name) + '.')
                print()
                inpatient += 1
                break

    else:
        print('Carol: ' + str(randomtherapistphrase))
        print()
