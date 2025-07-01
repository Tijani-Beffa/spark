from pyspark import SparkContext

# Fonction pour générer les paires d’amis normalisées (min, max)
def generate_pairs(line):
    parts = line.split()
    if len(parts) != 3:
        return []
    user = parts[0]
    friends = parts[2].split(",")
    return [((min(user, f), max(user, f)), set(friends)) for f in friends]

if __name__ == "__main__":
    sc = SparkContext("local", "AmisCommuns")

    # Chargement du fichier texte
    data = sc.textFile("amis.txt")

    # Création des paires
    pairs = data.flatMap(generate_pairs)

    # Calcul des amis communs via intersection
    common_friends = pairs.reduceByKey(lambda x, y: x & y)

    # Filtrer uniquement la paire Sidi (1) et Mohamed (2)
    target = common_friends.filter(lambda x: x[0] == ("1", "2")).collect()

    for (pair, friends) in target:
        print(f"{pair[0]}<Sidi>{pair[1]}<Mohamed>{','.join(friends)}")
