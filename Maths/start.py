#!/usr/bin/python
#coding: UTF-8

from Polynome import Polynome

pol1 = Polynome((1, 2, 3, 4, 0, 6))
pol2 = Polynome((2, 1, 0, -1, 3))
print(pol1 + pol2)
print(pol1)
pol1 += pol2
print(pol1)


