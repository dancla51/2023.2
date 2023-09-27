import numpy as np

# Deflate polynomial, with coefficents (ordered from highest to lowested)
# given by c, using a known root x.

# Returns the coefficients of the deflated polynomial, given previous
# coefficients c, and root x.
# Remainder R is the remainder after deflation: Up to rounding error, R
# will be zero if x is an exact root.
def deflate(c, x):
    R = c[0];
    c[0] = 0;
    for i in range(1,len(c)):
        q = c[i];
        c[i] = R;
        R = x*R + q;

    c = np.delete(c,0)
    
    if abs(R) > 10e-14:
        print(f'Root {x} may be inaccurate')

    return c, R