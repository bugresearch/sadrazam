import http.client
import json
import konus

conn = http.client.HTTPSConnection("api.collectapi.com")
headers = {'content-type': "application/json",'authorization': "apikey xxx:xxx"}
conn.request("GET", "/economy/currencyToAll?int=10&base=TRY", headers=headers)
res = conn.getresponse()
data = res.read()
liste = json.loads(data.decode("utf-8"))

def parabirimibul(birim):
    for i in liste["result"]["data"]:
        if i["code"] == birim:
            return(1/i["rate"])

def parabirimi(birim, kisaltma):
    konusma = "Şu anda 1 "+birim+str(int(parabirimibul(kisaltma)))+" türk lirası."
    konus.konus(konusma)
    return True
