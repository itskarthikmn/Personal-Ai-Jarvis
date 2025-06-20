import os
import re
from shlex import quote
import sqlite3
import struct
import subprocess
import time
import webbrowser
import eel
from hugchat import hugchat 
import pvporcupine
import pyaudio
import pyautogui
import pywhatkit as kit
import pygame
from backend.command import speak
from backend.config import ASSISTANT_NAME
from backend.helper import extract_yt_term, remove_words

# to define cursor
conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()


@eel.expose
def play_assistant_sound():
    try:
        pygame.mixer.init()
        sound_file = r"frontend\assets\audio\start_sound.mp3"
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error playing sound: {e}")

        
def openCommand(query):
    query=query.replace(ASSISTANT_NAME,"")
    query=query.replace("open","")
    query.lower()

    app_name = query.strip()
    # strip() commend deletes extra space before and after the query

    if app_name != "":

        try:
            cursor.execute( 
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing"+search_term+"on YouTube")
    kit.playonyt(search_term)

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:      
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        print("[Listening for hotword: 'jarvis' or 'alexa']")
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key ctrl+k
                import pyautogui as autogui
                autogui.keyDown("ctrl")
                autogui.press("k")
                time.sleep(2)
                autogui.keyUp("win")                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


# used to find the contact which we tell
def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT Phone FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0


def whatsApp(Phone, message, flag, name):
    

    if flag == 'message':
        target_tab = 21
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 17
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 11
        message = ''
        jarvis_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={Phone}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)

def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="backend\cookie.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response

# this is for feature.py
import eel

def faceRecognition():
    eel.showJarvisMessage("Recognizing Face...")
    # your face recognition logic...
    eel.showJarvisMessage("Face Match Found")
    # after success
    eel.showJarvisMessage("Access Granted")
