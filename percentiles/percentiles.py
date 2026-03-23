import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.sort(x)
    return (np.percentile(a=x,q=q,method='linear'))
    pass