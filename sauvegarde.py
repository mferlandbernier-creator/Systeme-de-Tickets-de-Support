import json

def sauvegarde(titre, 
               description, 
               utilisateur, 
               statut, 
               date_creation):
    with open("sauvegarde.json", "a") as fichier:
        fichier.write(f"""titre: {titre}\n 
                          description: {description}\n
                          utilisateur: {utilisateur}\n
                          statut: {statut}\n
                          date_creation: {date_creation}\n""")
        
