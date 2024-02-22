from flask import Flask, render_template, request
from tkinter import *
import pyttsx3
from PyDictionary import PyDictionary

app = Flask(__name__)

def speak(audio, speed=120):  # Default speed is 200, adjust as needed
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', speed)  # Adjust speech rate here
    engine.say(audio)
    engine.runAndWait()

def meaning(query):
    dic = PyDictionary()
    word = dic.meaning(query)
    res=''
    for state in word:
        res+=(str(word[state][0]))+'\n'
        spokenText = "the meaning is" + str(word[state])
        speak(spokenText)
    return res

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_meaning', methods=['POST'])
def get_meaning():
    word = request.form['word']
    result = meaning(word)
    return result

if __name__ == '__main__':
    app.run(debug=True)
