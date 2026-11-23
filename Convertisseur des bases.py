
import tkinter as tk

title_font = ("arial", 30, "bold")
options = ["Base 16 (Hexadécimal)", "Base 10 (Décimal)", "Base 5", "Base 2 (Binaire)"]

def FENETRE():
    result_label = None  # Stocker le label du résultat localement

    def verification(n, base_1, base_2):
        # Vérifications d'erreurs selon la base
        if base_1 == 4 and any(char in "ABCDEF23456789" for char in n):
            return "Revérifier vos bases"
        elif base_1 == 3 and any(char in "ABCDEF56789" for char in n):
            return "Revérifier vos bases"
        elif base_1 == 2 and any(char in "ABCDEF" for char in n):
            return "Revérifier vos bases"
        elif base_1 == 2 and any(char not in "0123456789" for char in n):  # Vérification pour base 10
            return "Revérifier vos bases"
        else:
            return conversion(n, base_1, base_2)  # Retourne le résultat de la conversion
            
    def conversion(n, base_1, base_2):
        # Conversion de la valeur n de base_1 à base_2
        if base_1 == 1:  # Hexadécimal (base 16)
            if base_2 == 1:  # Hexa -> Hexa
                return n
            elif base_2 == 2:  # Hexa -> Décimal
                return str(int(n, 16))  # Conversion correcte du hexadécimal en décimal
            elif base_2 == 3:  # Hexa -> Base 5
                n = int(n, 16)
                base_5 = ""
                while n > 0:
                    reste = n % 5
                    base_5 = str(reste) + base_5
                    n = n // 5
                return base_5 if base_5 else "0"
            elif base_2 == 4:  # Hexa -> Binaire
                n = int(n, 16)
                base_binaire = ""
                while n > 0:
                    reste = n % 2
                    base_binaire = str(reste) + base_binaire
                    n = n // 2
                return base_binaire if base_binaire else "0"

        elif base_1 == 2:  # Décimal (base 10)
            n = int(n)
            if base_2 == 1:  # Décimal -> Hexa
                base_hexa = ""
                while n > 0:
                    reste = n % 16
                    if reste >= 10:
                        reste = chr(55 + reste)  # Conversion pour les lettres A-F
                    base_hexa = str(reste) + base_hexa
                    n = n // 16
                return base_hexa if base_hexa else "0"
            elif base_2 == 2:  # Décimal -> Décimal
                return str(n)
            elif base_2 == 3:  # Décimal -> Base 5
                base_5 = ""
                while n > 0:
                    reste = n % 5
                    base_5 = str(reste) + base_5
                    n = n // 5
                return base_5 if base_5 else "0"
            elif base_2 == 4:  # Décimal -> Binaire
                base_binaire = ""
                while n > 0:
                    reste = n % 2
                    base_binaire = str(reste) + base_binaire
                    n = n // 2
                return base_binaire if base_binaire else "0"

        elif base_1 == 3:  # Base 5
            if base_2 == 1:  # Base 5 -> Hexa
                n = int(n, 5)
                base_hexa = ""
                while n > 0:
                    reste = n % 16
                    if reste >= 10:
                        reste = chr(55 + reste)
                    base_hexa = str(reste) + base_hexa
                    n = n // 16
                return base_hexa if base_hexa else "0"
            elif base_2 == 2:  # Base 5 -> Décimal
                return str(int(n, 5))
            elif base_2 == 3:  # Base 5 -> Base 5
                return n
            elif base_2 == 4:  # Base 5 -> Binaire
                n = int(n, 5)
                base_binaire = ""
                while n > 0:
                    reste = n % 2
                    base_binaire = str(reste) + base_binaire
                    n = n // 2
                return base_binaire if base_binaire else "0"

        elif base_1 == 4:  # Binaire (base 2)
            n = int(n, 2)
            if base_2 == 1:  # Binaire -> Hexa
                base_hexa = ""
                while n > 0:
                    reste = n % 16
                    if reste >= 10:
                        reste = chr(55 + reste)
                    base_hexa = str(reste) + base_hexa
                    n = n // 16
                return base_hexa if base_hexa else "0"
            elif base_2 == 2:  # Binaire -> Décimal
                return str(n)
            elif base_2 == 3:  # Binaire -> Base 5
                base_5 = ""
                while n > 0:
                    reste = n % 5
                    base_5 = str(reste) + base_5
                    n = n // 5
                return base_5 if base_5 else "0"
            elif base_2 == 4:  # Binaire -> Binaire
                return n

    def confirm_action():
        nonlocal result_label
        base_1 = options.index(var.get()) + 1
        base_2 = options.index(var1.get()) + 1
        n = entry.get()
        resultat = verification(n, base_1, base_2)

        if result_label:
            result_label.destroy()
        
        result_label = tk.Label(f1, text=f"{resultat} en {var1.get()}", font=title_font)
        result_label.grid(sticky="w", pady=10)

    f1 = tk.Tk()
    f1.title("Convertisseur")
    f1.geometry("960x1080")

    title = tk.Label(f1, text="Programme de convertisseur de base", font=title_font)
    title.grid(sticky="w", pady=10)

    label = tk.Label(f1, text="Choisissez votre base de départ")
    label.grid(sticky="w")
    var = tk.StringVar(value=options[1])
    menu_deroulant = tk.OptionMenu(f1, var, *options)
    menu_deroulant.grid(sticky="w", pady=10)

    entry = tk.Entry(f1, width=50)
    entry.grid(sticky="w", pady=10)

    label1 = tk.Label(f1, text="Choisissez votre base finale")
    label1.grid(sticky="w", pady=10)
    var1 = tk.StringVar(value=options[0])
    menu_deroulant2 = tk.OptionMenu(f1, var1, *options)
    menu_deroulant2.grid(sticky="w", pady=10)

    confirm_button = tk.Button(f1, text="Confirmer", command=confirm_action)
    confirm_button.grid(sticky="w", pady=10)

    close = tk.Button(f1, text="X", command=f1.destroy)
    close.place(relx=0.99, y=110, anchor="ne")
    
    f1.mainloop()

FENETRE()