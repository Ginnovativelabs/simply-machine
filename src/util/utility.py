import numpy as np
import numbers


def checksum(array: np.ndarray) -> int:
    """Calculate the checksum of a numpy array."""
    return sum(hash(x) for x in array.flat) % (2**32)

def cal_var(array: np.ndarray,confidence: float) -> dict:
    """Calculate the quartile quantile of the numpy array."""
    array_int=[i for i in array if isinstance(i, numbers.Number)]
    quartile=[np.percentile(array_int, 25), np.percentile(array_int, 50), np.percentile(array_int, 75)]
    return {"Q1": quartile[0], "Q2": quartile[1], "Q3": quartile[2]}

def std(array: np.ndarray) -> float:
    """Calculate the standard deviation of a numpy array."""
    array_int=[i for i in array if isinstance(i, numbers.Number)]
    return np.std(array_int)
