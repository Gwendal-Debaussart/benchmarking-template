import os
import pandas as pd
from benchmarks.loader import load_dataset
from .evaluation import evaluate


def get_existing_repeats(
    dataset_name: str,
    method_name: str,
    metrics: list = [],
    save_dir="tables/benchmark_raw/",
):
    """
    Get the number of existing repeats for the given arguments. If a metric list is provided,
    only counts repeats that have results for all specified metrics.

    :param dataset_name: str
    :param method_name: str
    :param metrics: list, optional
    :param save_dir: str, optional
    :return: int, number of existing repeats for the given method and dataset, possibly filtered by metrics. 0 if none exist.
    """

    file_path = os.path.join(save_dir, f"{dataset_name}__raw.csv")
    if not os.path.exists(file_path):
        return 0
    df = pd.read_csv(file_path)
    existing = df[df["method"] == method_name]
    if existing.empty:
        return 0

    if len(metrics) == 0:
        return existing["repeat"].max() + 1

    existing = existing[existing["metric"].isin(metrics)]
    if existing.empty:
        return 0

    for metric in existing["metric"].unique():
        metric_repeats = existing[existing["metric"] == metric]["repeat"].nunique()
        if metric_repeats < existing["repeat"].nunique():
            return metric_repeats
    return existing["repeat"].nunique()


def save_raw_results(dataset, method_name, repeats, save_dir="tables/benchmark_raw/"):
    """
    Save raw repeat-level benchmark results (append-only).
    """
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, f"{dataset['name']}__raw.csv")

    if os.path.exists(filepath):
        df_existing = pd.read_csv(filepath)
        mask = df_existing["method"] == method_name
        if mask.any():
            repeat_offset = df_existing.loc[mask, "repeat"].max() + 1
        else:
            repeat_offset = 0
    else:
        repeat_offset = 0

    rows = []
    for i, repeat in enumerate(repeats):
        for metric, value in repeat.items():
            rows.append(
                {
                    "method": method_name,
                    "repeat": i + repeat_offset,
                    "metric": metric,
                    "value": value,
                }
            )
    df_new = pd.DataFrame(rows)

    if os.path.exists(filepath):
        df_new.to_csv(filepath, mode="a", header=False, index=False)
    else:
        df_new.to_csv(filepath, index=False)

    print(f"[{dataset['name']} -- {method_name}] Raw results appended to {filepath}")


def run_one_repeat(
    method: dict,
    X,
    Y,
    metrics: list = [],
):
    """
    Run one repeat of the benchmark with the given arguments, e.g., one method on one dataset.

    method : dict
        A dictionary representing the method to be benchmarked.
    X : any
        The input data for the method.
    Y : any
        The true labels or outputs for the method.

    Returns:
    --------
    score_dict : dict
        A dictionary containing the evaluation scores for the method. {"metric_name": score_value, ...}
    """
    # replace with actual method execution logic
    score_dict = evaluate(method, X, Y, metrics)
    return score_dict


def run_benchmark_for_dataset(
    dataset, methods, num_repeats=100, save_dir="tables/benchmark_raw/", metrics=[]
):
    """
    Run benchmark for one dataset.
    """
    dataset_name = dataset["name"]
    X, Y = load_dataset(dataset_name, **dataset.get("parameters", {}))
    all_results = []
    for method in methods:
        method_name = method["name"]
        existing_repeats = get_existing_repeats(
            dataset_name=dataset_name,
            method_name=method_name,
            save_dir=save_dir,
            metrics=metrics,
        )
        repeats = []
        for repeat in range(existing_repeats, num_repeats):
            print(
                f"Running method {method_name} on dataset {dataset_name}, repeat {repeat+1}/{num_repeats}"
            )
            result = run_one_repeat(
                method=method,
                X=X,
                Y=Y,
                metrics=metrics,
            )
            repeats.append(result)

        print(
            f"[{dataset_name}] Completed [{num_repeats - existing_repeats}] repeats for {method['name']}"
        )
        save_raw_results(dataset, method["name"], repeats)
        all_results.extend(repeats)
    return all_results
