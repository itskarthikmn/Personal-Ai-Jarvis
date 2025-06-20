
import pyttsx3
import speech_recognition as sr
import eel
import time

engine = pyttsx3.init()
engine.setProperty('rate', 174)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    # default function that get all the avilable voices
    voices = engine.getProperty('voices')
    # print(voices)
    # set another voice 
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 174)
    eel.receiverText(text)

@eel.expose
def takecommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source,10,8)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-US")
            print(f"User said: {query}")
            speak(query)
            # eel.ShowHood()
            return query
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"API error: {e}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
        
@eel.expose
def takeAllCommands(message=None):
    if message is None:
        query=takecommand()
        if not query:
            return
        print(query)
        eel.senderText(query)
    else:
        query=message
        print(f"Message received: {query}")
        eel.senderText(query)
    try:
        if query:
            if "open" in query:
                from backend.feature import openCommand
                openCommand(query)
            elif "send message" in query or "call" in query or "video call" in query:
                from backend.feature import findContact, whatsApp
                flag = ""
                Phone, name = findContact(query)
                if Phone != 0:
                    if "send message" in query:
                        flag = 'message'
                        speak("What message to send?")
                        query = takecommand()
                    elif "call" in query:
                        flag = 'call'
                    else:
                        flag = 'video call'
                    whatsApp(Phone, query, flag, name)
            elif "YouTube" in query:
                from backend.feature import PlayYoutube
                PlayYoutube(query)
            else:
                from backend.feature import chatBot
                chatBot(query)
                # print("I;m not sure what to do.")
                # speak("I;m not sure what to do.")
    except Exception as e:
        print(f"[Error]:{e}")
        speak("Something went wrong.")
        eel.DisplayMessage("Something went wrong.")
    eel.ShowHood()
    time.sleep(2)
    return query
