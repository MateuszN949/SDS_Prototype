"""
Core model implementation.

This module contains the reference implementation of the
Linear Transformation Network described in the associated paper.
"""


class LinearTransformModel:
    """
    Simple linear transformation model.

    Computes:

        y = a * x + b

    Attributes:
        coefficient: Multiplication factor.
        bias: Additive offset.
    """

    def __init__(self, coefficient: float, bias: float) -> None:
        """
        Initialize the model.

        Args:
            coefficient: Multiplication factor.
            bias: Additive offset.
        """
        self.coefficient = coefficient
        self.bias = bias

    def predict(self, value: float) -> float:
        """
        Transform a single input value.

        Args:
            value: Input value.

        Returns:
            Transformed value.
        """
        return self.coefficient * value + self.bias