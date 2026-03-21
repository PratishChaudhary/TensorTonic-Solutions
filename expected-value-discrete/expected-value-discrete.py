import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if np.allclose(np.array(p).sum(),1.0):
        return(np.sum(np.fromiter(((i*j) for i,j in zip(p,x)),dtype='float64')))
    else:
        raise ValueError