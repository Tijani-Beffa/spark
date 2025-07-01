# 🚀 Mini Projet Big Data avec PySpark : Recherche d'Amis en Commun

## 📘 Présentation du projet

Ce projet a pour objectif de démontrer comment exploiter **Apache Spark** (via **PySpark**) pour analyser un **graphe social**.  
L'objectif est d'identifier efficacement les **amis en commun entre deux utilisateurs** d'un réseau, à partir d'un fichier texte contenant des relations d’amitié.

---

## 📂 Données d’entrée

Le fichier source (`amis.txt`) contient une **liste d’adjacence** représentant les utilisateurs et leurs amis :

```
<user_id> <nom> <ami1>,<ami2>,<ami3>,...
```

Exemple :
```
1 Sidi 2,3,4
2 Mohamed 1,4,5
```

---

## 🎯 Objectifs pédagogiques

- Utiliser PySpark pour traiter des données relationnelles
- Appliquer le modèle MapReduce dans Spark
- Générer dynamiquement les couples `(utilisateur, ami)`
- Trouver les amis communs à une paire d’utilisateurs (ex. : **Sidi** et **Mohamed**)

---

## ⚙️ Technologies

- Python 3
- Apache Spark (PySpark)
- RDD (Resilient Distributed Dataset)
- GitHub (pour versionnage et partage)

---

## 🧪 Étapes d’exécution

### 1. Lecture du fichier texte

```python
data = sc.textFile("amis.txt")
```

### 2. Génération des paires normalisées

```python
def generate_pairs(line):
    parts = line.split()
    if len(parts) != 3:
        return []
    user = parts[0]
    friends = parts[2].split(",")
    return [((min(user, f), max(user, f)), set(friends)) for f in friends]
```

### 3. Calcul des amis communs

```python
pairs = data.flatMap(generate_pairs)
common_friends = pairs.reduceByKey(lambda x, y: x & y)
```

### 4. Extraction des amis communs entre l’utilisateur `1` (Sidi) et `2` (Mohamed)

```python
target = common_friends.filter(lambda x: x[0] == ("1", "2")).collect()
for (pair, friends) in target:
    print(f"{pair[0]}<Sidi>{pair[1]}<Mohamed>{','.join(friends)}")
```

---

## ✅ Exemple de sortie

```
1<Sidi>2<Mohamed>4
```

---

## 🗂 Arborescence du projet

```
spark-amis-communs/
├── amis.txt         # Fichier d'entrée
├── main.py          # Script principal PySpark
├── output.txt       # Exemple de sortie
├── README.md        # Présentation du projet
```

---

## 👨‍🎓 Réalisé par

- Nom : Mohmed Mahmoud Ahmedou Beffa
- Master ISDR – Université de Nouakchott Al Aasriya
- Année : 2024 / 2025

---

## 📬 Contact

Pour toute question, contactez-moi via GitHub ou par mail.

