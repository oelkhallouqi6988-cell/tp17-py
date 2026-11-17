
from datetime import datetime
import copy


# Mixin de validation
class ValidationMixin:

    def valider_titre(self):
        if not self.titre or not self.titre.strip():
            raise ValueError("Le titre est obligatoire et ne peut pas être vide.")


# Mixin d'historique
class HistoriqueMixin:

    def __init__(self):
        self.historique = []

    def enregistrer_historique(self):
        ancienne_description = copy.deepcopy(self.description)

        self.historique.append({
            "date": datetime.now(),
            "description": ancienne_description
        })

    def afficher_historique(self):
        if not self.historique:
            print("Aucun historique disponible.")
            return

        print("\n--- Historique des modifications ---")

        for version in self.historique:
            print(f"Date : {version['date']}")
            print(f"Description : {version['description']}")
            print("-----------------------------------")


# Mixin de journalisation
class JournalisationMixin:

    def journaliser(self, message):
        print(f"[Journal] {datetime.now()} : {message}")


# Classe principale
class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):

    def __init__(self, titre, description):
        HistoriqueMixin.__init__(self)

        self.titre = titre
        self.description = description
        self.date_creation = datetime.now()

        # Validation du titre
        self.valider_titre()

        # Journalisation de la création
        self.journaliser(
            f"Création de la tâche '{self.titre}'"
        )

    def mettre_a_jour(self, description):
        # Vérifier le titre avant la modification
        self.valider_titre()

        # Enregistrer l'ancienne description
        self.enregistrer_historique()

        # Modifier la description
        self.description = description

        # Journaliser la modification
        self.journaliser(
            f"Modification de la tâche '{self.titre}'"
        )


# Programme principal
tache = Tache(
    "Développer une application",
    "Créer la structure du projet"
)

tache.mettre_a_jour(
    "Créer les classes principales"
)

tache.mettre_a_jour(
    "Ajouter les mixins"
)

print("\n--- Informations de la tâche ---")
print(f"Titre : {tache.titre}")
print(f"Description actuelle : {tache.description}")
print(f"Date de création : {tache.date_creation}")

tache.afficher_historique()
