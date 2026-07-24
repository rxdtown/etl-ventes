import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df["montant_total"] = df["quantite"] * df["prix_unitaire"]
    agg = df.groupby("produit").agg(
        quantite_totale=("quantite", "sum"),
        chiffre_affaires=("montant_total", "sum"),
    ).reset_index()
    return agg