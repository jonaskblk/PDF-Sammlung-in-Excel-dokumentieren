class Buch:

    def __init__(self, id, jahr, typ, name, autor):
        self.id = id
        self.jahr = jahr
        self.typ = typ
        self.name = name
        self.autor = autor

    def toText(self):
        return (self.id + " " + self.jahr + " " + self.typ + " " + self.name + " " + self.autor)

    def as_dict(self):
        return {'ID': int(self.id), 'Jahr': int(self.jahr), 'Typ': self.typ, 'Name': self.name, 'Autor': self.autor}

    @staticmethod
    def extrahiereId(dateiname):
        return int(dateiname.split()[0])

    @staticmethod
    def extrahiereJahr(dateiname):
        return str(dateiname.split()[1])

    @staticmethod
    def extrahiereTyp(dateiname):
        return str(dateiname.split()[2])

    @staticmethod
    def extrahiereName(dateiname):
        temp = dateiname.split()
        s = temp[3:-1]
        k = ""
        for i in range(len(s)):
            k = k + s[i] + " "
        return str(k.rstrip())

    @staticmethod
    def extrahiereAutor(dateiname):
        temp = dateiname.split()[-1]
        return str(temp[:-4])
    
