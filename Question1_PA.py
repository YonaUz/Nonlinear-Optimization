# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 00:07:36 2022

@author: yonau
"""
import numpy as np

def fonction(x):
    return x**5 -5*x**3 -20*x +5
    
def pas_accelere(x0,s0,optimum):
    """
    La fonction pas_accelere est une méthode d'optimisation qui permet de retourner 
    le point x_i (ou x*) qui peut être considéré comme point optimal.
    L'optimum peut être un point de maximisation ou de minimisation. 
    La fonction pas_accelere admet l'unimodalité de la fonction définie précédemment'
    
    INPUT x0: point de départ
    INPUT s0: pas de départ 
    INPUT optimum: maximisation ou minimisation 
    OUTPUT table: tableau des itérations et résultat final de l'optimisation'
    
    """
    x = x0
    initilisation = fonction(x0+s0)
    
    if optimum == 'mini':
        #pour une minimisation
        if initilisation < fonction(x0):
            signe = '+'
        else:
            signe = '-' 
    
    elif optimum == 'maxi':
        #por une maximisation 
        if initilisation < fonction(x0):
            signe = '-'
        else:
            signe = '+'
            
    liste_antecedants = []
    liste_images = []
    liste_s=[]
    liste_antecedants.append(x0)
    liste_images.append(fonction(x0))
    liste_s.append(s0)
    i = 0
    
    if optimum == 'mini':
        if signe== '+':
            while fonction(x0+(s0*2**(i+1))) < fonction(x0+(s0*2**i)):
                x=x0+(s0*2**(i+1))
                liste_antecedants.append(x)
                liste_images.append(fonction(x))
                liste_s.append(s0*2**(i+1))
                i+=1
            #on ajoute les derniers pour marquer le changement 
            liste_antecedants.append(x0+(s0*2**(i+1)))
            liste_images.append(fonction(x0+(s0*2**(i+1))))
            liste_s.append(s0*2**(i+1))
        else: 
            while fonction(x0-(s0*2**(i+1))) < fonction(x0-(s0*2**i)):
                x=x0-(s0*2**(i+1))
                liste_antecedants.append(x)
                liste_images.append(fonction(x))
                liste_s.append(s0*2**(i+1))
                i+=1
            #on ajoute les derniers pour marquer le changement 
            liste_antecedants.append(x0-(s0*2**(i+1)))
            liste_images.append(fonction(x0-(s0*2**(i+1))))
            liste_s.append(s0*2**(i+1))
        i = liste_images.index(min(liste_images)) 
        
    elif optimum == 'maxi':
        if signe== '+':
            while fonction(x0+(s0*2**(i+1))) > fonction(x0+(s0*2**i)):
                x=x0+(s0*2**(i+1))
                liste_antecedants.append(x)
                liste_images.append(fonction(x))
                liste_s.append(s0*2**(i+1))
                i+=1
            #on ajoute les derniers pour marquer le changement 
            liste_antecedants.append(x0+(s0*2**(i+1)))
            liste_images.append(fonction(x0+(s0*2**(i+1))))
            liste_s.append(s0*2**(i+1))
            
        else: 
            while fonction(x0-(s0*2**(i+1))) > fonction(x0-(s0*2**i)):
                x=x0-(s0*2**(i+1))
                liste_antecedants.append(x)
                liste_images.append(fonction(x))
                liste_s.append(s0*2**(i+1))
                i+=1
            #on ajoute les derniers pour marquer le changement 
            liste_antecedants.append(x0-(s0*2**(i+1)))
            liste_images.append(fonction(x0-(s0*2**(i+1))))
            liste_s.append(s0*2**(i+1))
        i = liste_images.index(max(liste_images))
            
    table=np.zeros((len(liste_images),5))
    
    if optimum == 'mini':
        print('\n************ MINIMISATION: **********')
        #numpy ne permet pas le mélanchge des types str et float alors voici le nom des colonnes:
        #la derniere colonne sera le booléen 1 si vrai, 0 si faux
        print('\n','     i   ','        s','        x_i    ','     f(x_i) ','     f(x_i)>f(x_i)')
        for i in range(len(liste_images)):
            table[i,0]=i
            table[i,1]=liste_s[i]
            table[i,2]=liste_antecedants[i]
            table[i,3]=liste_images[i]
            ouinon=liste_images[i]>liste_images[i-1]
            table[i,4]=ouinon
    elif optimum == 'maxi':
        print('\n********** MAXIMISATION:*********')
        print('\n','     i   ','        s','        x_i    ','     f(x_i) ','     f(x_i)<f(x_i)')
        for i in range(len(liste_images)):
            table[i,0]=i
            table[i,1]=liste_s[i]
            table[i,2]=liste_antecedants[i]
            table[i,3]=liste_images[i]
            ouinon=liste_images[i]<liste_images[i-1]
            table[i,4]=ouinon
    print(np.round(table,3))
    
    if optimum == 'mini':
        print('Le {0}mum obtenu est {1} atteint en x_{2}={3}'.format(optimum,round(min(liste_images),3),i-1,round(liste_antecedants[i-1],3)))
    elif optimum == 'maxi':
       print('Le {0}mum obtenu est {1} atteint en x_{2}={3}'.format(optimum,round(max(liste_images),3),i-1,round(liste_antecedants[i-1],3)))
    
    
print('\nLa fonction f admet un minimum et un maximum.') 

pas_accelere(0, 0.1, 'mini')
pas_accelere(0, 0.1, 'maxi') 