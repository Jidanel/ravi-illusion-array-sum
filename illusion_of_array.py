MOD = 10**9 + 7

def illusion_of_array(arr):
    n = len(arr)
    left = [0] * n
    right = [0] * n
    stack = []
    
    # Calculer les limites vers la gauche
    for i in range(n):
        count = 1
        while stack and stack[-1][0] > arr[i]:
            count += stack.pop()[1]
        left[i] = count
        stack.append((arr[i], count))
    
    stack = []
    
    # Calculer les limites vers la droite
    for i in range(n - 1, -1, -1):
        count = 1
        while stack and stack[-1][0] >= arr[i]:
            count += stack.pop()[1]
        right[i] = count
        stack.append((arr[i], count))
    
    # Calculer la "somme des illusions"
    result = 0
    for i in range(n):
        result = (result + arr[i] * left[i] * right[i]) % MOD
    
    return result

# Lecture de l'entrée
n = int(input())
arr = list(map(int, input().split()))

# Calculer et afficher le résultat
print(illusion_of_array(arr))
