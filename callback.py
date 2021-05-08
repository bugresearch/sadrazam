import kurhesapla
import konus
import saatsoyle
import speech_recognition as sr
import os
import time

mic = sr.Microphone()
r = sr.Recognizer()

def callback(recognizer, audio):
    try:
        ses = r.recognize_google(audio, language='tr-tr')
        ses = ses.lower()
        sadrazam = ses.find('sadrazam ')
        if sadrazam == 0:
            # Eğer Sadrazam Geçiyorsa
            text = ses.replace("sadrazam ","")
            saatkac = text.find("saat")
            dolar = text.find("dolar")
            euro = text.find("euro")
            sterlin = text.find("sterlin")
            google = text.find("google ")
            wikipedia = text.find("wikipedia ")
            if saatkac == 0: saatsoyle.saatsoyle()
            if dolar == 0: kurhesapla.parabirimi("dolar","USD")
            if euro == 0: kurhesapla.parabirimi("euro","EUR")
            if sterlin == 0: kurhesapla.parabirimi("sterlin","GPB")
            if google == 0:
                text = text.replace("google ","")
                konus.konus("Tamam Google'da "+text+"'ı aratıyorum")
                text = text.replace(" ","+")
                os.system("start https://www.google.com/search?q="+text)
            if wikipedia == 0:
                text = text.replace("wikipedia ","")
                konus.konus("Tamam Wikipedia'da "+text+"'ı aratıyorum")
                text = text.replace(" ","+")
                os.system("start https://tr.wikipedia.org/w/index.php?search="+text)
            if text.find("merhaba") == 0: konus.konus("Merhaba ben sadrazam sana nasıl yardımcı olabilirim")
            if text.find("yaş") == 0: konus.konus("Yapay zekaya yaş sorulmaz.")
            if text.find("hesap makinesi") == 0: 
                os.system("calc.exe")
                konus.konus("Tamam hesap makinesini açtım")
            if text.find("bilgisayarı kapat") == 0:
                konus.konus("Tamam bilgisayarı kapatıyorum kendine iyi bak")
            if text.find("kendini kapat") == 0:
                konus.konus("Tamam ben gidiyorum. Kendine iyi bak. Eğer yine kullanmak istersen çift tıklaman gerekecek")
                exit()
    except sr.WaitTimeoutError:
        print("")

    except sr.UnknownValueError:
        print("")

    except sr.RequestError:
        print("")
