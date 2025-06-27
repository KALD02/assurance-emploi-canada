
## Analyse de l’assurance-emploi au Canada
Ce projet vise à analyser les tendances des bénéficiaires de l’assurance-emploi au Canada en utilisant des données publiques de Statistique Canada.

## Objectifs
Comprendre l’évolution du nombre de bénéficiaires de l’assurance-emploi.
Identifier les impacts de la crise post-COVID.
Segmenter l’analyse par province, groupe d’âge et sexe.
Visualiser les données de manière claire et interactive.

## Technologies utilisées

Python
 - Pandas pour la manipulation de données
 - Matplotlib et Seaborn pour la visualisation
 - Jupyter Notebook pour l'exécution interactive

## Structure du projet
bash
Copy
Edit
assurance-emploi-canada/
├── assurance_canada.csv        
├── assurance_emploi_analysis.ipynb  
└── README.md
└── images/
    ├── ![Évolution nationale](images/evolution_beneficiaires_canada.png)
    ├── ![Par province](images/evolution_beneficiaires_par_province.png)
    └── ![Par groupe d'âge](images/evolution_beneficiaires_par_groupe_age.png)

## Résultats clés
Plus de 1,5 million de lignes analysées
Suppression de plus de 120 000 valeurs manquantes
Analyse des bénéficiaires :
 -> par mois
 -> par province
 -> par groupe d’âge
 -> par sexe (dans une partie du projet)

## Mise en évidence :
 - d’un pic important post-COVID
 - de fortes disparités entre les provinces

## Prochaines étapes
Ajout d’un modèle prédictif pour estimer les tendances futures
Création de dashboards dynamiques avec Looker Studio

## Aperçu

Exemple de graphique réalisé avec Seaborn:
    -> Évolution du nombre de bénéficiaires de l’assurance-emploi au canada par province.png

## Auteur
Alain Kammogne

## 👉 Mon profil LinkedIn (www.linkedin.com/in/alain-kammogne-python)
