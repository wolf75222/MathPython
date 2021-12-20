#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# =============================================================================
# Romain.D 19/12/2021
# =============================================================================

from math import sqrt, degrees, atan, pi
import numpy as np
import matplotlib as plt
from mpl_toolkits import mplot3d


# =============================================================================
#  i² = -1
#  forme algébrique : z = a+ib (avec a;b -> réel)
#  forme trigo : z = |z|cos(teta)+isin(teta) (avec teta = arg(z))
#  forme expo : e(iteta) = cos(teta) + i sin(teta), z = |z|e(iteta)
# =============================================================================

class NBcomplexe():
    """
    La class des nombres complexes""
        a : partie réel du nombre complexe
        b : partie imaginaire du nombre complexe
    """
    def __init__(self, x = 0, y = 0):  #J'implémenterai l'appel avec un nombre complexe en paramètre qui permet ainsi la copie d'instances
        #assert isinstance(x, int or float or Fraction), "Attribut 'x' : doit être de type float ou int"
#        if x.__class__ is Fraction or y.__class__ is Fraction:
#            self.a = ....

        self.a = x
        self.b = y


    def __eq__(self,other): #Je te propose maintenant de toujours ajouter un jeu de test AVANT d'écrire le code
        """
        >>> NBcomplexe(1,2)==NBcomplexe(1,2)
        True
        >>> NBcomplexe(1,2)==NBcomplexe(1,3)
        False

        """
        return (self.a==other.a and self.b==other.b )#Il faudrait pouvoir faire NBcomplexe(1,0)==1


    def __str__(self):
        if self.a == 0 and self.b == 0:
            return f"0"
        if self.a == 0:
            return f"{self.b}i"
        if self.b == 0:
            return f"{self.a}"
        return f"{self.a} + {self.b}i"

    def __repr__(self):
        return f"NBcomplexe({self.a},{self.b})"#Modif GV

    def __add__(self, other):
        """
        >>> NBcomplexe(1,2)+(NBcomplexe(1,2)+2)+(2-NBcomplexe(1,2))
        NBcomplexe(5,6)
        """
        if other.__class__ is NBcomplexe:
            x = self.a + other.a
            y = self.b + other.b
            return NBcomplexe(x,y)
        elif other.__class__ is float or other.__class__ is int:#Je mettrai else il ne faut pas trop présumer des utilisations
            x = self.a * other
            y = self.b * other
            return NBcomplexe(x,y)
        else:
            return NotImplemented

    def __sub__(self, other):
        x = self.a - other.a
        y = self.b - other.b
        return NBcomplexe(x,y)

    def __mul__(self, other):
        x = self.a * other.a - self.b * other.b
        y = self.a * other.b + self.b * other.a
        return NBcomplexe(x,y)

    def __truediv__(self, other):
        if other.a * other.a + other.b * other.b != 0:
            x = (self.a * other.a + self.b * other.b) / (other.a * other.a + other.b * other.b)
            y = (self.b * other.a - self.a * other.b) / (other.a * other.a + other.b * other.b)
            return NBcomplexe(x,y)
        else:
            return f"Le dénominateur est zéro !"#plutôt en début de code un assert other!=0

    def module(self):#ou abs
        return  sqrt( self.a * self.a + self.b * self.b)

    def arg(self):#il manque une gestion d'erreur
        return degrees(atan(self.b / self.a)) * pi/180

    def conjuge(self):
        x = self.a
        y = self.b * -1
        return NBcomplexe(x,y)#On doit bouvoir écrire return NBcomplexe(self.x,-self.y)

    def affiche(self):#Implémenter plutôt l'affichage d'une LISTE de complexes
        """
        Affiche Le nombre complex dans un graphique matplotlib tel que : x = la partie reel ; y = partie imaginaire
        """
        x = self.a
        y = self.b
        plt.plot(x,y, color='green', marker='+')
        plt.grid()
        plt.title(("Affichage de {}").format(str(NBcomplexe(self.a, self.b))))


# =============================================================================
z1=NBcomplexe(1,1)   #A intégrer dans les tests des fonctions
assert z1==z1
assert z1+z1==NBcomplexe(2,2)
assert z1*z1==NBcomplexe(0,2)
assert z1.conjuge()==NBcomplexe(1,-1)
assert z1.arg()==0.7853981633974483
assert z1.module()==1.4142135623730951
assert str(z1-z1)==f"0"


if __name__ == "__main__":
    import doctest
    doctest.testmod()#Pour tester les docString

    z1=NBcomplexe(1,1)
    z2=NBcomplexe(2,1)
    print(f"{z1} * {z2} = {z1*z2}")
    print(f"{z1} + {z2} = {z1+z2}")
    print(f"{z1} - {z2} = {z1-z2}")
    print(f"{z1} / {z2} = {z1/z2}")
    #z3=NBcomplexe( Fraction(1,2),1)
    #z4=NBcomplexe( 1,Fraction(1,3))
    #print(f"{z3} * {z4} = {z3*z4}")
    #print(f"{z3} + {z4} = {z3+z4}")
    #print(f"{z3} - {z4} = {z3-z4}")
    #print(f"{z3} / {z4} = {z3/z4}")








