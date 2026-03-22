import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    total = len(y)
    unique_vals, counts = np.unique(y, return_counts=True)
    proba = counts / total
    if (proba == 1).any():
      return -0.0

    E = -np.sum(proba * np.log2(proba))
    return E

