import time

def tri_selection(tableau, cle):
    debut = time.time()
    n = len(tableau)
    comparaisons = 0
    echanges = 0
    
    for i in range(n-1):
        # search min
        min_idx = i
        for j in range(i+1, n):
            comparaisons += 1
            if tableau[j][cle] < tableau[min_idx][cle]:
                min_idx = j
        
        # exchange with 1st element
        tableau[i], tableau[min_idx] = tableau[min_idx], tableau[i]
        echanges += 1
    
    fin = time.time()
    temps = fin - debut
    
    return tableau, comparaisons, echanges, temps