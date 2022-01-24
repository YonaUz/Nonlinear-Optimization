# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:53:15 2022

@author: yonau
"""

import pandas as pd
import numpy as np

def fonction(x):
    return x**5 -5*x**3 -20*x +5

def bissec(a,b,epsilon,optimum):
    """
    Parameters
    ----------
    a : float
        borne inférieure de l'intervalle de départ
    b : float
        borne supérieure de l'intervalle de départ
    epsilon : float between 0 and 1
        précision souhaitée
    optimum : string 
        minimisation ou maximisation

    Returns
    -------
    a
    b

    """
    
    x0=(a+b)/2
    x1=(a+x0)/2
    x2=(x0+b)/2
    f0 = fonction(x0)
    f1 = fonction(x1)
    f2 = fonction(x2)
    if optimum == 'mini':
        if f2>f0 and f0>f1:
            #f2>f0>f1 donc [a,x0]
            b=x0
        elif f2<f0 and f0<f1:
            #f2<f0<f1 donc [a,x0]
            a=x0
        elif f1>f0 and f2>f0:
            #[x1,x2]
            a=x1
            b=x2
    elif optimum == 'maxi':
        if f2>f0 and f0>f1:
            #f2>f0>f1 donc [a,x0]
            a=x0
        elif f2<f0 and f0<f1:
            #f2<f0<f1 donc [a,x0]
            b=x0
        elif f1>f0 and f2>f0:
            #[x1,x2]
            if f1==max(f1,f2):
                #[a,x1]
                b=x1
            else:
                #[x2,b]
                a=x2
    return(a,b)

        
def bissection(a,b,optimum,epsilon):
    """
    La méthode de la bissection est un cas particulier de la méthode 
    dichotomique. Exactement la moitié de l’intervalle d’incertitude
    actuel est supprimé à chaque étape. 
    
    Parameters
    ----------
    a : float
        borne inférieure de l'intervalle de départ
    b : float
        borne supérieure de l'intervalle de départ
    epsilon : float between 0 and 1
        précision souhaitée
    optimum : string 
        minimisation ou maximisation

    Returns
    -------
    None.

    """
    liste_a=[]
    liste_b=[]
    while (b-a)>epsilon:
        (a,b)=bissec(a,b,epsilon,optimum)
        liste_a.append(a)
        liste_b.append(b)
    if optimum == 'mini':
        print('\n************ MINIMISATION: **********')
    elif optimum == 'maxi':
        print('\n********** MAXIMISATION:*********')
        
    table=np.zeros((len(liste_a),2))
    print('   a       b')
    for i in range(len(liste_a)):
        table[i,0]=liste_a[i]
        table[i,1]=liste_b[i]
    print(table)
    print("Le {0}mum a été trouvé dans l'intervalle [{1},{2}] et le point médian optimum x* est x*={3}".format(optimum,a,b,(a+b)/2))
    print("f(x*)={0}".format(fonction((a+b)/2)))

bissection(0,5,'mini',0.1)
bissection(-4,-1,'maxi',0.1)