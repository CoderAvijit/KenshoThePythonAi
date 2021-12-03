import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Kensho Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('avijitrana121299@gmail.com', 'Kensho@1999')
    server.sendmail('avijitrana121299@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("sure sir!")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("sure sir!")
            webbrowser.open("https://www.google.com/")

        elif 'open stackoverflow' in query:
            speak("sure sir!")
            webbrowser.open("https://stackoverflow.com/")   


        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'quit' in query:
            speak("sure sir.")
            speak("have a great day sir!. i'm quiting")
            exit()  

        elif 'help' in query:
            speak("I am learning, I can assit you on anything")
            speak("tell me on what you need my help") 

        elif 'whatsapp' in query:
            speak("I am good , Whats about you, Avijit")
            speak("tell me how can I help you")  
    
        elif 'my name' in query:
            speak("you're my boss.my dear Avijit sir.")
            speak("tell me how can I help you, Avijit sir")  

        elif 'open code' in query:
            codePath = r"C:\Users\aviji\AppData\Local\Programs\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'mail'  in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mandalkeshab2018@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")  
        
    

