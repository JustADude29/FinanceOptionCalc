from django.shortcuts import render
from django.http import HttpResponse

from math import *
import numpy as np
import scipy.stats as ss


def binomial_tree(S0, K, T, r, sigma, N, call_put):
    dt = T/N
    u = np.exp(sigma * np.sqrt(dt))
    d = np.exp(-sigma * np.sqrt(dt))
    print(u)
    print(d)
    p = (np.exp(r*dt) - d)/(u - d)
    print(p)
    c = 0
    for i in range(N+1):
        node_prob = comb(N, i)*(pow(p, i))*(pow((1-p), (N-i)))
        #node_prob = comb(N, i) * (p)**i * (1-p)**(N-i)
        ST = S0*(pow(u, i))*(pow(d, N-i))
        #ST = S0 * (u)**i * (d)**(N-i)
        if call_put == 'C':
            c += max(ST-K, 0) * node_prob
        elif call_put == 'P':
            c += max(K-ST, 0) * node_prob
        else:
            raise ValueError("Must be 'C' or 'P'")
    return round(c * np.exp(-r*T), 4)


def binomialIndex(request):
    return render(request, 'BinomialModel.html')


def Binomial(request, S, K, T, r, sigma, N, call_put):
    c = binomial_tree(float(S), float(K), float(T), float(r), float(sigma), int(N), str(call_put))
    r = HttpResponse(str(c))
    return r
