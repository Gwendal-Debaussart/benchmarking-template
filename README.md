# Benchmarking Template

This repository provides a template for benchmarking machine learning methods on various datasets.
It includes utilities for running benchmarks, saving results, and evaluating methods.
Files needs to be tuned to the specific methods and datasets being benchmarked.

## Features

This template includes:
- Predefined structure for datasets and methods.
- Modular structure for easy addition of new datasets and methods.
- Utility scripts for running benchmarks and formatting results.
- Evaluation framework for assessing method performance.
- LaTeX support for generating reports and table from benchmark results.

Everything is designed to be easily customizable to fit different benchmarking needs.

## Directory Structure

The repository is organized as follows:
- `benchmarks/`: Contains dataset definitions and loading functions.
- `methods/`: Contains method definitions and initialization functions.
- `utils/`: Contains utility scripts for running benchmarks, formatting results, and evaluating methods.

Each file in the `benchmarks` and `methods` directories should define a function that loads the dataset or initializes the method, respectively.

## Usage

1. **Datasets**: place your datasets in the `benchmarks` directory: add a .py file for each dataset containing a function that loads and returns the dataset. The function should be added in the function `dataset_list` in the `benchmarks/loader.py` file (see file for the correct format).
2. **Methods**: place your methods in the `methods` directory: add a .py file for each method containing a function that initializes and returns the method. The function should be added in the function `method_list` in the `methods/loader.py` file (see file for the correct format).
3. **Run Benchmarks**: Use the `utils/run_benchmark.py` script to run benchmarks on the specified methods and datasets. Adjust parameters as needed.
4. **Format Results**: Use the `utils/format_results.py` script to format and summarize the benchmark results.
5. **Evaluate Methods**: Implement the evaluation logic in `utils/evaluation.py` as needed for your specific use case.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This template is made by Gwendal Debaussart-Joniec. Feel free to contribute and improve it!
