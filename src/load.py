import pandas as pd
import os

def load(df: pd.DataFrame, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_parquet(output_path, index=False)
    print(f"[LOAD] Fichier écrit : {output_path}")