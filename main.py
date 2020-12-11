import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing M.A.Y.A..")

MASTER= "sooraj"
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def command():
    hr=int(datetime.datetime.now().hour)
    if(hr>=0 and hr<=12):
        speak("Good Morning "+MASTER)
    elif(hr>=12 and hr<18):
        speak("Good Afternoon "+MASTER)
    else:
        speak("Good Evening "+MASTER)

    speak("I am MAYAA... How may i help you")
    #speak("Kya haal hai suraj....hukum karein")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk to M.A.Y.A: ")
        audio = r.listen(source)
    try:
        print (r.recognize_google(audio))
        return r.recognize_google(audio).lower()
    except sr.UnknownValueError:
        speak(
            "I couldn't understand what you said! Would you like to repeat?")
        return(listen())
    except sr.RequestError as e:
        print("Could not request results from " +
              "Google Speech Recognition service; {0}".format(e))



#Execution starts from here
speak("Initializing MAYAA...")
command()
order=listen()

if 'wikipedia' in order:
    speak('Searching Wikipedia...')
    order=order.replace("wikipedia","")
    result=wikipedia.summary(order,sentences=2)
    print(result)
    speak(result)

elif 'open google' in order:
    webbrowser.open("google.com")

elif 'open youtube' in order:
    webbrowser.open("youtube.com")

elif 'open facebook' in order:
    webbrowser.open("facebook.com")

elif 'the time' in order:
    t=datetime.datetime.now().strftime("%H:%M:%S")
    print("Time : "+t)
    speak(f"The time is {t}")

elif 'open wordpad' in order:
    path="C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe"
    os.startfile(path)