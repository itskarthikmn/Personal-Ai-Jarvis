import eel
from backend.auth import recoganize
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import *

def start():
    eel.init("frontend")
    play_assistant_sound()

    @eel.expose
    def init():
        eel.hideLoader()
        eel.showJarvisMessage("Welcome to Jarvis")
        speak("Welcome to Jarvis")

        eel.showJarvisMessage("Ready for Face Authentication")
        speak("Ready for Face Authentication")

        eel.showJarvisMessage("Recognizing Face…")
        flag = recoganize.AuthenticateFace()

        if flag == 1:
            eel.showJarvisMessage("Face Match Found")
            speak("Face recognized successfully")
            eel.hideFaceAuth()
            eel.hideFaceAuthSuccess()

            eel.showJarvisMessage("Access Granted")
            speak("Welcome to Your Assistant")
            eel.hideStart()
            play_assistant_sound()
        else:
            eel.showJarvisMessage("Face not recognized. Please try again")
            speak("Face not recognized. Please try again")

    eel.start("index.html", mode='chrome', size=(900, 700))

