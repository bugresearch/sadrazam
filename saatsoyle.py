import datetime
import konus

def saatsoyle():
    an = datetime.datetime.now()
    konusma = "Şu an saat "+str(an.hour)+"ı "+str(an.minute)+" geçiyor."
    konus.konus(konusma)
    return True