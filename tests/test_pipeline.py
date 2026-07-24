import pandas as pd
from src.quality_checks import drop_duplicates, fill_missing_quantite, check_missing_values
from src.transform import transform

def test_drop_duplicates():
    df = pd.DataFrame({
        "produit": ["Clavier", "Clavier"],
        "quantite": [5, 5],
        "prix_unitaire": [150.0, 150.0],
        "date": ["2026-01-05", "2026-01-05"],
    })
    result = drop_duplicates(df)
    assert len(result) == 1

def test_fill_missing_quantite():
    df = pd.DataFrame({"quantite": [5.0, None, 10.0]})
    result = fill_missing_quantite(df)
    assert result["quantite"].isnull().sum() == 0

def test_transform_aggregation():
    df = pd.DataFrame({
        "produit": ["Clavier", "Clavier"],
        "quantite": [5, 3],
        "prix_unitaire": [150.0, 150.0],
    })
    result = transform(df)
    assert result.loc[result["produit"] == "Clavier", "quantite_totale"].values[0] == 8
    assert result.loc[result["produit"] == "Clavier", "chiffre_affaires"].values[0] == 1200.0