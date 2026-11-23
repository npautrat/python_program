import tkinter as tk

# AFFICHAGE

# PREMIERE FENETRE 
def PREMIERE_FENETRE():
    # Création de la fenêtre principale
    f1 = tk.Tk()
    f1.title("Temps ?")
    f10 = tk.Label(f1, text="Choisissez votre temps en appuyant sur le bouton")
    f10.pack(pady=10)
    Temps=0

    def clicked_I():
        print("Vous avez choisis l'imparfait")
        global Temps
        Temps=1
        f1.destroy()
        
    def clicked_P():
        print("Vous avez choisis le présent")
        global Temps
        Temps=2
        f1.destroy()
        
    def clicked_F():
        print("Vous avez choisis le futur")
        global Temps
        Temps=3
        f1.destroy()
        
    def clicked_PS():
        print("Vous avez choisis le passé simple")
        global Temps
        Temps=4
        f1.destroy()
        
    def clicked_PC():
        print("Vous avez choisis le passé composé")
        global Temps
        Temps=5
        f1.destroy()
        
    def clicked_CP():
        print("Vous avez choisis le conditionnel présent")
        global Temps
        Temps=6
        f1.destroy()

    def clicked_PA():
        print("Vous avez choisis le passé antérieur")
        global Temps
        Temps=7
        f1.destroy()

    def clicked_FA():
        print("Vous avez choisis le futur antérieur")
        global Temps
        Temps=8
        f1.destroy()

    def clicked_PQP():
        print("Vous avez choisis le plus que parfait")
        global Temps
        Temps=9
        f1.destroy()

    def clicked_CP1():
        print("Vous avez choisis le passé conditionnel passé")
        global Temps
        Temps=10
        f1.destroy()
        
    # Création des boutons avec la couleur de fond, face et police
    b_I = tk.Button(f1, text="Imparfait", command=clicked_I, width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8))
    b_P = tk.Button(f1, text="Présent", command=clicked_P, width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8))
    b_F = tk.Button(f1, text="Futur", command=clicked_F, width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8))
    b_PS = tk.Button(f1, text="Passé Simple", command=clicked_PS, width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8))
    b_PC = tk.Button(f1, text="Passé Composé", command=clicked_PC, width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8))
    b_CP = tk.Button(f1, text="Conditonel Présent", command=clicked_CP, width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8))
    b_PA = tk.Button(f1, text="Passé Antérieur", command=clicked_PA, width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8))
    b_FA = tk.Button(f1, text="Futur Antérieur", command=clicked_FA, width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8))
    b_PQP = tk.Button(f1, text="Plus Que Parfait", command=clicked_PQP, width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8))
    b_CP1 = tk.Button(f1, text="Conditionnel Passé", command=clicked_CP1, width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8))

    # Affichage de la marge entre chaque bouton
    b_I.pack(pady=10)
    b_P.pack(pady=10)
    b_F.pack(pady=10)
    b_PS.pack(pady=10)
    b_PC.pack(pady=10)
    b_CP.pack(pady=10)
    b_PA.pack(pady=10)
    b_FA.pack(pady=10)
    b_PQP.pack(pady=10)
    b_CP1.pack(pady=10)    
    # Lancement pour afficher la fenêtre
    f1.mainloop()

# DEUXIEME FENETRE 

# Fonction pour afficher le verbe

def DEUXIEME_FENETRE():
    
    # Création de la nouvelle fenêtre
    f2 = tk.Tk()
    f2.title("Verbe")

    # Label pour indiquer à l'utilisateur d'entrer un verbe
    f20 = tk.Label(f2, text="Inscribez votre verbe:")
    f20.pack(pady=10)

    # Endroit pour mettre le verbe
    entry = tk.Entry(f2, width=30)
    entry.pack(pady=10)

    # Fonction pour recuperer le verbe

    def save_verbe(entry):
        global verbe
        verbe = entry.get()
        print(f"Verbe sauvegardé: {verbe}")
        

    # Fonction pour gérer la confirmation et la destruction de la fenêtre
    def confirm_action():
        save_verbe(entry)
        f2.destroy()

    confirm_button = tk.Button(f2, text="Confirmer le verbe", command=confirm_action)
    confirm_button.pack(pady=10)

    f2.mainloop()  # Lancer la boucle d'événements pour f2

# TROISIEME FENETRE 

#Tout s'ouvre en fonction de sa
def TROISIEME_FENETRE():
    f3 = tk.Tk()
    f3.title("Personne ?")
    f30 = tk.Label(f3, text="Choisissez votre personne en appuyant sur le bouton")
    f30.pack(pady=10)

    # Fonctions pour chaque personne
    Personne = 0
    def clicked_PPS_1():
        print("Vous avez choisi la première personne du singulier")
        global Personne
        Personne = 1
        f3.destroy()
        
    def clicked_DPS_1():
        print("Vous avez choisi la deuxième personne du singulier")
        global Personne
        Personne = 2
        f3.destroy()
        
    def clicked_TPS_1():
        print("Vous avez choisi la troisième personne du singulier")
        global Personne
        Personne = 3
        f3.destroy()
        
    def clicked_PPP_1():
        print("Vous avez choisi la première personne du pluriel")
        global Personne
        Personne = 4
        f3.destroy()
        
    def clicked_DPP_1():
        print("Vous avez choisi la deuxième personne du pluriel")
        global Personne
        Personne = 5
        f3.destroy()
        
    def clicked_TPP_1():
        print("Vous avez choisi la troisième personne du pluriel")
        global Personne
        Personne = 6
        f3.destroy()
        
    # Création des boutons avec la couleur de fond, face et police
    b_PPS = tk.Button(f3, text="Première personne du singulier", width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8), command=clicked_PPS_1)
    b_DPS = tk.Button(f3, text="Deuxième personne du singulier", width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8), command=clicked_DPS_1)
    b_TPS = tk.Button(f3, text="Troisième personne du singulier", width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8), command=clicked_TPS_1)
    b_PPP = tk.Button(f3, text="Première personne du pluriel", width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8), command=clicked_PPP_1)
    b_DPP = tk.Button(f3, text="Deuxième personne du pluriel", width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8), command=clicked_DPP_1)
    b_TPP = tk.Button(f3, text="Troisième personne du pluriel", width=30, height=3, bg="blue", fg="white", font=("Helvetica", 8), command=clicked_TPP_1)

    # Affichage des boutons
    b_PPS.pack(pady=10)
    b_DPS.pack(pady=10)
    b_TPS.pack(pady=10)
    b_PPP.pack(pady=10)
    b_DPP.pack(pady=10)
    b_TPP.pack(pady=10)

    # Lancement pour afficher la fenêtre
    f3.mainloop() 


   
def trouver_le_groupe(verbe):
    global groupe
    verbes_2e_groupe = ["finir", "choisir", "grandir", "réussir", "rougir", "applaudir", "grossir"]
    
    if verbe.endswith("er") and verbe != "aller":
        groupe = 1
        print('1er groupe')
    elif verbe.endswith("ir") and verbe in verbes_2e_groupe:
        groupe = 2
        print('2e groupe')
    else:
        groupe = 3
        print('3e groupe')
    
    return groupe
 
TPSI1G = ['e', 'es', 'e', 'ons', 'ez', 'ent']
def present_indicatif(verbe):
    global Personne
    global groupe
    if groupe == 1:
        if verbe[-3] == 'g':
            racine = verbe[:-2]
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine}{TPSI1G[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine}{TPSI1G[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine}{TPSI1G[2]}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine}{'e'}{TPSI1G[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine}{TPSI1G[4]}" ]
                return conjugaison
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine}{TPSI1G[5]}" ]
                return conjugaison  
        if verbe[-3] == 'y' and verbe[-4] == 'u' or 'o':
            racine = verbe[:-2]
            racine_uyer_oyer = verbe[:-3]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_uyer_oyer}{'i'}{TPSI1G[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_uyer_oyer}{'i'}{TPSI1G[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_uyer_oyer}{'i'}{TPSI1G[2]}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine}{TPSI1G[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine}{TPSI1G[4]}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_uyer_oyer}{'i'}{TPSI1G[5]}" ]
                return conjugaison
        if verbe[-3] == 'c':
            racine = verbe[:-2]
            racine_cer = verbe[:-3]
            #Personne = 4
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine}{TPSI1G[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine}{TPSI1G[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine}{TPSI1G[2]}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_cer}{'ç'}{TPSI1G[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine}{TPSI1G[4]}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine}{TPSI1G[5]}" ]
                return conjugaison  
        if verbe[-3] == 't' and verbe[-4] == 'e' and verbe[-5] == 'j':
            racine = verbe[:-2]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine}{'t'}{TPSI1G[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine}{'t'}{TPSI1G[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine}{'t'}{TPSI1G[2]}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine}{TPSI1G[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine}{TPSI1G[4]}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine}{'t'}{TPSI1G[5]}" ]
                return conjugaison  
        doublement_consonne_L = ['agneler', 'celer', 'déceler', 'receler', 'ciseler', 'démanteler', 'écarteler', 'geler', 'dégeler', 'congeler', 'surgeler', 'marteler', 'modeler', 'peler']
        if verbe in doublement_consonne_L:
            racine = verbe[:-2]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine}{'l'}{TPSI1G[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine}{'l'}{TPSI1G[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine}{'l'}{TPSI1G[2]}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine}{TPSI1G[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine}{TPSI1G[4]}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine}{'l'}{TPSI1G[5]}" ]
                return conjugaison 
        else:   
            racine = verbe[:-2]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine}{TPSI1G[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine}{TPSI1G[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine}{TPSI1G[2]}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine}{TPSI1G[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine}{TPSI1G[4]}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine}{TPSI1G[5]}" ]
                return conjugaison


    TPSI2G = ['is', 'is', 'it', 'issons', 'issez', 'issent']
    if groupe == 2:
        racine = verbe[:-2]
        if Personne == 1 :
            conjugaison =[f"{'Je'} {racine}{TPSI2G[0]}" ]
            return conjugaison            
        elif Personne == 2 :
            conjugaison =[f"{'Tu'} {racine}{TPSI2G[1]}" ]
            return conjugaison    
        elif Personne == 3 :
            conjugaison =[f"{'Il/Elle/On'} {racine}{TPSI2G[2]}" ]
            return conjugaison 
        elif Personne == 4 :
            conjugaison =[f"{'Nous'} {racine}{TPSI2G[3]}" ]
            return conjugaison
        elif Personne == 5 :
            conjugaison =[f"{'Vous'} {racine}{TPSI2G[4]}" ]
            return conjugaison 
        elif Personne == 6 :
            conjugaison =[f"{'Ils/Elles'} {racine}{TPSI2G[5]}" ]
            return conjugaison
    TPSI3G_DRE = ['s', 's', 't', 'ons', 'ez', 'ent']
    if groupe == 3:
        if verbe[-1] == 'e' and verbe[-2] == 'r' and verbe[-3] == 'd' and verbe[-4] == 'n' and verbe[-5] == 'e' and verbe[-6] == 'r' and verbe[-7] == 'p':                       
            racine = verbe[:-2]        
            racine_prendre = verbe[:-3]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_prendre}{'ds'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_prendre}{'ds'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_prendre}{'d'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_prendre}{'ons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_prendre}{'ez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_prendre}{'nent'}" ]
                return conjugaison
        if verbe[-1] == 'e' and verbe[-2] == 'r' and verbe[-3] == 't' and verbe[-4] == 'e':
            racine_etre = verbe[:-4]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_etre}{'suis'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_etre}{'es'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_etre}{'est'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_etre}{'sommes'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_etre}{'etes'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_etre}{'sont'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'o' and verbe[-4] == 'v' and verbe[-5] == 'a'  :                     
            racine = verbe[:-2]        
            racine_avoir = verbe[:-5]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_avoir}{'ai'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_avoir}{'as'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_avoir}{'a'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_avoir}{'avons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_avoir}{'avez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_avoir}{'ont'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'e' and verbe[-3] == 'l' and verbe[-4] == 'l' and verbe[-5] == 'a'  :                     
            racine = verbe[:-2]        
            racine_aller = verbe[:-3]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_aller}{'vais'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_aller}{'vas'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_aller}{'va'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_aller}{'allons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_aller}{'allez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_aller}{'vont'}" ]
                return conjugaison
        if verbe[-1] == 'e' and verbe[-2] == 'r' and verbe[-3] == 'i' and verbe[-4] == 'a' and verbe[-5] == 'f':                       
            racine = verbe[:-2]        
            racine_faire = verbe[:-5]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_faire}{'fais'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_faire}{'fais'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_faire}{'fait'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_faire}{'faisons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_faire}{'faites'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_faire}{'font'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'o' and verbe[-4] == 'v' and verbe[-5] == 'u' and verbe[-6] == 'o' and verbe[-7] == 'p':                       
            racine = verbe[:-2]        
            racine_pouvoir = verbe[:-7]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_pouvoir}{'peux'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_pouvoir}{'peux'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_pouvoir}{'peut'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_pouvoir}{'pouvons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_pouvoir}{'pouvez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_pouvoir}{'peuvent'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'o' and verbe[-4] == 'l' and verbe[-5] == 'u' and verbe[-6] == 'o' and verbe[-7] == 'v':                       
            racine = verbe[:-2]        
            racine_vouloir = verbe[:-7]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_vouloir}{'veux'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_vouloir}{'veux'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_vouloir}{'veut'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_vouloir}{'voulons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_vouloir}{'voulez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_vouloir}{'veulent'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'o' and verbe[-4] == 'v' and verbe[-5] == 'a' and verbe[-6] == 's':                       
            racine = verbe[:-2]        
            racine_savoir = verbe[:-6]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_savoir}{'sais'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_savoir}{'sais'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_savoir}{'sait'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_savoir}{'savons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_savoir}{'savez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_savoir}{'savent'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'o' and verbe[-4] == 'v' :                     
            racine = verbe[:-2]        
            racine_voir = vervenir
            #ersonne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_voir}{'vois'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_voir}{'vois'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_voir}{'voit'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_voir}{'voyons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_voir}{'voyez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_voir}{'voient'}" ]
                return conjugaison
        if verbe.endswith("venir"):                       
            racine = verbe[:-2]        
            racine_venir = verbe[:-5]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_venir}{'viens'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_venir}{'viens'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_venir}{'vient'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_venir}{'venons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_venir}{'venez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_venir}{'viennent'}" ]
                return conjugaison
        if verbe[-1] == 'e' and verbe[-2] == 'r' and verbe[-3] == 't' and verbe[-4] == 't' and verbe[-5] == 'e' and verbe[-6] =='m':                   
            racine = verbe[:-2]        
            racine_mettre = verbe[:-6]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_mettre}{'mets'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_mettre}{'mets'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_mettre}{'met'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_mettre}{'mettons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_mettre}{'mettez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_mettre}{'mettent'}" ]
                return conjugaison
        if verbe[-1] == 'e' and verbe[-2] == 'r' and verbe[-3] == 'i' and verbe[-4] == 'd':                   
            racine = verbe[:-2]        
            racine_dire = verbe[:-4]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_dire}{'dis'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_dire}{'dis'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_dire}{'dit'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_dire}{'disons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_dire}{'dites'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_dire}{'disent'}" ]
                return conjugaison
        if verbe[-1] == 'e' and verbe[-2] == 'r' and verbe[-3] == 'i' and verbe[-4] == 'l'  :                  
            racine = verbe[:-2]        
            racine_lire = verbe[:-4]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_lire}{'lis'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_lire}{'lis'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_lire}{'lit'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_lire}{'lisons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_lire}{'lisez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_lire}{'lisent'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'n' and verbe[-4] == 'e' and verbe[-5] == 't' :                  
            racine = verbe[:-2]        
            racine_tenir = verbe[:-5]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_tenir}{'tiens'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_tenir}{'tiens'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_tenir}{'tient'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_tenir}{'tenons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_tenir}{'tenez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_tenir}{'tiennent'}" ]
                return conjugaison
    
        TPSI3G_DRE = ['s', 's', ' ', 'ons', 'ez', 'ent']    
        if verbe[-3] == 'd' and verbe[-2] == 'r' and verbe[-1] == 'e':        
            racine_dre = verbe[:-3]        
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine}{TPSI3G_DRE[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine}{TPSI3G_DRE[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine}{TPSI3G_DRE[2]}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine}{TPSI3G_DRE[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine}{TPSI3G_DRE[4]}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine}{TPSI3G_DRE[5]}" ]
                return conjugaison  
        TPSI3G_IR = ['s', 's', 't', 'ons', 'ez', 'ent']    
        if verbe[-1] == 'r' and verbe[-2] == 'i':      
            racine_ir = verbe[:-3]        
            #ersonne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_ir}{TPSI3G_IR[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_ir}{TPSI3G_IR[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_ir}{TPSI3G_IR[2]}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine}{TPSI3G_IR[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine}{TPSI3G_IR[4]}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_ir}{TPSI3G_IR[5]}" ]
                return conjugaison 
        TPSI3G_OIR = ['x', 'x', 't', 'ons', 'ez', 'ent']    
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'o':              
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine}{TPSI3G_OIR[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine}{TPSI3G_OIR[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine}{TPSI3G_OIR[2]}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine}{TPSI3G_OIR[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine}{TPSI3G_OIR[4]}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine}{TPSI3G_OIR[5]}" ]
                return conjugaison
        TPSI3G_TRE = ['s', 's', 't', 'ssons', 'ssez', 'ssent']    
        if verbe[-1] == 'e' and verbe[-2] == 'r' and verbe[-3] == 't':              
            racine_TRE = verbe[:-3]
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_TRE}{TPSI3G_TRE[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_TRE}{TPSI3G_TRE[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_TRE}{TPSI3G_TRE[2]}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_TRE}{TPSI3G_TRE[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_TRE}{TPSI3G_TRE[4]}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_TRE}{TPSI3G_TRE[5]}" ]
                return conjugaison
TFSI1G = ['ai', 'as', 'a', 'ons', 'ez', 'ont']   
def futur_indicatif(verbe):
    #groupe=1
    if groupe == 1:
        if verbe == 'envoyer' :
            #Personne = 4
            if Personne == 1 :
                return 'je enverrai'   
            elif Personne == 2 :
                return 'tu enverras' 
            elif Personne == 3 :
                return 'il/elle/on enverra'
            elif Personne == 4 :
                return 'nous enverrons'
            elif Personne == 5 :
                return 'vous enverrez'
            elif Personne == 6 :
                return 'ils/elles enverront'
        else:           
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {verbe}{TFSI1G[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {verbe}{TFSI1G[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {verbe}{TFSI1G[2]}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {verbe}{TFSI1G[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {verbe}{TFSI1G[4]}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {verbe}{TFSI1G[5]}" ]
                return conjugaison
    TFSI2G = ['ai', 'as', 'a', 'ons', 'ez', 'ont']   
    if groupe == 2:
        #Personne = 2
        if Personne == 1 :
            conjugaison =[f"{'Je'} {verbe}{TFSI2G[0]}" ]
            return conjugaison            
        elif Personne == 2 :
            conjugaison =[f"{'Tu'} {verbe}{TFSI2G[1]}" ]
            return conjugaison    
        elif Personne == 3 :
            conjugaison =[f"{'Il/Elle/On'} {verbe}{TFSI2G[2]}" ]
            return conjugaison 
        elif Personne == 4 :
            conjugaison =[f"{'Nous'} {verbe}{TFSI2G[3]}" ]
            return conjugaison
        elif Personne == 5 :
            conjugaison =[f"{'Vous'} {verbe}{TFSI2G[4]}" ]
            return conjugaison 
        elif Personne == 6 :
            conjugaison =[f"{'Ils/Elles'} {verbe}{TFSI2G[5]}" ]
            return conjugaison
    TFSI3G = ['ai', 'as', 'a', 'ons', 'ez', 'ont']
    if groupe == 3:
        if verbe[-1] == 'e' and verbe[-2] == 'r' and verbe[-3] == 't' and verbe[-4] == 'e':
            racine_etre_future = verbe[:-4]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_etre_future}{'serai'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_etre_future}{'seras'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_etre_future}{'sera'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_etre_future}{'serons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_etre_future}{'serez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_etre_future}{'seront'}" ]
                return conjugaison
        if verbe[-1] == 'e' and verbe[-2] == 'r' and verbe[-3] == 'i' and verbe[-4] == 'a' and verbe[-5] == 'f':
            racine_faire_future = verbe[:-5]
            #Personne = 5
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_faire_future}{'ferai'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_faire_future}{'feras'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_faire_future}{'fera'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_faire_future}{'ferons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_faire_future}{'ferez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_faire_future}{'feront'}" ]
                return conjugaison
        if verbe=="avoir":
            racine_avoir_future = verbe[:-5]
            #ersonne = 1
            if Personne == 1 :
                conjugaison =[f"{"J'aurai"}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu auras'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On aura'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous aurons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous aurez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles auront'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'o' and verbe[-4] == 'l' and verbe[-5] == 'u' and verbe[-6] == 'o' and verbe[-7] == 'v':
            racine_vouloir_future = verbe[:-7]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_vouloir_future}{'voudrai'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_vouloir_future}{'voudras'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_vouloir_future}{'voudra'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_vouloir_future}{'voudrons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_vouloir_future}{'voudrez'}" ]
                return conjugaison 
            elif Personne == 6 : 
                conjugaison =[f"{'Ils/Elles'} {racine_vouloir_future}{'voudront'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'o' and verbe[-4] == 'v' and verbe[-5] == 'u' and verbe[-6] == 'o' and verbe[-7] == 'p':
            racine_pouvoir_future = verbe[:-7]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_pouvoir_future}{'pourrai'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_pouvoir_future}{'pourras'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_pouvoir_future}{'pourra'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_pouvoir_future}{'pourrons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_pouvoir_future}{'pourrez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_pouvoir_future}{'pourront'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'e' and verbe[-3] == 'l' and verbe[-4] == 'l' and verbe[-5] == 'a' :
            racine_aller_future = verbe[:-5]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_aller_future}{'irai'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_aller_future}{'iras'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_aller_future}{'ira'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_aller_future}{'irons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_aller_future}{'irez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_aller_future}{'iront'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'n' and verbe[-4] == 'e' and verbe[-5] == 'v' :
            racine_venir_future = verbe[:-5]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_venir_future}{'viendrai'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_venir_future}{'viendras'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_venir_future}{'viendra'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_venir_future}{'viendrons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_venir_future}{'viendrez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_venir_future}{'viendront'}" ]
                return conjugaison
        if verbe[-1] == 'e' and verbe[-2] == 'r' and verbe[-3] == 'd' and verbe[-4] == 'n' and verbe[-5] == 'e' and verbe[-6] == 'r' and verbe[-7] == 'p' :
            racine_prendre_future = verbe[:-7]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_prendre_future}{'prendrai'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_prendre_future}{'prendras'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_prendre_future}{'prendra'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_prendre_future}{'prendrons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_prendre_future}{'prendrez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_prendre_future}{'prendront'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'o' and verbe[-4] == 'v' and verbe[-5] == 'a' and verbe[-6] == 's' :
            racine_savoir_future = verbe[:-6]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_savoir_future}{'saurai'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_savoir_future}{'sauras'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_savoir_future}{'saura'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_savoir_future}{'saurons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_savoir_future}{'saurez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_savoir_future}{'sauront'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'n' and verbe[-4] == 'e' and verbe[-5] == 't' :
            racine_tenir_future = verbe[:-5]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_tenir_future}{'tiendrai'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_tenir_future}{'tiendras'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_tenir_future}{'tiendra'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_tenir_future}{'tiendrons'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_tenir_future}{'tiendrez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_tenir_future}{'tiendront'}" ]
                return conjugaison
        else:           
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {verbe}{TFSI3G[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {verbe}{TFSI3G[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {verbe}{TFSI3G[2]}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {verbe}{TFSI3G[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {verbe}{TFSI3G[4]}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {verbe}{TFSI3G[5]}" ]
                return conjugaison

TISI1G = ['ais', 'ais', 'ait', 'ions', 'iez', 'aient']  
def imparfait_indicatif(verbe):
    if groupe == 1:
        if verbe[-3] == 'c':
            racine = verbe[:-2]
            racine_cer = verbe[:-3]
            #ersonne = 4
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_cer}{'ç'}{TISI1G[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_cer}{'ç'}{TISI1G[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_cer}{'ç'}{TISI1G[2]}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine}{TISI1G[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine}{TISI1G[4]}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_cer}{'ç'}{TISI1G[5]}" ]
                return conjugaison  
        if verbe[-3] == 'g':
            racine = verbe[:-2]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine}{'e'}{TISI1G[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine}{'e'}{TISI1G[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine}{'e'}{TISI1G[2]}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine}{TISI1G[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine}{TISI1G[4]}" ]
                return conjugaison
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine}{'e'}{TISI1G[5]}" ]
                return conjugaison 
        else:       
            racine = verbe[:-2]
            #Personne = 2
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine}{TISI1G[0]}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine}{TISI1G[1]}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine}{TISI1G[2]}" ]
                return conjugaison
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine}{TISI1G[3]}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine}{TISI1G[4]}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine}{TISI1G[5]}" ]
                return conjugaison
    TISI2G = ['issais', 'issais', 'issait', 'issions', 'issiez', 'issaient']            
    if groupe == 2:
        racine = verbe[:-2]
        #Personne = 2
        if Personne == 1 :
            conjugaison =[f"{'Je'} {racine}{TISI2G[0]}" ]
            return conjugaison            
        elif Personne == 2 :
            conjugaison =[f"{'Tu'} {racine}{TISI2G[1]}" ]
            return conjugaison    
        elif Personne == 3 :
            conjugaison =[f"{'Il/Elle/On'} {racine}{TISI2G[2]}" ]
            return conjugaison 
        elif Personne == 4 :
            conjugaison =[f"{'Nous'} {racine}{TISI2G[3]}" ]
            return conjugaison
        elif Personne == 5 :
            conjugaison =[f"{'Vous'} {racine}{TISI2G[4]}" ]
            return conjugaison 
        elif Personne == 6 :
            conjugaison =[f"{'Ils/Elles'} {racine}{TISI2G[5]}" ]
            return conjugaison
TCP1G = ['ais', 'ais', 'ait', 'ions', 'iez', 'aient']
def conditionnel_present(verbe):
    if groupe == 1 or groupe == 2:
        #Personne = 2
        if Personne == 1 :
            conjugaison =[f"{'Je'} {verbe}{TCP1G[0]}" ]
            return conjugaison            
        elif Personne == 2 :
            conjugaison =[f"{'Tu'} {verbe}{TCP1G[1]}" ]
            return conjugaison    
        elif Personne == 3 :
            conjugaison =[f"{'Il/Elle/On'} {verbe}{TCP1G[2]}" ]
            return conjugaison 
        elif Personne == 4 :
            conjugaison =[f"{'Nous'} {verbe}{TCP1G[3]}" ]
            return conjugaison
        elif Personne == 5 :
            conjugaison =[f"{'Vous'} {verbe}{TCP1G[4]}" ]
            return conjugaison
        elif Personne == 6 :
            conjugaison =[f"{'Ils/Elles'} {verbe}{TCP1G[5]}" ]
            return conjugaison
    if groupe == 3:
        if verbe[-1] == 'e' and verbe[-2] == 'r' and verbe[-3] == 't' and verbe[-4] == 'e':
            racine_etre_CP = verbe[:-4]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_etre_CP}{'serais'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_etre_CP}{'serais'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_etre_CP}{'serait'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_etre_CP}{'serions'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_etre_CP}{'seriez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_etre_CP}{'seraient'}" ]
                return conjugaison
        if verbe[-1] == 'e' and verbe[-2] == 'r' and verbe[-3] == 'i' and verbe[-4] == 'a' and verbe[-5] == 'f':
            racine_faire_CP = verbe[:-5]
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_faire_CP}{'ferais'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_faire_CP}{'ferais'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_faire_CP}{'ferait'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_faire_CP}{'ferions'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_faire_CP}{'feriez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_faire_CP}{'feraient'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'o' and verbe[-4] == 'v' and verbe[-5] == 'a':
            racine_avoir_CP = verbe[:-5]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_etre_CP}{'aurais'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_etre_CP}{'aurais'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_etre_CP}{'aurait'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_etre_CP}{'aurions'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_etre_CP}{'auriez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_etre_CP}{'auraient'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'o' and verbe[-4] == 'l' and verbe[-5] == 'u' and verbe[-6] == 'o' and verbe[-7] == 'v':
            racine_vouloir_CP = verbe[:-7]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_vouloir_CP}{'voudrais'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_vouloir_CP}{'voudrai'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_vouloir_CP}{'voudrais'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_vouloir_CP}{'voudrions'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_vouloir_CP}{'voudriez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_vouloir_CP}{'voudraient'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'o' and verbe[-4] == 'v' :
            racine_voir_CP = verbe[:-4]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_voir_CP}{'verrais'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_voir_CP}{'verrais'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_voir_CP}{'verrait'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_voir_CP}{'verrions'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_voir_CP}{'verriez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_voir_CP}{'verraient'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'o' and verbe[-4] == 'v' and verbe[-5] == 'u' and verbe[-6] == 'o' and verbe[-7] == 'p':
            racine_pouvoir_CP = verbe[:-7]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_pouvoir_CP}{'pourrais'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_pouvoir_CP}{'pourrais'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_pouvoir_CP}{'pourrait'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_pouvoir_CP}{'pourrions'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_pouvoir_CP}{'pourriez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_pouvoir_CP}{'pourraient'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'e' and verbe[-3] == 'l' and verbe[-4] == 'l' and verbe[-5] == 'a' :
            racine_aller_CP = verbe[:-5]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_aller_CP}{'irais'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_aller_CP}{'irais'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_aller_CP}{'irait'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_aller_CP}{'irions'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_aller_future}{'iriez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_aller_CP}{'iraient'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'n' and verbe[-4] == 'e' and verbe[-5] == 'v' :
            racine_venir_CP = verbe[:-5]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_venir_CP}{'viendrais'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_venir_CP}{'viendrais'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_venir_CP}{'viendrait'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_venir_CP}{'viendrions'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_venir_CP}{'viendriez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_venir_CP}{'vieCPnt'}" ]
                return conjugaison
        if verbe[-1] == 'e' and verbe[-2] == 'r' and verbe[-3] == 'd' and verbe[-4] == 'n' and verbe[-5] == 'e' and verbe[-6] == 'r' and verbe[-7] == 'p' :
            racine_prendre_CP = verbe[:-7]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_prendre_CP}{'prendrais'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_prendre_CP}{'prendrais'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_prendre_CP}{'prendrait'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_prendre_CP}{'prendrions'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_prendre_CP}{'prendriez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_prendre_CP}{'prendraient'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'o' and verbe[-4] == 'v' and verbe[-5] == 'a' and verbe[-6] == 's' :
            racine_savoir_CP = verbe[:-6]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_savoir_CP}{'saurais'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_savoir_CP}{'saurais'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_savoir_CP}{'saurait'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_savoir_CP}{'saurions'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_savoir_CP}{'sauriez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_savoir_CP}{'sCPnt'}" ]
                return conjugaison
        if verbe[-1] == 'r' and verbe[-2] == 'i' and verbe[-3] == 'n' and verbe[-4] == 'e' and verbe[-5] == 't' :
            racine_tenir_CP = verbe[:-5]
            #Personne = 1
            if Personne == 1 :
                conjugaison =[f"{'Je'} {racine_tenir_CP}{'tiendrais'}" ]
                return conjugaison            
            elif Personne == 2 :
                conjugaison =[f"{'Tu'} {racine_tenir_CP}{'tiendrais'}" ]
                return conjugaison    
            elif Personne == 3 :
                conjugaison =[f"{'Il/Elle/On'} {racine_tenir_CP}{'tiendrait'}" ]
                return conjugaison 
            elif Personne == 4 :
                conjugaison =[f"{'Nous'} {racine_tenir_CP}{'tiendrions'}" ]
                return conjugaison
            elif Personne == 5 :
                conjugaison =[f"{'Vous'} {racine_tenir_CP}{'tiendriez'}" ]
                return conjugaison 
            elif Personne == 6 :
                conjugaison =[f"{'Ils/Elles'} {racine_tenir_CP}{'tiendraient'}" ]

def conditionnel_passé(verbe: str, nombre="singulier") -> str:
    # Dictionnaire des auxiliaires à l'imparfait selon le sujet
    auxiliaires_avoir = ["aurais", "aurais", "aurait", "aurions", "auriez", "auraient"]
    
    auxiliaires_etre = ["serais" , "serais", "serait", "serions", "seriez", "seraient"]
    
    # Verbes qui utilisent "être" comme auxiliaire
    verbes_avec_etre = ["aller", "venir", "arriver", "partir", "monter", "descendre", "entrer",
                        "sortir", "tomber", "rester", "passer", "retourner", "naître", "mourir",
                        "devenir", "revenir", "rentrer"]
    
    # Participe passé des verbes irréguliers
    participes_irreguliers = {
        "être": "été", "avoir": "eu", "faire": "fait", "dire": "dit", "voir": "vu", "prendre": "pris",
        "mettre": "mis", "ouvrir": "ouvert", "vouloir": "voulu", "savoir": "su", "pouvoir": "pu",
        "devoir": "dû", "venir": "venu", "naître": "né", "mourir": "mort", "lire": "lu", "écrire": "écrit"
    }
    
    # Choisir l'auxiliaire en fonction du verbe
    if verbe in verbes_avec_etre:
        participe_passe = participes_irreguliers.get(verbe, verbe[:-2] + "é")
        # Accord pour l'auxiliaire être
        if nombre == "pluriel":
            participe_passe += "s"
        Personne = 1
        if Personne == 1: 
            return f"{'je'} {auxiliaires_etre[0]} {participe_passe}"
        if Personne == 2: 
            return f"{'tu'} {auxiliaires_etre[1]} {participe_passe}"
        if Personne == 3: 
            return f"{'il/elle/on'} {auxiliaires_etre[2]} {participe_passe}"
        if Personne == 4: 
            return f"{'nous'} {auxiliaires_etre[3]} {participe_passe}"
        if Personne == 5: 
            return f"{'vous'} {auxiliaires_etre[4]} {participe_passe}"
        if Personne == 6: 
            return f"{'ils/elles'} {auxiliaires_etre[5]} {participe_passe}"
    else:
        # Trouver le participe passé
        if verbe in participes_irreguliers:
            participe_passe = participes_irreguliers[verbe]
        elif verbe.endswith("er"):
            participe_passe = verbe[:-2] + "é"
        elif verbe.endswith("ir"):
            participe_passe = verbe[:-1] + "i"
        elif verbe.endswith("re"):
            participe_passe = verbe[:-2] + "u"
        else:
            return "Le verbe n'est pas pris en charge."
        Personne = 1
        if Personne == 1: 
            return f"{'je'} {auxiliaires_avoir[0]} {participe_passe}"
        if Personne == 2: 
            return f"{'tu'} {auxiliaires_avoir[1]} {participe_passe}"
        if Personne == 3: 
            return f"{'il/elle/on'} {auxiliaires_avoir[2]} {participe_passe}"
        if Personne == 4: 
            return f"{'nous'} {auxiliaires_avoir[3]} {participe_passe}"
        if Personne == 5: 
            return f"{'vous'} {auxiliaires_avoir[4]} {participe_passe}"
        if Personne == 6: 
            return f"{'ils/elles'} {auxiliaires_avoir[5]} {participe_passe}"

                
TP_SI1G = ['ai', 'as', 'a', 'âmes', 'âtes', 'èrent']

def passé_simple_indicatif(verbe):
    racine = ''

    if verbe[-3] == 'c':  
        racine = verbe[:-2]
        racine_cer = verbe[:-3]
        if Personne == 1:
            return f"Je {racine_cer}ç{TP_SI1G[0]}"
        elif Personne == 2:
            return f"Tu {racine_cer}ç{TP_SI1G[1]}"
        elif Personne == 3:
            return f"Il/Elle/On {racine_cer}ç{TP_SI1G[2]}"
        elif Personne == 4:
            return f"Nous {racine_cer}ç{TP_SI1G[3]}"
        elif Personne == 5:
            return f"Vous {racine_cer}ç{TP_SI1G[4]}"
        elif Personne == 6:
            return f"Ils/Elles {racine}{TP_SI1G[5]}"
    
    elif verbe[-3] == 'g': 
        racine = verbe[:-2]
        if Personne == 1:
            return f"Je {racine}e{TP_SI1G[0]}"
        elif Personne == 2:
            return f"Tu {racine}e{TP_SI1G[1]}"
        elif Personne == 3:
            return f"Il/Elle/On {racine}e{TP_SI1G[2]}"
        elif Personne == 4:
            return f"Nous {racine}{TP_SI1G[3]}"
        elif Personne == 5:
            return f"Vous {racine}{TP_SI1G[4]}"
        elif Personne == 6:
            return f"Ils/Elles {racine}{TP_SI1G[5]}"
    
    else:
        racine = verbe[:-2]
        if Personne == 1:
            return f"Je {racine}{TP_SI1G[0]}"
        elif Personne == 2:
            return f"Tu {racine}{TP_SI1G[1]}"
        elif Personne == 3:
            return f"Il/Elle/On {racine}{TP_SI1G[2]}"
        elif Personne == 4:
            return f"Nous {racine}{TP_SI1G[3]}"
        elif Personne == 5:
            return f"Vous {racine}{TP_SI1G[4]}"
        elif Personne == 6:
            return f"Ils/Elles {racine}{TP_SI1G[5]}"

    return 
    
    terminaisons_groupes = {
        2: ['is', 'is', 'it', 'îmes', 'îtes', 'irent'],
        3: {
            'etre': ['fus', 'fus', 'fut', 'fûmes', 'fûtes', 'furent'],
            'avoir': ['eus', 'eus', 'eut', 'eûmes', 'eûtes', 'eurent'],
            'aller': ['allai', 'allas', 'alla', 'allâmes', 'allâtes', 'allèrent'],
            'faire': ['fis', 'fis', 'fit', 'fîmes', 'fîtes', 'firent'],
            'prendre': ['pris', 'pris', 'prit', 'prîmes', 'prîtes', 'prirent'],
            'oir': ['ins', 'ins', 'int', 'înmes', 'întes', 'inrent'],
            'ire': ['is', 'is', 'it', 'îmes', 'îtes', 'irent'],
            'dre': ['is', 'is', 'it', 'îmes', 'îtes', 'irent'],
            'reste': ['us', 'us', 'ut', 'ûmes', 'ûtes', 'urent'],
        }
    }
    
    pronoms = ['Je', 'Tu', 'Il/Elle/On', 'Nous', 'Vous', 'Ils/Elles']
    
    if groupe == 2:
        racine = verbe[:-2]
        terminaison = terminaisons_groupes[2][Personne - 1]
        return f"{pronoms[Personne - 1]} {racine}{terminaison}"
    
    elif groupe == 3:
        if verbe.endswith("etre"):
            racine = verbe[:-4]
            terminaison = terminaisons_groupes[3]['etre'][Personne - 1]
        elif verbe.endswith("avoir"):
            racine = verbe[:-5]
            terminaison = terminaisons_groupes[3]['avoir'][Personne - 1]
        elif verbe.endswith("aller"):
            racine = verbe[:-5]
            terminaison = terminaisons_groupes[3]['aller'][Personne - 1]
        elif verbe.endswith("faire"):
            racine = verbe[:-5]
            terminaison = terminaisons_groupes[3]['faire'][Personne - 1]
        elif verbe.endswith("prendre"):
            racine = verbe[:-6]
            terminaison = terminaisons_groupes[3]['prendre'][Personne - 1]
        elif verbe.endswith("oir"):
            racine = verbe[:-3]
            terminaison = terminaisons_groupes[3]['oir'][Personne - 1]
        elif verbe.endswith("ire"):
            racine = verbe[:-3]
            terminaison = terminaisons_groupes[3]['ire'][Personne - 1]
        elif verbe.endswith("dre"):
            racine = verbe[:-3]
            terminaison = terminaisons_groupes[3]['dre'][Personne - 1]
        else:
            racine = verbe[:-2]
            terminaison = terminaisons_groupes[3]['reste'][Personne - 1]
        
        return f"{pronoms[Personne - 1]} {racine}{terminaison}"
    
    else:
        return

def passé_composé_indicatif(verbe: str, nombre="singulier") -> str:
    # Dictionnaire des auxiliaires à l'imparfait selon le sujet
    auxiliaires_avoir = ["ai", "as", "a", "avons", "avez", "ont"]
    
    auxiliaires_etre = ["suis" , "es", "est", "sommes", "êtes", "sont"]
    
    # Verbes qui utilisent "être" comme auxiliaire
    verbes_avec_etre = ["aller", "venir", "arriver", "partir", "monter", "descendre", "entrer",
                        "sortir", "tomber", "rester", "passer", "retourner", "naître", "mourir",
                        "devenir", "revenir", "rentrer"]
    
    # Participe passé des verbes irréguliers
    participes_irreguliers = {
        "être": "été", "avoir": "eu", "faire": "fait", "dire": "dit", "voir": "vu", "prendre": "pris",
        "mettre": "mis", "ouvrir": "ouvert", "vouloir": "voulu", "savoir": "su", "pouvoir": "pu",
        "devoir": "dû", "venir": "venu", "naître": "né", "mourir": "mort", "lire": "lu", "écrire": "écrit"
    }
    
    # Choisir l'auxiliaire en fonction du verbe
    if verbe in verbes_avec_etre:
        participe_passe = participes_irreguliers.get(verbe, verbe[:-2] + "é")
        # Accord pour l'auxiliaire être
        if nombre == "pluriel":
            participe_passe += "s"
        #Personne = 1
        if Personne == 1: 
            return f"{'je'} {auxiliaires_etre[0]} {participe_passe}"
        if Personne == 2: 
            return f"{'tu'} {auxiliaires_etre[1]} {participe_passe}"
        if Personne == 3: 
            return f"{'il/elle/on'} {auxiliaires_etre[2]} {participe_passe}"
        if Personne == 4: 
            return f"{'nous'} {auxiliaires_etre[3]} {participe_passe}"
        if Personne == 5: 
            return f"{'vous'} {auxiliaires_etre[4]} {participe_passe}"
        if Personne == 6: 
            return f"{'ils/elles'} {auxiliaires_etre[5]} {participe_passe}"
    else:
        # Trouver le participe passé
        if verbe in participes_irreguliers:
            participe_passe = participes_irreguliers[verbe]
        elif verbe.endswith("er"):
            participe_passe = verbe[:-2] + "é"
        elif verbe.endswith("ir"):
            participe_passe = verbe[:-1] + "i"
        elif verbe.endswith("dre"):
            participe_passe = verbe[:-3] + "s"
        elif verbe.endswitch("re"):
            participe_passe = verbe[:-2] + "u"
        else:
            return "Le verbe n'est pas pris en charge."
        #Personne = 1
        if Personne == 1: 
            return f"{"j'"}{auxiliaires_avoir[0]} {participe_passe}"
        if Personne == 2: 
            return f"{'tu'} {auxiliaires_avoir[1]} {participe_passe}"
        if Personne == 3: 
            return f"{'il/elle/on'} {auxiliaires_avoir[2]} {participe_passe}"
        if Personne == 4: 
            return f"{'nous'} {auxiliaires_avoir[3]} {participe_passe}"
        if Personne == 5: 
            return f"{'vous'} {auxiliaires_avoir[4]} {participe_passe}"
        if Personne == 6: 
            return f"{'ils/elles'} {auxiliaires_avoir[5]} {participe_passe}"

def passé_antérieur(verbe: str, nombre="singulier", personne=1) -> str:
    auxiliaires_avoir = ["eus", "eus", "eut", "eumes", "eutes", "eurent"]
    auxiliaires_etre = ["fus", "fus", "fut", "fûmes", "fûtes", "furent"]
    
    verbes_avec_etre = ["aller", "venir", "arriver", "partir", "monter", "descendre", "entrer",
                        "sortir", "tomber", "rester", "passer", "retourner", "naître", "mourir",
                        "devenir", "revenir", "rentrer"]
    
    # Participe passé des verbes irréguliers
    participes_irreguliers = {
        "être": "été", "avoir": "eu", "faire": "fait", "dire": "dit", "voir": "vu", "prendre": "pris",
        "mettre": "mis", "ouvrir": "ouvert", "vouloir": "voulu", "savoir": "su", "pouvoir": "pu",
        "devoir": "dû", "venir": "venu", "naître": "né", "mourir": "mort", "lire": "lu", "écrire": "écrit"
    }
    
    # Choisir l'auxiliaire en fonction du verbe
    if verbe in verbes_avec_etre:
        participe_passe = participes_irreguliers.get(verbe, verbe[:-2] + "é")
        # Accord pour l'auxiliaire être
        if nombre == "pluriel":
            participe_passe += "s"
        if personne == 1: 
            return f"{"j'"} {auxiliaires_etre[0]} {participe_passe}"
        elif personne == 2: 
            return f"{'tu'} {auxiliaires_etre[1]} {participe_passe}"
        elif personne == 3: 
            return f"{'il/elle/on'} {auxiliaires_etre[2]} {participe_passe}"
        elif personne == 4: 
            return f"{'nous'} {auxiliaires_etre[3]} {participe_passe}"
        elif personne == 5: 
            return f"{'vous'} {auxiliaires_etre[4]} {participe_passe}"
        elif personne == 6: 
            return f"{'ils/elles'} {auxiliaires_etre[5]} {participe_passe}"
    else:
        # Trouver le participe passé
        if verbe in participes_irreguliers:
            participe_passe = participes_irreguliers[verbe]
        elif verbe.endswith("er"):
            participe_passe = verbe[:-2] + "é"
        elif verbe.endswith("ir"):
            participe_passe = verbe[:-1] + "i"
        elif verbe.endswith("dre"):
            participe_passe = verbe[:-3] + "s"
        elif verbe.endswith("re"):
            participe_passe = verbe[:-2] + "u"
        else:
            return "Le verbe n'est pas pris en charge."
        
        # Accord pour l'auxiliaire avoir
        if nombre == "pluriel":
            participe_passe += "s"
        if personne == 1: 
            return f"{'je'} {auxiliaires_avoir[0]} {participe_passe}"
        elif personne == 2: 
            return f"{'tu'} {auxiliaires_avoir[1]} {participe_passe}"
        elif personne == 3: 
            return f"{'il/elle/on'} {auxiliaires_avoir[2]} {participe_passe}"
        elif personne == 4: 
            return f"{'nous'} {auxiliaires_avoir[3]} {participe_passe}"
        elif personne == 5: 
            return f"{'vous'} {auxiliaires_avoir[4]} {participe_passe}"
        elif personne == 6: 
            return f"{'ils/elles'} {auxiliaires_avoir[5]} {participe_passe}"

def futur_antérieur(verbe: str, nombre="singulier") -> str:
    # Dictionnaire des auxiliaires à l'imparfait selon le sujet
    auxiliaires_avoir = ["aurai", "auras", "aura", "aurons", "aurez", "aront"]
    
    auxiliaires_etre = ["serai" , "seras", "sera", "serons", "serez", "seront"]
    
    # Verbes qui utilisent "être" comme auxiliaire
    verbes_avec_etre = ["aller", "venir", "arriver", "partir", "monter", "descendre", "entrer",
                        "sortir", "tomber", "rester", "passer", "retourner", "naître", "mourir",
                        "devenir", "revenir", "rentrer"]
    
    # Participe passé des verbes irréguliers
    participes_irreguliers = {
        "être": "été", "avoir": "eu", "faire": "fait", "dire": "dit", "voir": "vu", "prendre": "pris",
        "mettre": "mis", "ouvrir": "ouvert", "vouloir": "voulu", "savoir": "su", "pouvoir": "pu",
        "devoir": "dû", "venir": "venu", "naître": "né", "mourir": "mort", "lire": "lu", "écrire": "écrit"
    }
    
    # Choisir l'auxiliaire en fonction du verbe
    if verbe in verbes_avec_etre:
        participe_passe = participes_irreguliers.get(verbe, verbe[:-2] + "é")
        # Accord pour l'auxiliaire être
        if nombre == "pluriel":
            participe_passe += "s"
        Personne = 1
        if Personne == 1: 
            return f"{"je"} {auxiliaires_etre[0]} {participe_passe}"
        if Personne == 2: 
            return f"{'tu'} {auxiliaires_etre[1]} {participe_passe}"
        if Personne == 3: 
            return f"{'il/elle/on'} {auxiliaires_etre[2]} {participe_passe}"
        if Personne == 4: 
            return f"{'nous'} {auxiliaires_etre[3]} {participe_passe}"
        if Personne == 5: 
            return f"{'vous'} {auxiliaires_etre[4]} {participe_passe}"
        if Personne == 6: 
            return f"{'ils/elles'} {auxiliaires_etre[5]} {participe_passe}"
    else:
        # Trouver le participe passé
        if verbe in participes_irreguliers:
            participe_passe = participes_irreguliers[verbe]
        elif verbe.endswith("er"):
            participe_passe = verbe[:-2] + "é"
        elif verbe.endswith("ir"):
            participe_passe = verbe[:-1] + "i"
        elif verbe.endswith("re"):
            participe_passe = verbe[:-2] + "u"
        elif verbe.endswith("dre"):
            participe_passe = verbe[:-3] + "s"
        else:
            return "Le verbe n'est pas pris en charge."
        #Personne = 1
        if Personne == 1: 
            return f"{"j'"} {auxiliaires_avoir[0]} {participe_passe}"
        if Personne == 2: 
            return f"{'tu'} {auxiliaires_avoir[1]} {participe_passe}"
        if Personne == 3: 
            return f"{'il/elle/on'} {auxiliaires_avoir[2]} {participe_passe}"
        if Personne == 4: 
            return f"{'nous'} {auxiliaires_avoir[3]} {participe_passe}"
        if Personne == 5: 
            return f"{'vous'} {auxiliaires_avoir[4]} {participe_passe}"
        if Personne == 6: 
            return f"{'ils/elles'} {auxiliaires_avoir[5]} {participe_passe}"

def plus_que_parfait(verbe: str, nombre="singulier") -> str:
    # Dictionnaire des auxiliaires à l'imparfait selon le sujet
    auxiliaires_avoir = ["avais", "avais", "avait", "avions", "aviez", "avaient"]
    
    auxiliaires_etre = ["étais" , "étais", "était", "étions", "étiez", "étaient"]
    
    # Verbes qui utilisent "être" comme auxiliaire
    verbes_avec_etre = ["aller", "venir", "arriver", "partir", "monter", "descendre", "entrer",
                        "sortir", "tomber", "rester", "passer", "retourner", "naître", "mourir",
                        "devenir", "revenir", "rentrer"]
    
    # Participe passé des verbes irréguliers
    participes_irreguliers = {
        "être": "été", "avoir": "eu", "faire": "fait", "dire": "dit", "voir": "vu", "prendre": "pris",
        "mettre": "mis", "ouvrir": "ouvert", "vouloir": "voulu", "savoir": "su", "pouvoir": "pu",
        "devoir": "dû", "venir": "venu", "naître": "né", "mourir": "mort", "lire": "lu", "écrire": "écrit"
    }
    
    # Choisir l'auxiliaire en fonction du verbe
    if verbe in verbes_avec_etre:
        participe_passe = participes_irreguliers.get(verbe, verbe[:-2] + "é")
        # Accord pour l'auxiliaire être
        if nombre == "pluriel":
            participe_passe += "s"
        #Personne = 1
        if Personne == 1: 
            return f"{"j'"} {auxiliaires_etre[0]} {participe_passe}"
        if Personne == 2: 
            return f"{'tu'} {auxiliaires_etre[1]} {participe_passe}"
        if Personne == 3: 
            return f"{'il/elle/on'} {auxiliaires_etre[2]} {participe_passe}"
        if Personne == 4: 
            return f"{'nous'} {auxiliaires_etre[3]} {participe_passe}"
        if Personne == 5: 
            return f"{'vous'} {auxiliaires_etre[4]} {participe_passe}"
        if Personne == 6: 
            return f"{'ils/elles'} {auxiliaires_etre[5]} {participe_passe}"
    else:
        # Trouver le participe passé
        if verbe in participes_irreguliers:
            participe_passe = participes_irreguliers[verbe]
        elif verbe.endswith("er"):
            participe_passe = verbe[:-2] + "é"
        elif verbe.endswith("ir"):
            participe_passe = verbe[:-1] + "i"
        elif verbe.endswith("re"):
            participe_passe = verbe[:-2] + "u"
        elif verbe.endswith("dre"):
            participe_passe = verbe[:-3] + "s"
        else:
            return "Le verbe n'est pas pris en charge."
        #Personne = 1
        if Personne == 1: 
            return f"{"j'"} {auxiliaires_avoir[0]} {participe_passe}"
        if Personne == 2: 
            return f"{'tu'} {auxiliaires_avoir[1]} {participe_passe}"
        if Personne == 3: 
            return f"{'il/elle/on'} {auxiliaires_avoir[2]} {participe_passe}"
        if Personne == 4: 
            return f"{'nous'} {auxiliaires_avoir[3]} {participe_passe}"
        if Personne == 5: 
            return f"{'vous'} {auxiliaires_avoir[4]} {participe_passe}"
        if Personne == 6: 
            return f"{'ils/elles'} {auxiliaires_avoir[5]} {participe_passe}"


PREMIERE_FENETRE()
DEUXIEME_FENETRE()
TROISIEME_FENETRE()
trouver_le_groupe(verbe)
print(groupe)
if Temps==1:
        resultat=imparfait_indicatif(verbe)
        print(resultat)
elif Temps==2:
        resultat=present_indicatif(verbe)
        print(resultat)
elif Temps==3:
        resultat=futur_indicatif(verbe)
        print(resultat)
elif Temps==4:
        resultat=passé_simple_indicatif(verbe)
        print(resultat)
elif Temps==5:
        resultat=passé_composé_indicatif(verbe, nombre="singulier")
        print(resultat)
elif Temps==6:
        resultat=conditionnel_present(verbe)
        print(resultat)
elif Temps==7:
        resultat=passé_antérieur(verbe, nombre="singulier")
        print(resultat)
elif Temps==8:
        resultat=futur_antérieur(verbe, nombre="singulier")
        print(resultat)
elif Temps==9:
        resultat=plus_que_parfait(verbe, nombre="singulier")
        print(resultat)
elif Temps==10:
        resultat=conditionnel_passé(verbe, nombre="singulier")     
        print(resultat)