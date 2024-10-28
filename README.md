# ravi-illusion-array-sum
Algorithme Python pour calculer la somme des minimums de tous les sous-tableaux d'un tableau donné en utilisant une pile monotone pour une complexité en  𝑂 ( 𝑛 ) O(n). Retourne le résultat modulo  1 0 9 + 7 10  9  +7.

# Ravi's Illusion - Array Minimum Subarrays Sum

## Description
Ce projet implémente un algorithme efficace pour calculer la somme des valeurs minimales de tous les sous-tableaux possibles d'un tableau donné. La solution utilise une technique de pile monotone pour trouver les sous-tableaux de manière optimisée, permettant de résoudre le problème dans un temps linéaire \(O(n)\).

## Problème
Ravi veut connaître la "somme des illusions" d'un tableau, définie comme la somme des valeurs minimales de tous les sous-tableaux possibles de ce tableau. Puisque le résultat peut être très grand, il doit être renvoyé modulo \(10^9 + 7\).

### Exemple
**Entrée :**
N = 4 Array = [71, 55, 82, 55]


**Sortie :**
593


## Solution
L'approche utilisée dans ce projet repose sur des piles monotones pour trouver, pour chaque élément, la portée maximale de sous-tableaux dans lesquels il est le minimum. En multipliant le nombre de sous-tableaux vers la gauche et la droite pour chaque élément, on obtient une contribution totale qui est ensuite additionnée.

### Complexité
- Temps : \(O(n)\), grâce à l'utilisation de piles monotones.
- Espace : \(O(n)\) pour les tableaux auxiliaires.

## Utilisation
### Prérequis
- Python 3.x

### Exécution
Clonez le dépôt, puis exécutez le script avec Python.

```bash
git clone https://github.com/votre-utilisateur/ravi-illusion-array-sum.git
cd ravi-illusion-array-sum
python illusion_of_array.py
Entrée : Entrez d'abord la longueur du tableau, suivie des éléments du tableau sur une seule ligne, par exemple :

4
71 55 82 55
Sortie : La somme des minimums de tous les sous-tableaux, modulo 
1
0
9
+
7
10 
9
 +7.

Input:
4
71 55 82 55

Output:
593