# Benchmarking Template

This repository provides a template for benchmarking machine learning methods on various datasets. It includes utilities for running benchmarks, saving results, and evaluating methods. Files needs to be tuned to the specific methods and datasets being benchmarked.

## Utilities
- `utils/run_benchmark.py`: Contains functions to run benchmarks and manage results, by default, it saves the number of repeats for each method-dataset combination inside a CSV file located in `tables/benchmark_raw/`.
- `utils/format_results.py`: Contains functions to format raw benchmark results into summary tables.
- `utils/evaluation.py`: Contains functions to evaluate methods on datasets: To be implemented by used to match the needed formulation.