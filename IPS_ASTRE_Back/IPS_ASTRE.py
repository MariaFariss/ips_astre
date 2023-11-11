import csv
import json

# I define a function that extract data from the csv file
def extract_csv_data(filename):
    data = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            data.append(row)

    return data

csv_data = extract_csv_data('Questionnaires.csv')

#Here i creat a function to verify if all keywords in the answers given by the students
def isVerified(hypothesis, answers):
    for keyword in hypothesis:
        # print(keyword)
        if keyword not in answers:
            return False
    # print(hypothesis)
    # print("----")
    return True

#hypothesis               
ips_keywords = {
        ("UX/UI", ): 3,    
        ("VR/AR", ): 3,
        ("Moteurs de jeux vidéo" , "ENSIMERSION" ): 4,
        ("Frontend / Backend", "JavaScript, HTML, CSS"): 3,
        ("Python", "Intelligence Artficielle"): 1,
        ("UX/UI", "L’esthétique"): 4,
    }

astre_keywords = {
        ("Domotique", "Robotique"): -4,
        ("Arduino", ): -3,
        ("Robotique", ): -3,
        ("MAO", "Vim"): -1,
        ("NetBeans", "C++"): -2
    }

# I transform the csv table (data) to a data structure like dictionnary 
def transform_to_data_structure(data=csv_data, ips_keywords=astre_keywords, astre_keywords=astre_keywords):
    scores = {}
    for row in data:
        student_id = row[1]
        score_etu = 0
        tabResult = []
        
        for answer in row[2:]:
            for keyword in answer.split(';'):
                tabResult.append(keyword)
        
        # print(tabResult)
        # print('-------')
        
        for hypothesis, score in ips_keywords.items():
            if(isVerified(hypothesis, tabResult)): 
                score_etu += score
        for hypothesis, score in astre_keywords.items():
            if(isVerified(hypothesis, tabResult)):   
                score_etu += score
        
        label = "IPS" if score_etu > 0 else "ASTRE"
        scores[student_id] = (label, score_etu)

    return scores

structured_data = transform_to_data_structure()

# Modélisation des données sous forme d'une structure adaptée (ici, un dictionnaire)
print(structured_data)

# I write tha data in json file that will helps me for my api
json_filename = 'structured_data.json'
with open(json_filename, 'w') as json_file:
    json.dump(structured_data, json_file, indent=4)

# Lire les données du fichier JSON (facultatif)
with open(json_filename, 'r') as json_file:
    loaded_data = json.load(json_file)
    # print("Loaded Data:")
    # print(loaded_data)