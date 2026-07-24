import pandas as pd

class DataQualityError(Exception):
    pass

def check_missing_values(df: pd.DataFrame, seuil: float = 0.2) -> pd.DataFrame:
    taux_manquant = df.isnull().mean()
    for col, taux in taux_manquant.items():
        if taux > seuil:
            raise DataQualityError(f"Colonne '{col}' a {taux:.0%} de valeurs manquantes (seuil {seuil:.0%})")
    return df

def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    avant = len(df)
    df = df.drop_duplicates(subset=["produit", "quantite", "prix_unitaire", "date"])
    apres = len(df)
    print(f"[DQ] {avant - apres} doublon(s) supprimé(s)")
    return df

def fill_missing_quantite(df: pd.DataFrame) -> pd.DataFrame:
    mediane = df["quantite"].median()
    df["quantite"] = df["quantite"].fillna(mediane)
    return df