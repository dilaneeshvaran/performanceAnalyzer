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

def tri_insertion(tableau, cle):
    debut = time.time()
    n = len(tableau)
    comparaisons = 0
    decalages = 0
    
    for i in range(1, n):
        # element to insert
        element_courant = tableau[i]
        
        # find right position in sorted part
        j = i - 1
        while j >= 0:
            comparaisons += 1
            if tableau[j][cle] > element_courant[cle]:
                tableau[j + 1] = tableau[j]
                decalages += 1
                j -= 1
            else:
                break
        
        # insert at correct position
        tableau[j + 1] = element_courant
    
    fin = time.time()
    temps = fin - debut
    
    return tableau, comparaisons, decalages, temps

def tri_fusion(tableau, cle):
    debut = time.time()
    comparaisons = [0]  # list to maintain reference in recursive calls
    
    def fusionner(gauche, droite, cle, comparaisons):
        resultat = []
        i = j = 0
        
        while i < len(gauche) and j < len(droite):
            comparaisons[0] += 1
            if gauche[i][cle] <= droite[j][cle]:
                resultat.append(gauche[i])
                i += 1
            else:
                resultat.append(droite[j])
                j += 1
        
        # add remaining elements
        resultat.extend(gauche[i:])
        resultat.extend(droite[j:])
        
        return resultat
    
    def tri_fusion_recursif(tableau, cle, comparaisons):
        if len(tableau) <= 1:
            return tableau
        
        # divide
        milieu = len(tableau) // 2
        gauche = tri_fusion_recursif(tableau[:milieu], cle, comparaisons)
        droite = tri_fusion_recursif(tableau[milieu:], cle, comparaisons)
        
        # fusion
        return fusionner(gauche, droite, cle, comparaisons)
    
    tableau_trie = tri_fusion_recursif(tableau, cle, comparaisons)
    
    fin = time.time()
    temps = fin - debut
    
    return tableau_trie, comparaisons[0], temps