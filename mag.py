class Mag():
    # Třída reprezentuje mága, který se může specializovat na určitá kouzla

    # jmeno = jméno mága
    # specializace = specializace mága, například oheň, voda, temná magie nebo čísta magie

    def __init__(self, jmeno, specializace):
        self.jmeno = jmeno
        self.specializace = specializace

    # Mág použije kouzlo
    def pouzij_kouzlo(self, kouzlo):
        if kouzlo.typ in self.typy_kouzel:
            print("{0} použil kouzlo {1}".format(self.jmeno, kouzlo.nazev))
        else:
            print("{0} nemůže použít {1} s typem poškození {2}".format(self.jmeno, kouzlo.nazev, kouzlo.typ))

    @property
    def specializace(self):
        return self._specializace

    @specializace.setter
    def specializace(self, nova_specializace):
        self._specializace = nova_specializace

        self.typy_kouzel = set()  # set/list typů poškození, která mág může používat (ovlivněno specializací)

        if nova_specializace == "voda":
            self.typy_kouzel.add("vodni")
            self.typy_kouzel.add("ohnive")
        elif nova_specializace == "ohen":
            self.typy_kouzel.add("ohnive")
            self.typy_kouzel.add("temne")
        elif nova_specializace == "cista":
            self.typy_kouzel.add("ciste")
        elif nova_specializace == "temna":
            self.typy_kouzel.add("temne")

        print("{0} se nyni specializuje na {1}".format(self.jmeno, self._specializace))

    # Vrací textovou reprezentaci
    def __str__(self):
        return "{0} je mág se specializací na {1}".format(self.jmeno, self._specializace)