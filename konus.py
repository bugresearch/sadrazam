from gtts import gTTS
import os



def konus(text):
    tts = gTTS(text=text, lang='tr')
    tts.save('merhaba.mp3')
    os.system("start merhaba.mp3")
    return True