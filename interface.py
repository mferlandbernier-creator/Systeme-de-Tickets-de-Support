def interface():
    '''
    Affiche un menu interactif pour la gestion des tickets.

    Retourne:
        dict: Un dictionnaire contenant au minimum la clé "action".
              Des clés supplémentaires sont présentes selon l'action choisie :
                - "action": "creer", "titre": str, "description": str, "utilisateur": str
                - "action": "afficher"
                - "action": "fermer", "id": str
                - "action": "quitter"
    '''

    MENU = (
            "\n--- Interface Ticket ---\n"
            "1. Créer un ticket\n"
            "2. Afficher tous les tickets\n"
            "3. Fermer un ticket\n"
            "4. Quitter\n"
        )

    while True:
        choix = input(f"{MENU}\nVotre choix:")

        match choix:
            case "1":
                titre = input("Titre du ticket: ")
                description = input("Description de votre ticket: ")
                utilisateur = input("Votre nom: ")
                return {
                    "action": "creer",
                    "titre": titre,
                    "description": description,
                    "utilisateur": utilisateur
                }
            case "2":
                return {"action: afficher"}
            case "3":
                id_ticket = input("Quel numéro d'ID voulez vous fermer? ")
                return {"action": "fermer", "id": id_ticket}
            case "4":
                print("Fin du programme.")
                break
            case _:
                print("Choix invalide.")