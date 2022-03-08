"""Rock paper scissors game with voice command of player"""
import speech_recognition as sr
from random import choice


voice = ""
elements = ['rock', 'paper', 'scissors']
while True:
    r = sr.Recognizer()
    machine = choice(elements)
    with sr.Microphone() as source:
        try:  # If it doesn't work, install flac converter
            print("Say 'rock', 'paper' or 'scissors'.")
            audio = r.listen(source)
            text_raw = r.recognize_google(audio)
            text = text_raw.lower()
            print(text)
            if text == 'stop':
                break
            elif text not in elements:  # If the word is not recognized correctly, ask to say it again
                print(f"I couldn't recognize properly your voice. Try to say again 'rock', 'paper' or 'scissors'.")
            elif text == machine:
                print(f'Draw. Computer has chosen {machine}.')
            elif (machine == 'rock' and text == 'paper') or (machine == 'paper' and text == 'scissors') or \
                    (machine == 'scissors' and text == 'rock'):
                print(f'You win. Computer has chosen {machine}.')
            else:
                print(f'You lose. Computer has chosen {machine}.')
        except:
            print("I can't hear you. Try to say something again....")
    print('Do you wish to play again?')
    continue
