class Ticket:
    compteur = 1

    def __init__(self, titre, description, utilisateur):
        self.id = Ticket.compteur
        Ticket.compteur += 1 
        self.titre = titre
        self.description = description
        self.utilisateur = utilisateur
        self.statut = "Ouvert"
        self.date_creation = "2025-12-18" #Date fictive

    def fermer(self):
        self.statut = "Fermé"

    def afficher(self):
        print (f"{self.id}, Titre: {self.titre}, Utilisateur:{self.utilisateur} Statut: {self.statut}, Date: {self.date_creation}")
