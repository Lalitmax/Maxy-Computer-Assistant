import openpyxl
import speech_recognition as sr
import pyttsx3
import time


import datetime
date = datetime.datetime.now()
date = str(date)
date = date.split()
date = date[0]
date = date.split('-')
date = date[2]
day = int(date)
eng = pyttsx3.init()


def speak(text):

    eng.say(text)
    eng.runAndWait()


def comaaaaand(name):
    
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print(name)
        speak(name)
        print('listening...')

        r.pause_threshold = 5
        audio = r.listen(mic, timeout=45)

    try:
        print('recognizing...')
        text = r.recognize_google(audio,language="en-in")
        text = text.lower()
    except Exception as e:
        
        return "None"
    return text
    


rm = openpyxl.load_workbook("Attendancer.xlsx")

sh1 = rm["Sheet1"]
sh2 = rm["Sheet2"]

length = sh1.max_row
# for write


# for read
def makeAt():
    li_name = []
    for i in range(2, length+1):
        name = sh1.cell(i, 1).value

        rc = comaaaaand(name)

        if ("present sir" in rc) or ("yes sir" in rc) or ("sir present" in rc):
            sh2.cell(row=i, column=1+day, value="Present")
            rm.save("Attendancer.xlsx")

        else:
            sh2.cell(row=i, column=1+day, value="Not Present")
            rm.save("Attendancer.xlsx")


# makeAt()

# atd
