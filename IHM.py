# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 17:52:41 2022

@author: yonau
"""

import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QWidget, QRadioButton, QLabel)

import Pas_Fixe, Pas_Accelere, Bissection,Newton_Raphson

class Accueil(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(600,200,697,392)
        self.setStyleSheet("background-color: mistyrose;")
        self.setWindowTitle('Accueil')
        self.texte = QLabel("Bienvenue dans mon IHM d'optimisation non linéaire. \nVous serez capable de réaliser des optimisations en choix libre ou selon les questions posées dans le CC. \nEnjoy ! \n\nYona UZAN")
        self.l1 = QLabel("Choisissez une question.") 
        self.choix1 = QRadioButton("Question 1")
        self.choix2 = QRadioButton("Question 2")
        self.choix3 = QRadioButton('Autre: autre fonction avec méthode de mon choix')
        self.go= QPushButton("Let's go")
        self.blanc = QLabel('\n\n')
        self.init_ui()
        
    def init_ui(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.texte)
        v_box.addWidget(self.blanc)
        v_box.addWidget(self.l1)
        v_box.addWidget(self.choix1)
        v_box.addWidget(self.choix2)
        v_box.addWidget(self.choix3)
        v_box.addWidget(self.blanc)
        v_box.addWidget(self.go)
        
        self.setLayout(v_box)
        self.show()
        self.go.clicked.connect(self.choisirsvp)
        
    def choisirsvp(self):
        if self.choix1.isChecked():
            self.suivant = Question1()
            self.suivant.show()
        if self.choix2.isChecked():
            self.suivant = Question2()
            self.suivant.show()
        if self.choix3.isCheckable():
            self.suivant = Question3()
            self.suivant.show()
            
class Question1(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Question 1')
        self.setGeometry(600,200,697,392)
        self.setStyleSheet("background-color: blanchedalmond;")
        self.l0 = QLabel("Bienvenue dans mon programme pour la question 1")
        self.l1 = QLabel("Choisissez la méthode que vous voulez utiliser : ")
        self.choix1 = QRadioButton("Pas fixe")
        self.choix2 = QRadioButton("Pas accéléré")
        self.ch3 = QRadioButton("Méthode de la bissection")
        self.go= QPushButton("GO !")
        self.blanc = QLabel('\n\n')
        self.init_ui()

    def init_ui(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.l0)
        v_box.addWidget(self.blanc)
        v_box.addWidget(self.l1)
        v_box.addWidget(self.choix1)
        v_box.addWidget(self.choix2)
        v_box.addWidget(self.ch3)
        v_box.addWidget(self.blanc)
        v_box.addWidget(self.go)
        
        self.setLayout(v_box)
        self.go.clicked.connect(self.methodechoisie)
        self.show()
    
    def methodechoisie(self):
        if self.choix1.isChecked():
            self.parameters = Alors('fixe')
        elif self.choix2.isChecked():
            self.parameters = Alors('accel')
        elif self.ch3.isChecked():
            self.parameters = Alors('bissec')
        self.parameters.show()
            

class Alors(QWidget):
    
    def __init__(self,method):
        super().__init__()
        self.method = method
        self.setGeometry(600,200,697,392)
        self.setStyleSheet("background-color: gainsboro;")
        self.setWindowTitle('Choix Minimisation / Maximisation')
        self.l0 = QLabel("Vous allez chercher des extremums de la fonction")
        self.l1 = QLabel("f(x)=x^5 -5x^3 -20x +5")
        self.blanc = QLabel('\n\n')
        self.extrem = QLabel("Vous souhaitez traiter quel optimum ?")
        self.min = QRadioButton('Minimum')
        self.min.setChecked(True)
        self.max = QRadioButton('Maximum')
        self.point_depart = QLabel('Chosissez votre point de départ :')
        self.depart = QLineEdit('0')
        self.blanc_depart=QLabel('                                                                                           ')
        self.pa = QLabel('Choisissez votre pas de départ :')
        self.pas = QLineEdit('0.05')
        self.prec = QLabel('Choisissez votre précision demandée (entre 0 et 1) :')
        self.preci = QLineEdit('0.1')
        self.inter = QLabel('Choisissez votre intervalle de départ sous forme de liste : ')
        self.interval1 = QLineEdit('0')
        self.interval2 = QLineEdit('5')
        self.calcul = QPushButton('Calculer')
        self.init_ui()
    
    def init_ui(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.l0)
        v_box.addWidget(self.l1)
        v_box.addWidget(self.blanc)
        v_box.addWidget(self.extrem)
        v_box.addWidget(self.min)
        v_box.addWidget(self.max)
        v_box.addWidget(self.blanc)
        
        h_1 = QHBoxLayout()
        h_1.addWidget(self.point_depart)
        h_1.addWidget(self.depart)
        h_1.addWidget(self.blanc_depart)
        
        h_2 = QHBoxLayout()
        h_2.addWidget(self.pa)
        h_2.addWidget(self.pas)
        h_2.addWidget(self.blanc_depart)
        
        h_3 = QHBoxLayout()
        h_3.addWidget(self.prec)
        h_3.addWidget(self.preci)
        
        h_inter = QHBoxLayout()
        h_inter.addWidget(self.inter)
        h_inter.addWidget(self.interval1)
        h_inter.addWidget(self.interval2)
        
        
        if self.method == 'bissec':
            v_box.addLayout(h_inter)
            v_box.addLayout(h_3)
        else:
            v_box.addLayout(h_1)
            v_box.addLayout(h_2)
            
        v_box.addWidget(self.blanc)
        v_box.addWidget(self.calcul)
        self.setLayout(v_box)
        
        self.calcul.clicked.connect(self.affiche)
    
    def affiche(self):
        x0 = float(self.depart.text())
        pas = float(self.pas.text())
        prec = float(self.preci.text())
        (a,b) = [float(self.interval1.text()),float(self.interval2.text())]
        
        if self.min.isChecked():
            ext = 'mini'
        elif self.max.isChecked():
            ext = 'maxi'
        
        if self.method == 'fixe':
            Pas_Fixe.pas_fixe(x0,pas,ext)
        elif self.method == 'accel':
            Pas_Accelere.pas_accelere(x0,pas,ext)
        else:
            Bissection.bissection(a,b,ext,prec)
            
class Question2(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(600,200,697,392)
        self.setStyleSheet("background-color: lavender;")
        self.setWindowTitle('Question 2')
        self.l0 = QLabel("Vous allez chercher des extremums de la fonction") 
        self.l3 = QLabel("x^3 -7x^2 +8x-3")
        self.l1 = QLabel('Sélectionnez le point de départ : ')   
        self.depart = QLineEdit('5')
        self.l2 = QLabel('Sélectionnez la précision désirée : ')
        self.prec = QLineEdit('0.01')
        self.calcul = QPushButton('Calculer')
        self.blanc = QLabel()
        self.init_ui()
        
    def init_ui(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.l0)
        v_box.addWidget(self.l3)
        
        h1 = QHBoxLayout()
        h1.addWidget(self.l1)
        h1.addWidget(self.depart)
        v_box.addLayout(h1)
        
        h2 = QHBoxLayout()
        h2.addWidget(self.l2)
        h2.addWidget(self.prec)
        v_box.addLayout(h2)
        
        v_box.addWidget(self.blanc)
        v_box.addWidget(self.calcul)
        self.setLayout(v_box)
        
        self.calcul.clicked.connect(self.affiche)
        
    def affiche(self):
        x0 = float(self.depart.text())
        prec = float(self.prec.text())
        Newton_Raphson.NR2(x0,prec)
        
class Question3(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,200,697,392)
        self.setStyleSheet("background-color: lightgreen;")
        self.setWindowTitle('Choix libre')
        self.l0 = QLabel("Vous allez chercher des extremums de la fonction") 
        self.l3 = QLabel("x^3 -7x^2 +8x-3")
        self.l1 = QLabel('Sélectionnez le point de départ : ')   
        self.depart = QLineEdit('5')
        self.l2 = QLabel('Sélectionnez la précision désirée : ')
        self.prec = QLineEdit('0.01')
        self.calcul = QPushButton('Calculer')
        self.blanc = QLabel()
        self.init_ui()
        
    def init_ui(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.l0)
        v_box.addWidget(self.l3)
        
        h1 = QHBoxLayout()
        h1.addWidget(self.l1)
        h1.addWidget(self.depart)
        v_box.addLayout(h1)
        
        h2 = QHBoxLayout()
        h2.addWidget(self.l2)
        h2.addWidget(self.prec)
        v_box.addLayout(h2)
        
        v_box.addWidget(self.blanc)
        v_box.addWidget(self.calcul)
        self.setLayout(v_box)
        
        self.calcul.clicked.connect(self.affiche)
        
    def affiche(self):
        x0 = float(self.depart.text())
        prec = float(self.prec.text())
        Newton_Raphson.NR2(x0,prec)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Accueil()
    sys.exit(app.exec_()) 