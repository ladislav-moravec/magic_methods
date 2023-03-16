from kouzlo import Kouzlo
from mag import Mag

# Vytvoříme kouzla
ohniva_koule = Kouzlo("Ohnivá koule", "ohnive")
kletba_smrti = Kouzlo("Kletba Smrti", "temne")
absolutni_nula = Kouzlo("Absolutní Nula", "vodni")
manipulace_zive_energie = Kouzlo("Manipulace Živé Energie", "cista")
# Vytvoříme kouzelníka
gandalf = Mag("Gandalf", "voda")
# Zkoušíme používat kouzla
gandalf.pouzij_kouzlo(absolutni_nula)
gandalf.pouzij_kouzlo(kletba_smrti)
gandalf.specializace = "temna"
gandalf.pouzij_kouzlo(kletba_smrti)
gandalf.pouzij_kouzlo(manipulace_zive_energie)
gandalf.specializace = "ohen"
gandalf.pouzij_kouzlo(ohniva_koule)