import pandas as pd

# Charger les données depuis un fichier CSV
input_file = 'cancer patient data sets.csv' 
df = pd.read_csv(input_file)

df['Gender'] = df['Gender'].replace({1: 'Femelle', 2: 'Male'})
df=df.drop(df.columns[0],axis=1)
# 1. Catégorisation de l'âge
def categorize_age(age):
    if age <= 12:
        return 'Jeune enfant'
    elif 13 <= age <= 17:
        return 'Adolescent'
    elif 18 <= age <= 35:
        return 'Jeune adulte'
    elif 36 <= age <= 59:
        return 'Adulte'
    else:
        return 'Senior'

df['Age'] = df['Age'].apply(categorize_age)

# 2. Catégorisation spécifique pour chaque attribut
def categorize_air_pollution(value):
    if value <= 3:
        return 'Faible pollution'
    elif 4 <= value <= 6:
        return 'Pollution modérée'
    else:
        return 'Forte pollution'

def categorize_alcohol_use(value):
    if value <= 2:
        return 'Faible consommation'
    elif 3 <= value <= 5:
        return 'Consommation modérée'
    else:
        return 'Grande consommation'

def categorize_dust_allergy(value):
    if value <= 3:
        return 'Allergie faible'
    elif 4 <= value <= 6:
        return 'Allergie modérée'
    else:
        return 'Allergie sévère'

def categorize_occupational_hazards(value):
    if value <= 3:
        return 'Risque faible'
    elif 4 <= value <= 6:
        return 'Risque modéré'
    else:
        return 'Risque élevé'

def categorize_genetic_risk(value):
    if value <= 3:
        return 'Risque génétique faible'
    elif 4 <= value <= 6:
        return 'Risque génétique modéré'
    else:
        return 'Risque génétique élevé'

def categorize_chronic_lung_disease(value):
    if value <= 3:
        return 'Maladie pulmonaire légère'
    elif 4 <= value <= 6:
        return 'Maladie pulmonaire modérée'
    else:
        return 'Maladie pulmonaire sévère'

def categorize_balanced_diet(value):
    if value <= 3:
        return 'Régime déséquilibré'
    elif 4 <= value <= 6:
        return 'Régime équilibré'
    else:
        return 'Régime très équilibré'

def categorize_obesity(value):
    if value <= 3:
        return 'Poids normal'
    elif 4 <= value <= 6:
        return 'Surpoids'
    else:
        return 'Obésité'

def categorize_smoking(value):
    if value <= 3:
        return 'Non-fumeur'
    elif 4 <= value <= 6:
        return 'Fumeur occasionnel'
    else:
        return 'Fumeur régulier'

def categorize_passive_smoker(value):
    if value <= 3:
        return 'Exposition faible'
    elif 4 <= value <= 6:
        return 'Exposition modérée'
    else:
        return 'Exposition élevée'

def categorize_chest_pain(value):
    if value <= 3:
        return 'Douleur faible'
    elif 4 <= value <= 6:
        return 'Douleur modérée'
    else:
        return 'Douleur intense'

def categorize_coughing_of_blood(value):
    if value <= 3:
        return 'Saignement rare'
    elif 4 <= value <= 6:
        return 'Saignement occasionnel'
    else:
        return 'Saignement fréquent'

def categorize_fatigue(value):
    if value <= 3:
        return 'Fatigue légère'
    elif 4 <= value <= 6:
        return 'Fatigue modérée'
    else:
        return 'Fatigue sévère'

def categorize_weight_loss(value):
    if value <= 3:
        return 'Perte de poids faible'
    elif 4 <= value <= 6:
        return 'Perte de poids modérée'
    else:
        return 'Perte de poids importante'

def categorize_shortness_of_breath(value):
    if value <= 3:
        return 'Essoufflement léger'
    elif 4 <= value <= 6:
        return 'Essoufflement modéré'
    else:
        return 'Essoufflement sévère'

def categorize_wheezing(value):
    if value <= 3:
        return 'Respiration sifflante légère'
    elif 4 <= value <= 6:
        return 'Respiration sifflante modérée'
    else:
        return 'Respiration sifflante sévère'

def categorize_swallowing_difficulty(value):
    if value <= 3:
        return 'Difficulté légère'
    elif 4 <= value <= 6:
        return 'Difficulté modérée'
    else:
        return 'Difficulté sévère'

def categorize_clubbing_of_finger_nails(value):
    if value <= 3:
        return 'Faible clubbing'
    elif 4 <= value <= 6:
        return 'Clubbing modéré'
    else:
        return 'Clubbing sévère'

def categorize_frequent_cold(value):
    if value <= 3:
        return 'Rhume rare'
    elif 4 <= value <= 6:
        return 'Rhume occasionnel'
    else:
        return 'Rhume fréquent'

def categorize_dry_cough(value):
    if value <= 3:
        return 'Toux sèche légère'
    elif 4 <= value <= 6:
        return 'Toux sèche modérée'
    else:
        return 'Toux sèche sévère'

def categorize_snoring(value):
    if value <= 3:
        return 'Ronflement léger'
    elif 4 <= value <= 6:
        return 'Ronflement modéré'
    else:
        return 'Ronflement sévère'

# Appliquer les catégorisations spécifiques
df['Air Pollution'] = df['Air Pollution'].apply(categorize_air_pollution)
df['Alcohol use'] = df['Alcohol use'].apply(categorize_alcohol_use)
df['Dust Allergy'] = df['Dust Allergy'].apply(categorize_dust_allergy)
df['OccuPational Hazards'] = df['OccuPational Hazards'].apply(categorize_occupational_hazards)
df['Genetic Risk'] = df['Genetic Risk'].apply(categorize_genetic_risk)
df['chronic Lung Disease'] = df['chronic Lung Disease'].apply(categorize_chronic_lung_disease)
df['Balanced Diet'] = df['Balanced Diet'].apply(categorize_balanced_diet)
df['Obesity'] = df['Obesity'].apply(categorize_obesity)
df['Smoking'] = df['Smoking'].apply(categorize_smoking)
df['Passive Smoker'] = df['Passive Smoker'].apply(categorize_passive_smoker)
df['Chest Pain'] = df['Chest Pain'].apply(categorize_chest_pain)
df['Coughing of Blood'] = df['Coughing of Blood'].apply(categorize_coughing_of_blood)
df['Fatigue'] = df['Fatigue'].apply(categorize_fatigue)
df['Weight Loss'] = df['Weight Loss'].apply(categorize_weight_loss)
df['Shortness of Breath'] = df['Shortness of Breath'].apply(categorize_shortness_of_breath)
df['Wheezing'] = df['Wheezing'].apply(categorize_wheezing)
df['Swallowing Difficulty'] = df['Swallowing Difficulty'].apply(categorize_swallowing_difficulty)
df['Clubbing of Finger Nails'] = df['Clubbing of Finger Nails'].apply(categorize_clubbing_of_finger_nails)
df['Frequent Cold'] = df['Frequent Cold'].apply(categorize_frequent_cold)
df['Dry Cough'] = df['Dry Cough'].apply(categorize_dry_cough)
df['Snoring'] = df['Snoring'].apply(categorize_snoring)

# 3. Sauvegarder le fichier corrigé avec des catégories textuelles
output_file = 'cancer patient data sets corrigee.csv'
df.to_csv(output_file, index=False)

print(f"Le fichier corrigé avec des catégories textuelles a été sauvegardé sous : {output_file}")