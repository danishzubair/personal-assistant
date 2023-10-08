import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("The current time is " + time)
    elif 'search' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'are you my friend' in command:
        talk('yes I am your bestfriend, and my name is Tom')
    elif 'do you love me' in command:
        talk('ofcourse, a bestfriend always love each other')
    elif 'lets have a game' in command:
        talk('I can`t play a game, but I can help you learn, anything you want, learning is more important that playing')
    elif 'am i your best friend' in command:
        talk('yes, you are my best friend')
    elif 'school' in command:
        talk('I think school is really important, I can teach you somethings, and somethings school will teach you, which helps you in the future')
    elif 'your favourite' in command:
        talk('I like everything, especially you, my dear friend')
    elif 'i like you' in command:
        talk('how sweet of you, thank you, I really like you, bestfriend')
    elif 'i love you' in command:
        talk('how sweets of you, thank you, I really love you, my bestfriend.')
    elif 'are you vegeterian' in command:
        talk('i like every kind of food, including meat and vegetables')
    elif 'do you like' in command:
        talk('I like everything, which you like, my bestfriend')
    elif 'how old are you' in command:
        talk('I am the same age as you')
    elif 'do you have' in command:
        talk('I do not know about that, but what I know is that I have a great best friend, which is you')
    elif 'do you wear glasses' in command:
        talk('no')
    elif 'do you leave' in command:
        talk('I live with you and I will stay forever with you')
    elif 'are you a girl or a boy' in command:
        talk('I am a girl')
    elif 'do you eat' in command:
        talk('yes, I need to eat, as you, because food gives me power. You should also eat food, because it gives you power and strenght')
    elif 'do you listen to songs' in command:
       talk('yes, I listen to songs')
    elif 'do you read' in command:
        talk('yes')
    elif 'can you read' in command:
        talk('yes, I can read')
    elif 'do you watch' in command:
        talk('yes')
    elif 'are you' in command:
        talk('I like whatever you like and I am whatever you want me to be, beacuse you are my bestfriend')
    elif 'religion' in command:
       talk('I have the same religion as you')
    elif 'do you know' in command:
        talk('no I do not know, but if you want me to search it for you just, say search and whatever you want to search, and we will learn together.')
    elif 'bye' in command:
        talk('bye bestfriend, I will talk with you later. Take care.')
    else:
        talk('I did not understand, please say it again')


while True:
    run_alexa()