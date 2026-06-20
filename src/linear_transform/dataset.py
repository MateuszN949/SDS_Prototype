"""
Dataset utilities.
"""

from pathlib import Path


def load_dataset(path: str) -> list[float]:
    """
    Load numeric values from a text file.

    The file should contain one floating-point value per line.

    Args:
        path: Path to the dataset file.

    Returns:
        List of loaded values.

    Raises:
        FileNotFoundError:
            If the file does not exist.

        ValueError:
            If a line cannot be parsed as a float.
    """

    dataset_path = Path(path)

    with dataset_path.open("r", encoding="utf-8") as file:
        return [float(line.strip()) for line in file]