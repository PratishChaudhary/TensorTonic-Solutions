def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    xf = x0
    for i in range(steps):
        derfx = 2*a*xf + b
        xf = xf - derfx*lr
    return round(xf,6)
