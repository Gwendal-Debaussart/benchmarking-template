import os
import pandas as pd

def format_results(dataset_name, results_dir, format_dir):
    """
    Format raw benchmark results into summary tables: mean and std deviation per metric and method.

    :param dataset_name: str
    :param results_dir: str
    :param format_dir: str
    :return: None

    """

    os.makedirs(format_dir, exist_ok=True)
    raw_file_path = os.path.join(results_dir, f"{dataset_name}__raw.csv")
    formatted_file_path = os.path.join(format_dir, f"{dataset_name}__formatted.csv")

    if not os.path.exists(raw_file_path):
        print(f"No raw results found for dataset {dataset_name} in {results_dir}.")
        return

    df_raw = pd.read_csv(raw_file_path)
    df_formatted = (
        df_raw.groupby(["method", "metric"])
        .agg(
            repeat_tol=("repeat", "count"),
            mean_val=("value", "mean"),
            std_val=("value", "std"),
        )
        .reset_index()
    )
    df_formatted.to_csv(formatted_file_path, index=False)
    print(f"Formatted results saved to {formatted_file_path}")
