# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:48:17 2022

@author: yonau
"""

def fonction(x):
    return(x**3 -7*x**2 +8*x -3)

def f_prime(x):
    return(3*x**2-14*x+8)

def f_seconde(x):
    return(6*x-14)

def NR2(x0,epsilon):
    """
    La méthode de Newton Raphson2 permet de trouver la 
    solution de l'équation f'(x)=0 
    donc de trouver un optimum à f.

    Parameters
    ----------
    a : float 
        borne inférieure de l'intervalle
    b : float
        borne supérieure de l'intervalle 
    epsilon : float between 0 and 1
        valeur de epsilon

    Returns
    -------
    None.

    """
    x=[x0]
    n=0 #nb d'iterations
    while abs(f_prime(x[n]))>epsilon: 
        x.append(x[n]-(f_prime(x[n])/f_seconde(x[n])))
        n+=1
    print('Résultat obtenu au bout de n={0} itérations'.format(n))
    print('La solution optimale est : x*={0} et f(x*)={1}, obtenu avec une précision de {2}'.format(x[n],fonction(x[n]),epsilon))
    if f_seconde(x[n])<=0:
        print("Il s'agit d'un maximum local")
    else:
        print("Il s'agit d'un minimum local")

