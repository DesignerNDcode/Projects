import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
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

hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
        speak("Good Morning! Sir Or Mam, I am C C E S Assistant")
        speak("enter 1 for voice command and 2 for typed command")

elif hour>=12 and hour<18:
        speak("Good Afternoon! Sir Or Mam, I am C C E S Assistant")
        speak("enter 1 for voice command and 2 for typed command")

else:
        speak("Good Evening! Sir Or Mam, I am C C E S Assistant")
        speak("enter 1 for voice command and 2 for typed command")
    
order = int(input(">>"))


def wishMe():
        speak("Please tell me how may i help you")
0
r = sr.Recognizer()
if order == 1:
    def takeCommand():
    #It takes microphone input from the user and returns string output

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
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
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
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")


                elif 'play music' in query:
                    music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif 'tell me time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif 'what is your name' in query:
                    speak("i am  C C E S Assistant")

                elif 'open code' in query:
                    codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                elif 'email to harry' in query:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = "harryyourEmail@gmail.com"
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry my friend harry bhai. I am not able to send this email")
            

elif order == 2:
    while True:
            input("Want to give command")
            speak("Please write command for me")

            command = input(">>")
            if 'wikipedia' in command:
                            speak('Searching Wikipedia...')
                            command = command.replace("wikipedia", "")
                            results = wikipedia.summary(command, sentences=2)
                            speak("According to Wikipedia")
                            print(results)
                            speak(results)

            elif 'open youtube' in command:
                            webbrowser.open("youtube.com")

            elif 'open google' in command:
                            webbrowser.open("google.com")

            elif 'open stackoverflow' in command:
                            webbrowser.open("stackoverflow.com")


            elif 'play music' in command:
                            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                            songs = os.listdir(music_dir)
                            print(songs)
                            os.startfile(os.path.join(music_dir, songs[0]))

            elif 'tell me time' in command:
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            speak(f"the time is {strTime}")
            
            elif 'tell school address' in command:
                            speak("CCES school is in Qasimabad hyderabad")
            
            elif 'who made you' in command:
                            speak("Abdul Muhaimin, Student of CCES made me and i like him")
            


else:
    speak("wrong Option is choosed")    
