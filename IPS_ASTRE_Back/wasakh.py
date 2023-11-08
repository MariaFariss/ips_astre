import csv
import json
data = [
    {"C": -2, "Java": 2, "JavaScript, HTML, CSS": 3, "Python": 1, "C++": -2, "Kotlin/Dart": 2, "C#": -2},
    {"Linux": 0, "Windows": 0, "Mac OS": 0, "Chrome OS": 0},
    {"Domotique": -4, "UX/UI": 4, "Frontend/Backend": 2, "Robotique": -4},
    {"VR/AR": 3 , "Arduino": -3, "Intelligence Artificielle": 1, "Moteur de jeu vidéo": 1, "Aucune": 0},
    {"PC": 0, "Téléphone": 0, "Non": 0},
    {"Le redstone": 0, "Construire des choses": 0, "Je connais pas/j'y joue pas": 0},
    {"Science de l'ingénieur (SI)": 1, "Mathématiques": 1, "Numérique et sciences informatiques": 0, "Physique-chimie": -1, "Sciences de la vie et de la Terre (SVT)": 0, "Biologie, écologie": 0},
    {"BDE": 0, "CULTU": 0, "K'verne": 0, "ENIGMA": 1, "ENSIMERSION": 3, "ENSIM'ELEC": -1, "GALA": 0, "Les trublions du plateau": 0, "Aucune": 0},
    {"Option 1": 2, "Option 2": -1, "Option 3": -1, "Option 4": -1},
    {"VSCode": 2, "Vim": -2, "La suite JetBrains (IntelliJ, PyCharm ...)": 2, "Code::Blocks": 1, "NetBeans": 2, "La suite anaconda (Jupyter ...)": 1},
    {"0": -1, "1": -1, "2": -1, "3": -1, "4": -1, "5": 0, "6": 1, "7": 1, "8": 1, "9": 1},
    {"Histoire - Géographie": 0, "EPS": 0, "Français": 0, "Mathématiques": 0, "Physique-Chimie": -1},
    {"Freelance (Indépendant)": 2, "PME / Startups": 1, "Grande entreprise, grand groupe": 0, "Laboratoire de recherche": -1},
    {"Résoudre des problèmes avec du code": 1, "Créer du contenu": -1, "Manager": 0, "La cyber-sécurité": 1},
    {"Brésil": 0, "Cameroun": 1, "Côte d'Ivoire": 1, "France": 0, "Maroc": 1, "Tunisie": 1},
    {"L’esthétique": 2, "Le fonctionnel": 0, "La sécurité": 1},
    {"Un tournevis, c'est toujours utile": -1, "Papier, crayon, trousse, la base": 0, "Mon pc portable only": 0, "Je ne prends pas de sac à dos": 0}
]


# import csv

# def calculate_scores(data, filename):
#     scores = {}
    # ips_keywords = {
    #     "Java": 4, "JavaScript, HTML, CSS": 4,
    #     "La suite JetBrains (IntelliJ, PyCharm ...)": 2, "VR/AR": 2, "Intelligence Artificielle": 2, "Résoudre des problèmes avec du code": 2,
    #     "La cyber-sécurité": 3, "ENSIMERSION": 3, "Option 1": 3
    # }
    # astre_keywords = {
    #     "Domotique": -4, "Robotique": -4, "C++": -4,
    #     "C": -2, "Option 2": -2, "Option 3": -2, "Option 4": -2,
    #     "NetBeans": -1, "Vim": -1
    # }

#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             score = 0
#             for i, response in enumerate(row):
#                 if i < len(data) and response in data[i]:
#                     score += data[i][response]
#                 if response in ips_keywords:
#                     score += ips_keywords[response]
#                 if response in astre_keywords:
#                     score += astre_keywords[response]
#             if score > 0:
#                 scores[row[1]] = ("IPS", score)
#             else:
#                 scores[row[1]] = ("ASTRE", score)
#     return scores

# scores = calculate_scores(data, 'Questionnaires.csv')
# for student, info in scores.items():
#     print(f"L'étudiant {student} est probablement {info[0]} avec un score de {info[1]}")



import csv

# Extraction du tableau CSV
def extract_csv_data(filename):
    data = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorer la première ligne d'en-têtes
        for row in reader:
            data.append(row)

    return data

csv_data = extract_csv_data('Questionnaires.csv')

# Transformation du tableau CSV en une structure de données (exemple : dictionnaire)
def transform_to_data_structure(data):
    scores = {}

    ips_keywords = {
        ("UX/UI", "Option 1"): 3,    
        ("VR/AR", "ENSIMERSION"): 3,
        ("Frontend/Backend", "JavaScript, HTML, CSS"): 3,
        ("Python", "Intelligence Artficielle"): 1,
        ("UX/UI", "L’esthétique"): 4,
    }

    astre_keywords = {
        ("Domotique", "Robotique", "C++"): -4,
        ("C++", "Arduino"): -3,
        ("MAO", "Option 2"): -1,
        ("Robotique", "Vim"): -1,
        ("NetBeans", "C++"): -3
    }

    for row in data:
        student_id = row[1]
        score = 0
        for response in row[2:]:
            for key, value in ips_keywords.items():
                if response in key:
                    score += value
            for key, value in astre_keywords.items():
                if response in key:
                    score += value
        label = "IPS" if score > 0 else "ASTRE"
        scores[student_id] = (label, score)

    return scores

structured_data = transform_to_data_structure(csv_data)

# Modélisation des données sous forme d'une structure adaptée (ici, un dictionnaire)
print(structured_data)

# Écrire les données structurées dans un fichier JSON
json_filename = 'structured_data.json'
with open(json_filename, 'w') as json_file:
    json.dump(structured_data, json_file, indent=4)

# Lire les données du fichier JSON (facultatif)
with open(json_filename, 'r') as json_file:
    loaded_data = json.load(json_file)
    print("Loaded Data:")
    print(loaded_data)