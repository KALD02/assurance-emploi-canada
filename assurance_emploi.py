import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os

# Upload the file 
#df = pd.read_csv("/Users/alainkammogne/Downloads/Projets Python/Canadastatistics/assurance_emploi_canada.csv")

# Keep only useful columns
#useful_columns = ['REF_DATE', 'GEO', 'Sex', 'Age group', 'Beneficiary detail', 'VALUE']
#df = df[useful_columns]

# Rename columns
#df.columns = ['Date', 'Province', 'Sexe', 'Groupe_Age', 'Prestation', 'Beneficiaires']

# Save a new, smaller file
#df.to_csv("/Users/alainkammogne/Downloads/Projets Python/Canadastatistics/assurance_canada.csv", index=False)

# Upload the new file
df = pd.read_csv("/Users/alainkammogne/Desktop/assurance_canada.csv")

# Checking for missing values
print(df.isnull().sum())

# Search for extreme / outlier values
print(df["Beneficiaires"].describe())
print("****************************************************************\n")
# Analyze NaNs to see if they are concentrated
print(df[df["Beneficiaires"].isna()]["Province"].value_counts())
print("****************************************************************\n")
print(df[df["Beneficiaires"].isna()]["Date"].value_counts())

# Delete only NaN lines
df = df.dropna(subset=["Beneficiaires"])

print("****************************************************************\n")
# Checking for missing values
print(df.isnull().sum())

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Aggregate: total number of beneficiaries per month
df_total_benef_month = df.groupby("Date")["Beneficiaires"].sum().reset_index()
print(df_total_benef_month)

# Visualization of the graph between Date and Beneficiaries
# Definition of the size of the graph
plt.figure(figsize=(12, 6))
# Begining with visualization
sns.lineplot(data=df_total_benef_month, x="Date", y="Beneficiaires", markers="o")
# Title of graph
plt.title("Évolution du nombre de bénéficiaire de l'assurance-emploi au Canada")
# Name of axis
plt.xlabel("Date")
plt.ylabel("Nombre de beneficiaires")
plt.grid("True")
plt.tight_layout()
plt.show()
# Aggregate: total of beneficiaries per province
df_total_benef_province = df.groupby("Province")["Beneficiaires"].sum().reset_index()
print(df_total_benef_province)

# Create a dictionary to map names to abbreviation
province_map = {
    "Alberta": "AB",
    "British Columbia": "BC",
    "Manitoba": "MB",
    "New Brunswick": "NB",
    "Newfoundland and Labrador": "NL",
    "Nova Scotia": "NS",
    "Ontario": "ON",
    "Prince Edward Island": "PE",
    "Quebec": "QC",
    "Saskatchewan": "SK",
    "Northwest Territories": "NT",
    "Nunavut": "NU",
    "Yukon": "YT",
    "Canada": "CA"
}

# Match the province column with abbreviations
df_total_benef_province["Province_abr"] = df_total_benef_province["Province"].map(province_map)

# Visualization of the graph between Province and Beneficiaries
# Definition of the size of the graph
plt.figure(figsize=(12, 6))
# Begining with visualization
sns.lineplot(data=df_total_benef_province, x="Province_abr", y="Beneficiaires", markers="o")
# Title of graph
plt.title("Évolution du nombre de bénéficiaire de l'assurance-emploi au Canada par province")
# Name of axis
plt.xlabel("Province")
plt.ylabel("Nombre de beneficiaires")
plt.grid("True")
plt.tight_layout()
plt.show()

# Sort the DataFrame in descinding order
df_range_asc = df_total_benef_province.sort_values(by="Beneficiaires", ascending=False)
#print(df_range_asc.head(5))

# Filter post COVID data
df_post_covid = df[df["Date"] >= "2020-04-01"]
print(df_post_covid)

# Group by age group and sum of the beneficiaries
df_age_post_covid = df_post_covid.groupby("Groupe_Age")["Beneficiaires"].sum().reset_index()
df_age_post_covid = df_age_post_covid.sort_values(by="Beneficiaires", ascending=False)
#print(df_age_post_covid)
# Visualization of the graph between Province and Beneficiaries
# Definition of the size of the graph
plt.figure(figsize=(12, 6))
# Begining with visualization
sns.lineplot(data=df_age_post_covid, x="Groupe_Age", y="Beneficiaires", markers="o")
# Title of graph
plt.title("Évolution du nombre de bénéficiaire de l'assurance-emploi au Canada en fonction des groupes d'age")
# Name of axis
plt.xlabel("Groupe Age")
plt.ylabel("Nombre de beneficiaires")
plt.grid("True")
plt.tight_layout()
plt.show()

# Saved the images link
os.makedirs("images", exist_ok=True)

plt.savefig("images/Evolution_du_nombre_de_beneficiaires_de_lassurance_emploi_au_canada.png")
plt.savefig("images/Evolution_du_nbre_benef_au_canada_par_province.png")
plt.savefig("images/Evolution_du_nombre_de_beneficiaires_de_lassurance_emploi_au_Canada_en_fonction_des_groupes_dage.png")
