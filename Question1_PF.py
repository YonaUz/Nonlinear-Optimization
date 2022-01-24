# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 23:48:55 2022

@author: yonau
"""

import numpy as np

def fonction(x):
    return x**5 -5*x**3 -20*x +5

def signeplz(x,s,signe):
    """
    La fonction signeplz renvoie le sens d'exécution: 
    vers la droite ou vers la gauche. 
    
    """
    
    if signe == '+':
        #si on va dans le sens + (à droite) : x_i=x_(i-1)+s
        return x+s
    else:
        #si on va dans le sens -(à gauche): x_i=x_(i-1)-s
        return x-s
    
def pas_fixe(x0,s,optimum):
    """
    La fonction pas_fixe est une méthode d'optimisation qui permet de retourner 
    le point x_i (ou x*) qui peut être considéré comme point optimal.
    L'optimum peut être un point de maximisation ou de minimisation. 
    La fonction pas_fixe admet l'unimodalité de la fonction définie précédemment'
    
    INPUT x0: point de départ
    INPUT s: pas fixe 
    INPUT optimum: maximisation ou minimisation 
    OUTPUT table: tableau des itérations et résultat final de l'optimisation'
    
    """
    x = x0
    initilisation = fonction(x0+s)
    
    if optimum == 'mini':
        if initilisation < fonction(x0):
            signe = '+'
        else:
            signe = '-' 
    
    elif optimum == 'maxi':
        if initilisation < fonction(x0):
            signe = '-'
        else:
            signe = '+'
    
    liste_antecedants = []
    liste_images = []
    
    if optimum == 'mini':
        #pour une minimisation
        while fonction(signeplz(x,s,signe)) < fonction(x):
            liste_antecedants.append(x)
            liste_images.append(fonction(x))
            x = signeplz(x,s,signe) 
            
        liste_antecedants.append(x)
        liste_images.append(fonction(x))
        x = signeplz(x,s,signe)
        liste_antecedants.append(x)
        liste_images.append(fonction(x))
        i = liste_images.index(min(liste_images)) 
    
    elif optimum == 'maxi':
        #pour une maximisation
        while fonction(signeplz(x,s,signe)) > fonction(x):
            liste_antecedants.append(x)
            liste_images.append(fonction(x))
            x = signeplz(x,s,signe)
            
        liste_antecedants.append(x)
        liste_images.append(fonction(x))
        x = signeplz(x,s,signe)
        liste_antecedants.append(x)
        liste_images.append(fonction(x))
        i = liste_images.index(max(liste_images))
    
    table=np.zeros((len(liste_images),4))
    
        
    if optimum == 'mini':
        print('\n************ MINIMISATION: **********')
        #numpy ne permet pas le mélanchge des types str et float alors voici le nom des colonnes:
        #la derniere colonne sera le booléen 1 si vrai, 0 si faux
        print('\n','itération_i      ','x_i    ','f(x_i)   ','  f(x_i)>f(x_i)')
        for i in range(len(liste_images)):
            table[i,0]=i
            table[i,1]=liste_antecedants[i]
            table[i,2]=liste_images[i]
            ouinon=liste_images[i]>liste_images[i-1]
            table[i,3]=ouinon
    elif optimum == 'maxi':
        print('\n********** MAXIMISATION:*********')
        print('\n','itération_i     ','x_i      ','f(x_i)    ','  f(x_i)<f(x_i)')
        for i in range(len(liste_images)):
            table[i,0]=i
            table[i,1]=liste_antecedants[i]
            table[i,2]=liste_images[i]
            ouinon=liste_images[i]<liste_images[i-1]
            table[i,3]=ouinon
    print(table)
    
    if optimum == 'mini':
        print('Le {0}mum obtenu est {1} atteint en x_{2}={3}'.format(optimum,round(min(liste_images),3),i-1,round(liste_antecedants[i-1],3)))
    elif optimum == 'maxi':
       print('Le {0}mum obtenu est {1} atteint en x_{2}={3}'.format(optimum,round(max(liste_images),3),i-1,round(liste_antecedants[i-1],3)))
        
print('\nLa fonction f admet un minimum et un maximum.')     
         
pas_fixe(1,0.01,'mini')
pas_fixe(-3,0.01,'maxi')
        