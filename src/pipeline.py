from src.extract import extract
from src.quality_checks import check_missing_values, drop_duplicates, fill_missing_quantite
from src.transform import transform
from src.load import load

def run_pipeline(input_path: str, output_path: str):
    df = extract(input_path)
    df = drop_duplicates(df)
    df = fill_missing_quantite(df)
    df = check_missing_values(df)
    df_agg = transform(df)
    load(df_agg, output_path)
    return df_agg

if __name__ == "__main__":
    run_pipeline("data/ventes.csv", "output/ventes_agregees.parquet")