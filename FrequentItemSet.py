from itertools import combinations
import csv
import numpy as np
import matplotlib.pyplot as plt

# Global data structures:
dataSet = []
itemSet = set()
candidates = {}
associations = []

def generateData(filepath):
    global itemSet
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data = [item.strip() for item in row if item.strip() != '']
            dataSet.append(sorted(data))
            for d in data:
                itemSet.add(d)
    itemSet = set(sorted(itemSet))

def apriori_gen(k, Ck, Ck_p):
    print(f"Generating {k}-item candidate set")
    if k == 1:
        for item in itemSet:
            Ck.append([item])
        return
    cklen = len(Ck_p)
    for i in range(cklen):
        for j in range(i + 1, cklen):
            if Ck_p[i][:-1] == Ck_p[j][:-1]:
                Ck.append(Ck_p[i] + [Ck_p[j][-1]])

def supportof(pat):
    pat = frozenset(pat)
    frequency = sum(1 for transaction in dataSet if pat.issubset(transaction))
    return frequency

def calculate_dynamic_minsup(supports):
    q1 = np.percentile(supports, 25)
    q3 = np.percentile(supports, 75)
    iqr = q3 - q1
    return np.median(supports) + 0.5 * iqr

def generateAssociateRule(pat, suppat, minconf, NTd):
    for i in range(1, len(pat)):
        for left in combinations(pat, i):
            left = list(left)
            right = list(set(pat) - set(left))
            if not right:
                continue
            conf = float(suppat) / candidates[frozenset(left)]
            if conf >= minconf:
                associations.append((conf, left, right, float(suppat) / NTd))

def apriori(minconf):
    k = 1
    NTd = len(dataSet)
    initial_supports = [supportof([item]) for item in itemSet]
    minsup = calculate_dynamic_minsup(initial_supports)
    print(f"Initial MinSup: {minsup}")
    
    Ck_p = []
    all_supports = []  # Pour stocker le min_support de chaque itération
    frequent_items = []  # Pour stocker tous les itemsets fréquents

    while True:
        Ck = []
        apriori_gen(k, Ck, Ck_p)
        Ck_p = []
        if not Ck:
            break
        current_supports = []
        for c in Ck:
            supc = supportof(c)
            current_supports.append(supc)
            if supc >= minsup:
                generateAssociateRule(c, supc, minconf, NTd)
                candidates[frozenset(c)] = supc
                Ck_p.append(sorted(c))
                frequent_items.append((c, supc))
        if not current_supports:
            break
        new_minsup = max(minsup, calculate_dynamic_minsup(current_supports))
        print(f"Iteration {k}: Updated MinSup: {new_minsup}")
        minsup = new_minsup
        all_supports.append(minsup)  # Stocker le min_support
        k += 1

    return all_supports, frequent_items

def visualize_support_evolution(supports):
    """Visualisation de l'évolution du min_support"""
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(supports) + 1), supports, marker='o', linestyle='-', color='b')
    plt.xlabel("Itération")
    plt.ylabel("Min Support")
    plt.title("Évolution du min_support dynamique")
    plt.grid()
    plt.show()

def visualize_frequent_itemsets(frequent_items):
    """Visualisation des itemsets fréquents"""
    if not frequent_items:
        print("Aucun itemset fréquent trouvé.")
        return
    
    itemsets = ["-".join(i[0]) for i in frequent_items]
    support_counts = [i[1] for i in frequent_items]

    plt.figure(figsize=(10, 6))
    plt.barh(itemsets, support_counts, color='skyblue')
    plt.xlabel("Support")
    plt.ylabel("Itemsets")
    plt.title("Itemsets Fréquents")
    plt.gca().invert_yaxis()
    plt.show()

def visualize_association_rules(associations):
    """Visualisation des règles d'association"""
    if not associations:
        print("Aucune règle d'association trouvée.")
        return
    
    antecedents = [" & ".join(map(str, a[1])) for a in associations]
    confidence = [a[0] for a in associations]
    support = [a[3] for a in associations]

    plt.figure(figsize=(10, 6))
    plt.scatter(support, confidence, c='purple', alpha=0.6)
    plt.xlabel("Support")
    plt.ylabel("Confiance")
    plt.title("Règles d'Association : Support vs Confiance")
    for i, txt in enumerate(antecedents):
        plt.annotate(txt, (support[i], confidence[i]), fontsize=9, alpha=0.7)
    plt.show()

def main():
    filepath = "cancer patient data sets corrigee.csv"
    minconf = 0.5
    
    generateData(filepath)
    all_supports, frequent_items = apriori(minconf)
    
    # Tri des règles d'association par confiance décroissante
    associations.sort(reverse=True, key=lambda x: x[0])
    
    print("\n------------------- ASSOCIATION RULES -------------------\n")
    for rule in associations:
        conf, left, right, sup = rule
        print(f"{left} ---> {right} | conf: {conf:.3f}, sup: {sup:.3f}")
    
    # Visualisations finales
    visualize_support_evolution(all_supports)
    visualize_frequent_itemsets(frequent_items)
    visualize_association_rules(associations)

if __name__ == "__main__":
    main()
