import random

# Makes a guess g<N that shaares no factors with N
def guess(N):
    r = 1
    Nfact = factors(N)
    while True:
        Good = True
        g = random.randint(1, N-1)
        gfact = factors(g)
        for i in gfact:
            if i in Nfact:
                Good = False
        if Good == True:
            break
        
    while True:
        if pow(g, r)%N == 1:
            break
        r = r + 1

    if r%2 != 0:
        return guess(N)
    return r, g # r is the power at which g^r = m*N + 1

# Returns the two prime numbers, p1 and p2, from g^(r/2) + 1 and g^(r/2) - 1
def TwoPrime(r, g):
    p1 = (pow(g, r/2)) + 1
    p2 = (pow(g, r/2)) - 1
    return p1, p2

# Finds the greates common devisor of p and N
def gcd(p, N):
    if p%N != 0:
        return gcd(N, p%N)
    return N

# Returns a list of the factors of n
def factors(n):
    L = []
    for i in range(2, n+1):
        if n%i == 0:
            L.append(i)
    return L

def main():
    N = 77

    r, g = guess(N)                     
    p1, p2 = TwoPrime(r, g)
    ans1 = gcd(p1, N)
    ans2 = gcd(p2, N)

    print(ans1, ans2)

if __name__ == "__main__":
    main()
