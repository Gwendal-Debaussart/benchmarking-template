# from .competitor_a import method_a
# from .competitor_b import method_b

"""
This module defines a list of methods to be benchmarked. Each method is represented as a dictionary
containing its name, the function to be called, and any parameters required for execution.
This structure is used in utils/run_benchmarks.py to systematically benchmark each method. Method's output can vary based on the benchmark being run.
"""


def method_list():
    """
    Returns a list of methods to benchmark.
    Each method is represented as a dictionary with the following keys:
    - "name": A string representing the name of the method.
    - "function": A string representing the function to be called for the method.
    - "parameters": A dictionary of parameters to be passed to the function.
    """
    return [
        {"name": "", "function": "", "parameters": {}},
    ]
