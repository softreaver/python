#!/usr/bin/python 
#-*- coding: UTF-8 -*-

from CompteSimple import CompteSimple
from CompteCourant import CompteCourant
from Titulaire import Titulaire

personne = Titulaire("MILAZZO", "Christopher", [CompteCourant(1500), CompteSimple(200), CompteSimple()])

personne.speak()
print("compte numéro 1 : " + str(personne.getCompte(1).getSolde()) + " euros.")
print("ajout de 150 euros sur le compte numéro 1")
personne.getCompte(1).credit(250)
personne.getCompte(1).debit(50)
personne.getCompte(1).debit(50)
print("compte numéro 1 : " + str(personne.getCompte(1).getSolde()) + " euros.")

personne.speak()

if isinstance(personne.getCompte(1), CompteCourant):
	print("historique du compte numéro 1 :")
	personne.getCompte(1).afficherHistorique()

