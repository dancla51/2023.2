# Horner evaluate polynomial and its first two derivatives.
# Returns the value at x of a polynomial, defined by coefficients c.
# p0x=P(x), together with its derivatives p1x=P'(x) and p2x=P''(x).
# c is a vector of length n+1 whose elements are the coefficients of
# the polynomial in descending powers:
#     P(x) = c[0]*x^n + c[1]*x^(n-1) + ... + c[n-1]*x + c[n]
def horner(c, x):
    p0x = c[0]
    p1x = 0
    p2x = 0
    for i in range(1,len(c)):
        p2x = x*p2x + p1x
        p1x = x*p1x + p0x
        p0x = x*p0x + c[i]
    p2x = 2*p2x

    return p0x, p1x, p2x