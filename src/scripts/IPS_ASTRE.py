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

#Here i create a function to verify if all keywords in the answers given by the students
def isVerified(hypothesis, answers):
    for keyword in hypothesis:
        if keyword not in answers:
            return False
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

print(structured_data)


