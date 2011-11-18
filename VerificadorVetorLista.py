#!/usr/bin/env python
# _*_ coding: utf-8 -*_

from array import array
import unittest


class VerificaLista(object):

    def __init__ (self,x1,x2,x3,x4,x5):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5

    def lista(self):
             
        lista = [self.x1,self.x2,self.x3,self.x4,self.x5]
     
        if (self.x1 < self.x2) & (self.x2<self.x3) & (self.x3< self.x4) & (self.x4 < self.x5):
            print " a lista passada esta ordenado ordem crescente"
            #20,21,22,23,25
        if (self.x1 > self.x2) & (self.x2>self.x3) & (self.x3> self.x4) & (self.x4 > self.x5):
        # 20 , 19, 18 ,17,16
            print "a lista passada esta ordem decrescente"
        if (self.x1 == self.x2) & (self.x2 == self.x3) & (self.x3 == self.x4) & (self.x4 == self.x5):
            print "todos elementos possuem o mesmo numero"
        else:
            print "esta desordenado"
        return lista

    def soma(self):

        #lista = [self.x1,self.x2,self.x3,self.x4,self.x5]
        soma = self.x1 + self.x2 + self.x3 + self.x4 + self.x5
        return soma

        
   
#listaOrdenada = [1,2,3,4,5]
#listaDesordenada= [90,2,34,89,56]
#listaCrescente= [30,50,60,89,90] 


if __name__ == '__main__':
    print "================================================"
    print "RESULTADOS "
    print "================================================"
    #print "Lista desordenada"
    v = VerificaLista (2,10,2,5,2)
    print v.lista()
    print "================================================"
    #print " lista ordenada"
    v = VerificaLista(1,2,3,4,5)
    print v.lista()
    print "================================================"
    #verificarListasOrdenacao()


