import pandas as pd
import numpy as np

# PARTE - 1 - CARICAMENTO ED ESPOLARIONE

# CARICAMENTO DATASET
df = pd.read_csv("dataset_vendite.csv")

# PRIME RIGHE
print(df.head())

# INFORMAZIONI DATASET
print(df.info())

# PARTE DESCRITTIVA
print(df.describe())

# VALORI MANCANTI
print(df.isna().sum())

# PARTE - 2 - PULIZIA DATI

# Imputazione valori mancanti
df["Vendite"] = df["Vendite"].fillna(df["Vendite"].mean())
df["Prezzo"] = df["Prezzo"].fillna(df["Prezzo"].mean())

# Verifica valori mancanti dopo la pulizia
print(df.isna().sum())

# Identificazione duplicati
print("Duplicati", df.duplicated().sum())

# Rimozione duplicati
df = df.drop_duplicates()

# Verifica duplicati
print("Duplicati:", df.duplicated().sum())

# Conversione della colonna Data
df["Data"] = pd.to_datetime(df["Data"])

# Verifica dei tipi di dato
print(df.info())

# PARTE - 3 - ANALISI ESPLORATIVA

# Vendite totali per prodotto
vendite_totali = df.groupby("Prodotto")["Vendite"].sum()
print(vendite_totali)

# Ricerca prodotto piu o meno venduto
prodotto_piu_venduto = vendite_totali.idxmax()
prodotto_meno_venduto = vendite_totali.idxmin()

print("Prodotto più venduto:", prodotto_piu_venduto)
print("Prodotto_meno_venduto:", prodotto_meno_venduto)

# Vendite giornaliere
vendite_giornaliere = df.groupby("Data")["Vendite"].sum()

# Vendite medie giornaliere
media_giornaliera = vendite_giornaliere.mean()
print("Vendite medie giornaliere:", media_giornaliera)