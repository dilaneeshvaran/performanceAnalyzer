from utilitaires import lire_csv, sauvegarder_resultats
from algorithmes_tri import tri_selection, tri_insertion, tri_fusion, tri_rapide
from algorithmes_recherche import recherche_maisons_paris, recherche_appartements_3pieces, recherche_binaire_prix_350000
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
        
        # run search for sizes 500 and 1000
        if taille >= 500:
            search_header = f"\n=== RECHERCHES LINÉAIRES ({taille} éléments) ===\n"
            resultats += search_header
            print(search_header, end='')
            
            # test A: find all houses in paris
            donnees_copie = copy.deepcopy(donnees)
            occurrences, nb_comparaisons, temps = recherche_maisons_paris(donnees_copie)
            ligne_maisons = f"Recherche linéaire MAISONS PARIS : {temps:.4f}s | {nb_comparaisons} comparaisons | Trouvées: {len(occurrences)}\n"
            resultats += ligne_maisons
            print(ligne_maisons, end='')
            
            # test D: find all 3 room apartments
            donnees_copie = copy.deepcopy(donnees)
            occurrences, nb_comparaisons, temps = recherche_appartements_3pieces(donnees_copie)
            ligne_apparts = f"Recherche APPART 3P : {temps:.4f}s | {nb_comparaisons} comparaisons | Trouvés: {len(occurrences)}\n"
            resultats += ligne_apparts
            print(ligne_apparts, end='')
            
            # test B: binary search for exact price 350000 euros
            donnees_copie = copy.deepcopy(donnees)
            # sort by price first before binary search
            tableau_trie_prix, _, _ = tri_fusion(donnees_copie, 'prix')
            position, nb_comparaisons, temps = recherche_binaire_prix_350000(tableau_trie_prix)
            ligne_binaire = f"Recherche binaire PRIX 350000€ : {temps:.4f}s | {nb_comparaisons} comparaisons | Position: {position}\n"
            resultats += ligne_binaire
            print(ligne_binaire, end='')
    
    sauvegarder_resultats(chemin_resultats, resultats)
    print(f"Les résultats ont été sauvegardés dans {chemin_resultats}")

if __name__ == "__main__":
    main()