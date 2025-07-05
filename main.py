from utilitaires import lire_csv, sauvegarder_resultats
from algorithmes_tri import tri_selection, tri_insertion, tri_fusion, tri_rapide
import copy

def main():
    # file directory
    chemin_csv = 'transactions_immobilieres.csv'
    chemin_resultats = 'resultats.txt'
    
    # sizes to test
    tailles = [100, 500, 1000]
    
    # column to sort
    colonnes = ['prix', 'surface']
    
    # output file data
    resultats = ""
    
    for taille in tailles:
        donnees = lire_csv(chemin_csv, taille)
        
        section_header = f"\n{'=' * 30}\nRÉSULTATS POUR {taille} ÉLÉMENTS\n{'=' * 30}\n"
        resultats += section_header
        print(section_header, end='')
        
        for colonne in colonnes:
            colonne_header = f"\n=== TRI PAR {colonne.upper()} ({taille} éléments) ===\n"
            resultats += colonne_header
            print(colonne_header, end='')
            
            # test selection sort
            donnees_copie = copy.deepcopy(donnees)
            tableau_trie, nb_comparaisons, nb_echanges, temps = tri_selection(donnees_copie, colonne)
            ligne_selection = f"Tri SÉLECTION par {colonne.upper()} : {temps:.4f}s | {nb_comparaisons} comparaisons | {nb_echanges} échanges\n"
            resultats += ligne_selection
            print(ligne_selection, end='')
            
            # test insertion sort
            donnees_copie = copy.deepcopy(donnees)
            tableau_trie, nb_comparaisons, nb_decalages, temps = tri_insertion(donnees_copie, colonne)
            ligne_insertion = f"Tri INSERTION par {colonne.upper()} : {temps:.4f}s | {nb_comparaisons} comparaisons | {nb_decalages} décalages\n"
            resultats += ligne_insertion
            print(ligne_insertion, end='')
            
            # test merge sort
            donnees_copie = copy.deepcopy(donnees)
            tableau_trie, nb_comparaisons, temps = tri_fusion(donnees_copie, colonne)
            ligne_fusion = f"Tri FUSION par {colonne.upper()} : {temps:.4f}s | {nb_comparaisons} comparaisons\n"
            resultats += ligne_fusion
            print(ligne_fusion, end='')
            
            # test quick sort
            donnees_copie = copy.deepcopy(donnees)
            tableau_trie, nb_comparaisons, nb_echanges, temps = tri_rapide(donnees_copie, colonne)
            ligne_rapide = f"Tri RAPIDE par {colonne.upper()} : {temps:.4f}s | {nb_comparaisons} comparaisons | {nb_echanges} échanges\n"
            resultats += ligne_rapide
            print(ligne_rapide, end='')
    
    sauvegarder_resultats(chemin_resultats, resultats)
    print(f"Les résultats ont été sauvegardés dans {chemin_resultats}")

if __name__ == "__main__":
    main()