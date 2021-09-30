import os
import pandas as pd
from buch import *

namen = list()
dateinamenTemp = list()
dateinamen = list()

xlWorkbookPath = "C:/Users/jonas/Desktop/test.xlsx"
testpath = "C:/Users/jonas/Desktop/Quellen"

for files in os.walk(testpath, topdown=False):
    dateinamenTemp.append(files[2])

for i in range(len(dateinamenTemp[0])):
    dateinamen.append(dateinamenTemp[0][i])

buchliste = list()

for i in dateinamen:
    tempId = Buch.extrahiereId(str(i))
    tempJahr = Buch.extrahiereJahr(str(i))
    tempTyp = Buch.extrahiereTyp(str(i))
    tempName = Buch.extrahiereName(str(i))
    tempAutor = Buch.extrahiereAutor(str(i))

    buchliste.append(Buch(tempId, tempJahr, tempTyp, tempName, tempAutor))


def get_my_key(obj):
    return int(obj.id)


buchliste.sort(key=get_my_key)

for b in range(len(buchliste)):
    buchliste[b].id = str(buchliste[b].id)

# for b in range(len(buchliste)):
    # print(buchliste[b].toText())

df = pd.DataFrame([x.as_dict() for x in buchliste])

df.to_excel("Quellen.xlsx", sheet_name='Liste', index=False)
