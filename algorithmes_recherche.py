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

# Tests
def recherche_maisons_paris(tableau):
    def critere_maison_paris(element):
        return element["type_local"] == "Maison" and element["commune"] == "PARIS"
    
    return recherche_lineaire(tableau, critere_maison_paris)

def recherche_appartements_3pieces(tableau):
    def critere_appart_3p(element):
        try:
            nb_pieces = int(element["nb_pieces"]) if isinstance(element["nb_pieces"], str) else element["nb_pieces"]
            return element["type_local"] == "Appartement" and nb_pieces == 3
        except (ValueError, TypeError):
            return False
    
    return recherche_lineaire(tableau, critere_appart_3p)