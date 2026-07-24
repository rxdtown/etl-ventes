import pandas as pd

def extract(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df