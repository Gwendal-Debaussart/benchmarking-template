# from .dataset_name import load_your_dataset_here

def dataset_list():
    """
    Returns a dictionary of available datasets and their loading functions.

    :return: dict,
        A dictionary where keys are dataset names and values are functions to load them.
    """
    return {
        "dataset_name": lambda **args: ([], []),  # Replace with actual loading function
    }


def load_dataset(name: str, **args):
    """
    Load a dataset by name.

    :param name: str
        Name of the dataset to load.
    :param args: dict
        Additional arguments to pass to the dataset loading function.

    :return: tuple
        The loaded dataset, typically as (X, Y) or (list_views, true_labels).
    """
    datasets = dataset_list()
    ## Change here typically to add preprocessing steps after loading if needed
    if name in datasets:
        return datasets[name](**args)
    else:
        raise ValueError(f"Dataset '{name}' is not recognized.")