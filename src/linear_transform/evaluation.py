"""
Evaluation utilities.
"""

from .model import LinearTransformModel


def mean_prediction(
    model: LinearTransformModel,
    values: list[float],
) -> float:
    """
    Compute the mean prediction over a dataset.

    Args:
        model: Model used for prediction.
        values: Input values.

    Returns:
        Average prediction value.
    """

    predictions = [
        model.predict(value)
        for value in values
    ]

    return sum(predictions) / len(predictions)