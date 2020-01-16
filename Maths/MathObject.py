#!/usr/bin/python
#coding: UTF-8
import abc

class MathObject(abc.ABC):
    @abc.abstractmethod
    def __str__(this):
        pass
        
    @abc.abstractmethod
    def __add__(this, other):
        pass
    
    @abc.abstractmethod    
    def __sub__(this, other):
        pass
    
    @abc.abstractmethod    
    def __truediv__(this, other):
        pass
    
    @abc.abstractmethod    
    def __mul__(this, other):
        pass
    
    @abc.abstractmethod
    def __iadd__(this, other):
        pass
    
    @abc.abstractmethod    
    def __isub__(this, other):
        pass
    
    @abc.abstractmethod    
    def __itruediv__(this, other):
        pass
    
    @abc.abstractmethod    
    def __imul__(this, other):
        pass        

