from gtts import gTTS
import webbrowser
from playsound import playsound
def ispresent(x):
    string=x.split(" ")
    for i in string:
        if i=='hi':
            k=1
        elif i=='browser':
            k=2
        elif i=='whatsapp':
            k=3
    return k

while(True):
    a=input()
    k=ispresent(a)
    if  k==1:
        playsound(r'c:\Users\SANGEETHA\downloads\hithere.mp3')
        playsound(r'c:\Users\SANGEETHA\downloads\whatcanidoforyou.mp3')
    
    elif k==2:
        webbrowser.open('https://google.com')
        playsound(r'c:\Users\SANGEETHA\downloads\happylearning.mp3')
    elif k==3:
        webbrowser.open('https://web.whatsapp.com')
        playsound(r'c:\Users\SANGEETHA\downloads\openingwhatsapp.mp3')
    
'''    
def text_to_speech():
    text=input()
    speech=gTTS(text=text,lang='en')
    speech.save(r'c:\Users\SANGEETHA\downloads\openingwhatsapp.mp3')
    

    

text_to_speech()
playsound(r'c:\Users\SANGEETHA\downloads\openingwhatsapp.mp3')
'''

