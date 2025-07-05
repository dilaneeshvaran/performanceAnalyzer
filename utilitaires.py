def lire_csv(chemin_fichier, taille=None):
    donnees = []
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        # read header
        en_tete = fichier.readline().strip().split(',')
        
        # read data
        compteur = 0
        for ligne in fichier:
            if taille is not None and compteur >= taille:
                break
                
            valeurs = ligne.strip().split(',')
            if len(valeurs) == len(en_tete):
                element = {}
                for i in range(len(en_tete)):
                    cle = en_tete[i]
                    valeur = valeurs[i]
                    
                    # type conversion for types and price and surface
                    if cle == 'prix' or cle == 'surface' or cle == 'prix_m2':
                        try:
                            element[cle] = float(valeur)
                        except ValueError:
                            element[cle] = 0.0
                    else:
                        element[cle] = valeur
                
                donnees.append(element)
                compteur += 1
    
    return donnees

def sauvegarder_resultats(chemin_fichier, resultats):
    with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
        fichier.write(resultats)