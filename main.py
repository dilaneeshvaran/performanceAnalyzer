from utilitaires import lire_csv, sauvegarder_resultats
from algorithmes_tri import tri_selection
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
        
        resultats += f"\n{'=' * 30}\n"
        resultats += f"RÉSULTATS POUR {taille} ÉLÉMENTS\n"
        resultats += f"{'=' * 30}\n"
        
        for colonne in colonnes:
            resultats += f"\n=== TRI PAR {colonne.upper()} ({taille} éléments) ===\n"
            
            donnees_copie = copy.deepcopy(donnees)
            tableau_trie, nb_comparaisons, nb_echanges, temps = tri_selection(donnees_copie, colonne)
            resultats += f"Tri SÉLECTION par {colonne.upper()} : {temps:.3f}s | {nb_comparaisons} comparaisons | {nb_echanges} échanges\n"
    
    sauvegarder_resultats(chemin_resultats, resultats)
    print(f"Les résultats ont été sauvegardés dans {chemin_resultats}")

if __name__ == "__main__":
    main()