# Importing modules
from tkinter import *
import pyttsx3
from PyDictionary import PyDictionary

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def meaning():
    dic = PyDictionary()
    query = str(text.get())
    word = dic.meaning(query)
    res=''
    for state in word:
        res+=(str(word[state][0]))+'\n'
        spokenText.set(res)
        speak("the meaning  is" + str(word[state]))

# Creating the window
wn = Tk() 
wn.title("DataFlair Dictionary")
wn.geometry('600x400')
wn.configure(bg='#F0F0F0')  # Set background color using hexadecimal color code

# Creating the variables
text = StringVar(wn)
spokenText = StringVar(wn)

# The main label
Label(wn, text='DataFlair - Speak the Meaning', bg='#F0F0F0', fg='#333333', font=('Arial', 20, 'bold')).place(x=100, y=10)  # Set font and font color

# Getting the input of word from the user
Label(wn, text='Please enter the word', bg='#F0F0F0', font=('Arial', 13, 'normal')).place(x=20, y=70)  # Set font
Entry(wn, textvariable=text, width=35, font=('Arial', 13, 'normal')).place(x=20, y=110)  # Set font

# Label to show the correct word
queryLabel = Label(wn, textvariable=spokenText, bg='#F0F0F0', font=('Arial', 13, 'normal'), wraplength=500)
queryLabel.place(x=20, y=130)
spokenText.set("Which word do you want to find the meaning, sir/madam?")
speak("Which word do you want to find the meaning, sir or madam?")

# Button to speak the meaning
Button(wn, text="Speak Meaning", bg='#4CAF50', fg='white', font=('Arial', 13), command=meaning).place(x=230, y=350)  # Set background color, font color, and font

# Runs the window till it is closed by the user
wn.mainloop()
