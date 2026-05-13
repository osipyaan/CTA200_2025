def comp_calc(c, max_iter=100, escape_radius=2):
    """
    Outputs ODEs for the behaviour of the Earth's atmosphere at (X, Y, Z).
    
    inputs: t ------- float, time, required for solve_ivp
            w ------- array, current values, [X, Y, Z]
            s ------- float, the Prandtl number
            r ------- float, the Rayleigh number
            b ------- float, dimensionless length scale
            
    outputs: dW ----- array, [dXdt, dYdt, dZdt]
    
    """
    z = 0
    for n in range(max_iter):
        z = z**2 + c
        if abs(z) > escape_radius:
            return n  #diverge at iteration n
    return max_iter  #bounded