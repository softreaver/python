#!/usr/bin/python 
#-*- coding: UTF-8 -*-

from CompteSimple import CompteSimple

class Titulaire:
    _nom = ""
    _prenom = ""
    _comptes = 0

    def __init__(this, nom, prenom, comptes):
        this._nom = nom
        this._prenom = prenom
        this._comptes = comptes

    def speak(this):
        print("Bonjour je m'appel " + this._nom + " " + this._prenom + " et j'ai un total de " + str(len(this._comptes)) + " comptes totalisant un solde de " + str(this.getTotalSolde()) + " euros.")

    def getTotalSolde(this):
        total = 0
        for compte in this._comptes:
            total += compte.getSolde()

        return total

    def getCompte(this, nCompte):
        if nCompte > len(this._comptes):
            raise ValueError("Le compte numéro " + str(nCompte) + " n'existe pas !")
        else:
            return this._comptes[nCompte - 1]

    def ajoutCompte(this, compte):
        assert isinstance(compte, CompteSimple)
        this._comptes.append(compte)

    def supprimeCompte(this, nCompte):
        this._comptes.remove(this.getCompte(nCompte))


