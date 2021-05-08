import speech_recognition as sr
import time
import os
import callback
import konus

'''
Özellikler:
1) Para Birimleri
2) Wikipedia Araştırma
3) Google Arama
4)  Saat Kaç
'''

mic = sr.Microphone()
r = sr.Recognizer()





r.listen_in_background(mic, callback.callback)
while True: time.sleep(0.1)
