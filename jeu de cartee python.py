import tkinter as tk
import random
import time

# Liste des icônes de cartes
icons = [
    "🍎 ", "🍎 ", "🍉 ", "🍉 ", " 🌸", " 🌸", "✨", "✨",
    "🍒", "🍒", "❤️", "❤️", "🍕 ", "🍕 ", "⚽️", "⚽️"
]

# Mélanger les icônes
random.shuffle(icons)

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Jeu de Cartes Mémoire")

# Fonction pour retourner la carte
def card_click(i):
    global first, first_compteur

    buttons[i].config(text=icons[i])
    root.update()

    if first is None:
        first = icons[i]
        first_compteur = i
    elif first == icons[i] and first_compteur != i:
        first = None
        first_compteur= None
    else:
        time.sleep(1)
        buttons[first_compteur].config(text=" ")
        buttons[i].config(text=" ")
        first = None
        first_compteur = None

# Fonctions pour les boutons

def rejouer():
    for button in buttons:
        button.config(text=" ", state=tk.NORMAL)
    random.shuffle(icons)

def quitter():
    root.destroy()

# Créer et placer les boutons de cartes
buttons = []
first = None
first_compteur = None
for i in range(16):
    button = tk.Button(root, text=" ", width=4, height=2,
                       font=("Arial", 28),
                       command=lambda i=i: card_click(i),
                       bg="light blue")  # Couleurs personnalisées
    button.grid(row=i // 4, column=i % 4)
    buttons.append(button)

# Ajouter les nouveaux boutons avec des couleurs spécifiques

rejouer_button = tk.Button(root, text="Rejouer", command=rejouer, bg="pink", fg="black")
rejouer_button.grid(row=4, column=2, columnspan=2)


quitter_button = tk.Button(root, text="Quitter", command=quitter, bg="yellow", fg="black")
quitter_button.grid(row=4, column=0, columnspan=2)

root.mainloop()


