from datetime import datetime
import json


# Mixin 1 : Horodatage
class Horodatable:
    def horodatage(self):
        print(f"[LOG] Action à {datetime.now()}")


# Mixin 2 : Validation
class Validable:
    def valider(self):
        if not getattr(self, "titre", None):
            raise ValueError("Titre manquant")

        print("Validation OK")


# Mixin 3 : Sérialisation
class Serializable:
    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)


# Classe principale
class Document(Horodatable, Validable, Serializable):

    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu

    def sauvegarder(self):
        self.horodatage()
        self.valider()
        print(f"Document '{self.titre}' sauvegardé.")


# Programme principal
doc = Document("Rapport", "Contenu important")

doc.sauvegarder()

print("\nDocument en JSON :")
print(doc.to_json())