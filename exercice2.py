
import json
import csv
from datetime import datetime


# Mixin pour la sérialisation JSON
class Serializable:

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    @classmethod
    def from_json(cls, json_str):
        return cls(**json.loads(json_str))


# Mixin pour conserver l'historique
class Historisable:

    def __init__(self):
        self.historique = []

    def enregistrer_etat(self):
        self.historique.append(
            (datetime.now(), self.__dict__.copy())
        )


# Mixin pour journaliser les actions
class Journalisable:

    def journaliser(self, message):
        print(f"[Journal] {datetime.now()}: {message}")


# Mixin pour ajouter un horodatage
class Horodatable:

    def horodater(self):
        return datetime.now()


# Classe principale Contrat
class Contrat(Serializable, Historisable, Journalisable, Horodatable):

    def __init__(self, id, description):
        Historisable.__init__(self)

        self.id = id
        self.description = description

    def modifier(self, nouvelle_desc):
        self.journaliser(
            f"Modification du contrat {self.id}"
        )

        self.enregistrer_etat()

        self.description = nouvelle_desc

    def afficher_historique(self):
        print("\nHistorique du contrat :")

        for date, etat in self.historique:
            print(f"{date} -> {etat}")


# Programme principal
c = Contrat(1, "Initial")

# Modification
c.modifier("Révisé")

# Affichage JSON
print("\nContrat en JSON :")
print(c.to_json())

# Affichage historique
c.afficher_historique()

# Horodatage
print("\nDate actuelle :")
print(c.horodater())
