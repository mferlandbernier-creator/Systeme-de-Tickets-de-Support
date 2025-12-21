# tickets/gestion.py

def generer_nouvel_id(tickets: list) -> int:
    if len(tickets) == 0:
        return 1

    max_id = tickets[0].id
    for t in tickets:
        if t.id > max_id:
            max_id = t.id
    return max_id + 1


def creer_ticket(tickets: list, titre: str, description: str, auteur: str, priorite: str = "moyenne"):
    # Import local pour éviter certains problèmes d'import
    from ticket import Ticket

    nouvel_id = generer_nouvel_id(tickets)
    ticket = Ticket(nouvel_id, titre, description, auteur, priorite)
    tickets.append(ticket)
    return ticket


def lister_tickets(tickets: list) -> list:
    return tickets


def trouver_ticket_par_id(tickets: list, ticket_id: int):
    for t in tickets:
        if t.id == ticket_id:
            return t
    return None


def modifier_statut(tickets: list, ticket_id: int, nouveau_statut: str) -> bool:
    ticket = trouver_ticket_par_id(tickets, ticket_id)
    if ticket is None:
        return False
    ticket.statut = nouveau_statut
    return True


def supprimer_ticket(tickets: list, ticket_id: int) -> bool:
    for i in range(len(tickets)):
        if tickets[i].id == ticket_id:
            tickets.pop(i)
            return True
    return False
