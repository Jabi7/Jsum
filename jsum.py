def jsum(f, a, b, t = 0, tol = 0.00001):
    m  = (a+b)/2
    s =  (f(a) - t + f(m) - t) * abs(b-a)/2
    if abs(b-a) < tol/2:
        return 0
    s = s + jsum(f, a, m, f(a)) + jsum(f, m, b, f(m))
    return s
    
