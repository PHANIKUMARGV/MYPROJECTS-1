import pyautogui as p
import win32api as o
import pyttsx3 as e
import time as t1
import speech_recognition as sr
import cv2
import datetime as d
import pytz as do
import random as ra
t=''
usefull=["https://www.geeksforgeeks.org/","https://www.tutorialspoint.com/java8/index.htm","https://www.javatpoint.com/"]
favs=["bc0KhhjJP98","hYL_y4U4pxM","zyR-tE0siwY","-t5b7MrWENk","wJVq_6DkavM","cChZEYVRvIE"]
while t!='bye':
    f=0
    k=0
    r=sr.Recognizer()
    engine=e.init()
    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice', en_voice_id)
    engine.setProperty('rate',125)
    engine.setProperty('volume', 0.9)
    print('Say something:',end='')
    engine.say("Say something")
    engine.runAndWait()
    mic=sr.Microphone()
    with mic as source:
        #r.adjust_for_ambient_noise(source)                         
        audio=r.listen(source)
        t=r.recognize_google(audio)
    print(t)
    if t=='bye':
        break
    if t.casefold()=='open my favourite song' or t.casefold()=='my favourite song' or t.casefold()=='play a song for me':
        p.hotkey('winleft')
        t1.sleep(2)
        p.typewrite('chrome\n',0.2)
        l=ra.randint(0,len(favs)-1)
        p.typewrite('https://www.youtube.com/watch?v='+favs[l]+"\n",0.2)
        engine.say("here is your song enjoyy!")
        engine.runAndWait()
        t1.sleep(10)
        p.moveTo(600,600,0.25)
        p.click()
    elif t.casefold()=='anything usefull stuff' or t.casefold()=="show something interesting":
        p.hotkey('winleft')
        t1.sleep(2)
        p.typewrite('chrome\n',0.2)
        l=ra.randint(0,len(favs)-1)
        p.typewrite(usefull[l]+"\n",0.2)
        engine.say("here are your GATE tips!")
        engine.runAndWait()
    elif t.casefold()=='open notepad' or t.casefold()=='notepad':
        p.hotkey('winleft')
        t1.sleep(2)
        p.typewrite('notepad\n',0.2)
        engine.say('Notepad is opened,say something to type') ####
        engine.runAndWait()
        with mic as source:
    # r.adjust_for_ambient_noise(source)                         
            audio=r.listen(source)
            t=r.recognize_google(audio)
        p.typewrite(t,0.4)
    elif t.casefold()=='take a photo':
        videoCaptureObject = cv2.VideoCapture(0)
        result = True
        while(result):
            ret,frame = videoCaptureObject.read()
            cv2.imwrite("NewPicture.jpg",frame)
            result = False
        videoCaptureObject.release()
        cv2.destroyAllWindows()
        engine.say('Your photo has been captured and saved to desktop,check your desktop once')
        engine.runAndWait()
    elif t.casefold()=='what is the time':
        k=d.datetime.now(do.timezone('Asia/Kolkata'))
        f=k.hour
        if f>12:
            f=f-12
        print(k.hour,k.minute,k.second,sep=':')
        engine.say("%s hours %s minutes and %s seconds.."%(f,k.minute,k.second))
        engine.runAndWait()
    elif t.casefold()=='volume up':
        p.moveTo(1671,1055,0.25)
        p.click()
        f=ra.randint(3,4)
        k=ra.randint(100,250)
        p.moveTo(1551,994,0.25)
        p.moveTo(1551+k,994,1)
        p.click()
        engine.say("heyyy  your volume got raised dude!")
        engine.runAndWait()
        p.moveTo(1671,1055,0.25)
        p.click()
    elif t.casefold()=='volume down':
        p.moveTo(1671,1055,0.25)
        p.click()
        f=ra.randint(3,4)
        k=ra.randint(100,250)
        p.moveTo(1551+k,994,0.25)
        p.moveTo(1585,994,1)
        p.click()
        engine.say("heyyy  your volume fell down dude!")
        engine.runAndWait()
        p.moveTo(1671,1055,0.25)
        p.click()
    elif t.casefold()=='open microsoft teams':
        p.moveTo(1919,1042,0.25)
        p.click()
        p.moveTo(56,441,0.5)
        p.click(clicks=2)
        t1.sleep(10)
        p.moveTo(35,522,0.5)
        p.click()
    elif t.casefold()=='open python environment':
        p.hotkey('winleft')
        t1.sleep(2)
        p.typewrite('idle\n',0.2)
    elif t.casefold()=='open oracle':
        p.moveTo(1919,1042,0.25)
        p.click()
        p.moveTo(159,52,0.3)
        p.click(clicks=2)
        t1.sleep(5)
        p.typewrite('scott\n',0.25)
        p.typewrite('tiger\n',0.25)
        engine.say('Oracle sql is opened')   
engine.say('Bye sweetheart take care its corona times!!')
engine.runAndWait()

    


