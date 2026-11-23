def FENETRE():
    salle_50 = 5
    salle_40 = 5
    salle_30 = 10
    salle_20 = 10
    salle_150 = 3

    import tkinter as tk
    from tkinter import ttk

    title_font = ("arial", 30, "bold")
    options = ["Matin", "Après-Midi", "Journée"]

    salle_total = {
        5: 50,
        5: 40,
        10: 30,
        10: 20,
        3: 150
    }

    salle_matin_dispo = {
        5: 50,
        5: 40,
        10: 30,
        10: 20,
        3: 150
    }

    salle_aprem_dispo = {
        5: 50,
        5: 40,
        10: 30,
        10: 20,
        3: 150
    }

    salle_journée_dispo = {
        5: 50,
        5: 40,
        10: 30,
        10: 20,
        3: 150
    }

    def confirm_action():
        time_ask = options.index(var.get()) + 1
        if 'label' in locals():
            label.destroy()
        if 'menu_deroulant' in locals():
            menu_deroulant.destroy()
        if 'confirm_button' in locals():
            confirm_button.destroy()
        labe2 = tk.Label(f1, text="Pour combien de personne voulez vous reserver une/des salle(s)")
        labe2.grid(sticky="w", pady=10)
        entry1 = tk.Entry(f1, width=50)
        entry1.grid(sticky="w", pady=10)
        nbr_reserv = entry1.get
        confirm_button1 = tk.Button(f1, text="Confirmer")
        confirm_button1.grid(sticky="w", pady=10)

    # Création de la fenêtre principale
    f1 = tk.Tk()
    f1.title("Menu de réservation")
    f1.geometry("960x1080")

    # Titre
    title = tk.Label(f1, text="Réservation", font=title_font)
    title.grid(sticky="w", pady=10)

    # Menu déroulant pour sélectionner le moment de la réservation
    label = tk.Label(f1, text="Pour quand voulez vous reserver")
    label.grid(sticky="w", pady=10)
    var = tk.StringVar(value=options[0])  
    menu_deroulant = tk.OptionMenu(f1, var, *options)
    menu_deroulant.grid(sticky="w", pady=10)
    confirm_button = tk.Button(f1, text="Confirmer", command=confirm_action)
    confirm_button.grid(sticky="w", pady=10)

    # Bouton pour fermer la fenêtre
    close = tk.Button(f1, text="X", command=f1.destroy)
    close.place(relx=0.99, y=110, anchor="ne")


    
    # Ajouter le tableau (Treeview) pour l'agenda
    columns = ("Date", "Moment")
    tree = ttk.Treeview(f1, columns=columns, show='headings')

    # Définir les en-têtes du tableau
    tree.heading("Date", text="Date")
    tree.heading("Moment", text="Moment")

    # Insérer des données dans le tableau
    agenda = [
        ("29/11/2024", "10:00"),
        ("29/11/2024", "15:00"),
        ("30/11/2024", "09:00"),
    ]
    
    for event in agenda:
        tree.insert("", tk.END, values=event)

    # Ajouter une barre de défilement pour le tableau
    scrollbar_y = ttk.Scrollbar(f1, orient="vertical", command=tree.yview)
    scrollbar_y.grid(row=7, column=1, sticky="ns", padx=5)

    tree.configure(yscrollcommand=scrollbar_y.set)
    tree.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # Lancer l'application
    f1.mainloop()


