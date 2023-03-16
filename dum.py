class Dum():
    # Třída reprezentuje dům, ve kterém je N bytů

    def __init__(self, pocet_bytu):
        self.pocet_bytu = pocet_bytu

        self.uloziste = [None] * pocet_bytu

    # Nastavuje hodnotu podle indexu
    def __setitem__(self, index, hodnota):
        if index > self.pocet_bytu - 1:
            print( "V tomto domě je pouze {0} bytů".format(self.pocet_bytu) )
        else:
            self.uloziste[index] = hodnota

    # Vrací hodnotu podle indexu
    def __getitem__(self, index):
        if index > self.pocet_bytu - 1:
            print( "V tomto domě je pouze {0} bytů".format(self.pocet_bytu) )
        else:
            return "V bytě číslo {0} je {1}".format(index, self.uloziste[index]) if self.uloziste[index] else "Byt číslo {0} je na prodej".format(index)

    # Vrací textovou reprezentaci
    def __str__(self):
        reprezentace = ""
        for index, hodnota in enumerate(self.uloziste):
            reprezentace += "V bytě číslo {0} je {1}\n".format(index, hodnota) if hodnota else "Byt číslo {0} je na prodej\n".format(index)
        return reprezentace