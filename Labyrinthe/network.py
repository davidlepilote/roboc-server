import socket

# Création du serveur
import select

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((', 12345'))
serveur.listen(5)

clients = []

connexions_demandees, wl, xl = select.select([serveur], [], [], 0.05)

for connexion in connexions_demandees:
    client, infos = connexion.accept()
    clients.append(client)
