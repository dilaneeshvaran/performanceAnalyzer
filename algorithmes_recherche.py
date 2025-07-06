import time

def recherche_lineaire(tableau, critere_fn):
    debut = time.time()
    occurrences = []
    nb_comparaisons = 0
    
    for element in tableau:
        nb_comparaisons += 1
        if critere_fn(element):
            occurrences.append(element)
    
    fin = time.time()
    temps_execution = fin - debut
    
    return occurrences, nb_comparaisons, temps_execution

# test A
def recherche_maisons_paris(tableau):
    def critere_maison_paris(element):
        return element["type_local"] == "Maison" and element["commune"] == "PARIS"
    
    return recherche_lineaire(tableau, critere_maison_paris)

# test D
def recherche_appartements_3pieces(tableau):
    def critere_appart_3p(element):
        try:
            nb_pieces = int(element["nb_pieces"]) if isinstance(element["nb_pieces"], str) else element["nb_pieces"]
            return element["type_local"] == "Appartement" and nb_pieces == 3
        except (ValueError, TypeError):
            return False
    
    return recherche_lineaire(tableau, critere_appart_3p)

def recherche_binaire(tableau, valeur_cible, cle):
    debut = time.time()
    nb_comparaisons = 0
    gauche = 0
    droite = len(tableau) - 1
    position_trouvee = -1
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        nb_comparaisons += 1
        
        if tableau[milieu][cle] == valeur_cible:
            position_trouvee = milieu
            break
        elif tableau[milieu][cle] < valeur_cible:
            nb_comparaisons += 1
            gauche = milieu + 1
        else:
            nb_comparaisons += 1
            droite = milieu - 1
    
    fin = time.time()
    temps_execution = fin - debut
    
    return position_trouvee, nb_comparaisons, temps_execution

# test B
def recherche_binaire_prix_350000(tableau_trie_prix):
    return recherche_binaire(tableau_trie_prix, 350000.0, "prix")


def recherche_min_max(tableau, cle):
    debut = time.time()
    nb_comparaisons = 0
    
    if len(tableau) == 0:
        fin = time.time()
        temps_execution = fin - debut
        return None, None, nb_comparaisons, temps_execution
    
    # min and max with first element
    valeur_min = tableau[0][cle]
    valeur_max = tableau[0][cle]
    
    # start iteration with 2nd array element
    for i in range(1, len(tableau)):
        valeur_courante = tableau[i][cle]
        
        # min comparaison
        nb_comparaisons += 1
        if valeur_courante < valeur_min:
            valeur_min = valeur_courante
        
        # max comparaison
        nb_comparaisons += 1
        if valeur_courante > valeur_max:
            valeur_max = valeur_courante
    
    fin = time.time()
    temps_execution = fin - debut
    
    return valeur_min, valeur_max, nb_comparaisons, temps_execution

# test C
def recherche_min_max_prix_m2(tableau):
    return recherche_min_max(tableau, "prix_m2")