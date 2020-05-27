# importing speech recognition package from google api 
import speech_recognition as sr  
#import playsound # to play saved mp3 file 
#from gtts import gTTS # google text to speech 
import os # to save/open files 
#import wolframalpha # to calculate strings into formula 
import sys
import requests
import json
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)

num = 1
def assistant_speaks(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("PerSon : ", output) 
  
    #toSpeak = gTTS(text = output, lang ='en', slow = False) 
    # saving the audio file given by google text to speech 
    file = str(num)+".mp3"
    toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    #playsound.playsound(file, True)  
    os.remove(file) 
  
  
  
def get_audio(): 
    
    rObject = sr.Recognizer() 
    audio = '' 

    with sr.Microphone() as source: 
        engine.say("Beeeep") 
        print("Beeeep")
        engine.runAndWait()
        
          
        # recording the audio using speech recognition 
        audio = rObject.listen(source, phrase_time_limit = 3)  
    print("Stop.") # limit 5 secs 
  
    try: 
  
        text = rObject.recognize_google(audio, language ='en-US') 
        print("You : ", text) 
        return text 
  
    except: 
  
        engine.say("Could not understand your audio, PLease try again !") 
        print("Could not understand your audio, PLease try again !") 
        engine.runAndWait()
        return "There"
def config_tool():
    print("Welcome to Host Configuration Checker")
    engine.say("Welcome to Host Configuration Checker")
    engine.runAndWait()

    URL_BASE = "http://speb91.lss.emc.com:8080/RestapiSystemManager/sysmgr/"
    hosts = ['speb91.lss.emc.com', 'speb90.lss.emc.com', 'speb97.lss.emc.com']

    for host in hosts:
        print("Pinging host ", host + "...")
        engine.say("Pinging host " + host)
        engine.runAndWait()
        url=URL_BASE+"pinghost?hostname="+host
        print(url)
        req = requests.get(url=url)
        json_data = req.json()
        res = json_data[0]['exitStatus']
        if res == 0:
            out = json_data[0]['commandOutput']
            print("Ping status  : " + out)
            engine.say(out)
            engine.runAndWait()

        print("ssh host ", host + "...")
        engine.say("ssh host " + host)
        engine.runAndWait()
        url=URL_BASE+"sshhost?hostname="+host
        print(url)
        req = requests.get(url=url)
        json_data = req.json()
        res = json_data[0]['exitStatus']
        if res == 0:
            out = json_data[0]['commandOutput']
            print("ssh status  : " + out)
            engine.say(out)
            engine.runAndWait()

        print("Check host configuration ", host + "...")
        engine.say("Check host configuration " + host)
        engine.runAndWait()
        url=URL_BASE+"checkhost?hostname="+host
        print(url)
        req = requests.get(url=url)
        json_data = req.json()
        res = json_data[0]['exitStatus']
        if res == 0:
            out = json_data[0]['commandOutput']
            print("Check host configuration info : " + out)
            engine.say(out)
            engine.runAndWait()

    print("Thankyou")
    engine.say("Thankyou")
    engine.runAndWait()
  

def sanity_test():
    import shutil
    import psutil
    engine.say("Checking the disk RAM and CPU usage, hold on")
    print("Checking the disk RAM and CPU usage, hold on")
    engine.runAndWait()
    path=r"C:"
    print(path)
    stat = shutil.disk_usage(path)
    dsk = int(((int(stat.total/1024/1024/1024)-int(stat.free/1024/1024/1024))/int(stat.total/1024/1024/1024) ) * 100)
    cppu = psutil.cpu_percent()
    print(str(stat)+str(dsk))
    memor = psutil.virtual_memory().percent
    if dsk < 90 and cppu < 90 and memor < 90:
        print("Looks like All the resources are utilized less than 80%")
        engine.say("Looks like All the resources are utilized less than 90%")
        engine.runAndWait()
    else:
        engine.say("Looks like the system is running short of resources")
        engine.runAndWait()
    print("Do you want me to play the status report from your previous shift employee? ")
    engine.say("Do you want me to play the status report from your previous shift employee? ")
    engine.runAndWait()
    text = get_audio().lower() 
    if "no" or "na" in text:
        return 0
    if "yes" or "yea" in text:
        yess()
		
def yess():
    print("There is a complaint from the customer who was having the issue ")
    engine.say("There is a complaint from the customer who was having the issue ")
    engine.runAndWait()
    raise SystemExit()
	
def check_status():
    URL="http://speb91.lss.emc.com:8080/RestapiSystemManager/sysmgr/sysinfo"
    #print("Connecting to " + URL)
    print("Connecting to " + URL)
    engine.say("Connecting to " + URL)
    engine.runAndWait()
    req = requests.get(url=URL)

    json_data = req.json()
    res = json_data[0]['exitStatus']
    if res == 0:
        out = json_data[0]['commandOutput']
        print("System Memory Info:\n" + out)
        engine.say(out)
        engine.runAndWait()

def kannan_server():
    URL="http://speb91.lss.emc.com:8080/RestapiSystemManager/sysmgr/sysinfo"
    print("Connecting to " + URL)
    engine.say("Connecting to " + URL)
    engine.runAndWait()
    print("Getting System Memory Info")
    engine.say("Getting System Memory Info")
    engine.runAndWait()
    req = requests.get(url=URL)

    json_data = req.json()
    res = json_data[0]['exitStatus']
    if res == 0:
        out = json_data[0]['commandOutput']
        print("System Memory Info:\n" + out)
        engine.say(out)
        engine.runAndWait()
		
# Driver Code 
if __name__ == "__main__": 
    engine.say("Hello There, Please state your name after the beep sound")
    engine.runAndWait()
    name ='Human'
    name = get_audio() 
    print("Hello, " + str(name) + '.')
    engine.say("Hello, " + str(name) + '.') 
    engine.runAndWait()
      
    while(1): 
        print("What can i do for you?") 
        engine.say("What can i do for you?") 
        engine.runAndWait()
        text = get_audio().lower() 
  
        if text == 0:
            continue
          
        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
            print("Ok bye, "+ str(name)+'.')
            engine.say("Ok bye, "+ str(name)+'.') 
            engine.runAndWait()
            break
        
        if "sanity" in str(text) or "check" in str(text):
            print("Running sanity tests, Please hold on")
            engine.say("Running sanity tests, Please hold on")
            engine.runAndWait()
            sanity_test()

        if "status" in str(text) or "server" in str(text):
            print("Okie, checking the status of the servers. Hold on")
            engine.say("Okie, checking the status of the servers. Hold on")
            engine.runAndWait()
            kannan_server()

        if "config" in str(text) or "manager" in str(text) or "configuration" in str(text) or "run" in str(text):
            print("Okie, Running the configuration manager. Hold on")
            engine.say("Okie, running the configuration manager. Hold on")
            engine.runAndWait()
            config_tool()
            
  
        # calling process text to process the query 
        #process_text(text) 
		