#!/usr/bin/python
#coding: UTF-8

from MathObject import MathObject

class Polynome(MathObject):
	_coefList = ()

	def __init__(this, coefList):
		this._coefList = coefList
		
	def __str__(this):
		return this.getDisplay()
	
	def getDisplay(this):
		polynomeForme = ''
		for i, coef in enumerate(this._coefList):
			if i > 0:
				polynomeForme += ' + '
			polynomeForme += str(coef) + "x^" + str(i)
		return polynomeForme

	def __add__(this, other):
		foncteur = lambda op1, op2: op1 + op2
		return Polynome(this._op(this.getCoefs(), other.getCoefs(), foncteur))

	def __sub__(this):
		foncteur = lambda op1, op2: op1 - op2
		return Polynome(this._op(this.getCoefs(), other.getCoefs(), foncteur))
		
	def __truediv__(this):
		foncteur = lambda op1, op2: op1 / op2
		return Polynome(this._op(this.getCoefs(), other.getCoefs(), foncteur))
		
	def __mul__(this):
		foncteur = lambda op1, op2: op1 * op2
		return Polynome(this._op(this.getCoefs(), other.getCoefs(), foncteur))
		
	def __iadd__(this, other):
		foncteur = lambda op1, op2: op1 + op2
		this._coefList = this._op(this.getCoefs(), other.getCoefs(), foncteur)
		return this

	def __isub__(this):
		foncteur = lambda op1, op2: op1 - op2
		this._coefList = this._op(this.getCoefs(), other.getCoefs(), foncteur)
		return this
		
	def __itruediv__(this):
		foncteur = lambda op1, op2: op1 / op2
		this._coefList = this._op(this.getCoefs(), other.getCoefs(), foncteur)
		return this
		
	def __imul__(this):
		foncteur = lambda op1, op2: op1 * op2
		this._coefList = this._op(this.getCoefs(), other.getCoefs(), foncteur)
		return this

	def getCoefs(this):
		return this._coefList
		
	def _op(this, t1, t2, foncteur):
		newCoefs = []
		if len(t2) > len(t1):
			newCoefs = this._op(t2, t1, foncteur)
		else:
			for i, coef in enumerate(t1):
				op1 = coef
				op2 = 0
				if len(t2) > i:
					op2 = t2[i]
				result = foncteur(op1, op2)
				newCoefs.append(result)
		
		return tuple(newCoefs)
	
