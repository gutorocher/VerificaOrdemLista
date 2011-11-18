import unittest
from VerificadorVetorLista import VerificaLista


class TesteClass(unittest.TestCase):
   
    def setUp(self):
        ''' definicao dos parametro do objeto'''
        self.v1 = VerificaLista(2,2,2,2,2) #iguais
        self.v2 = VerificaLista(1,2,3,4,5) # crescente
        self.v3 = VerificaLista(90,2,34,89,56) # desordenado
        self.v4 = VerificaLista(90,80,70,60,50) #decrescente

  
    #teste 1
    def test_obj(self):
        ''' testa se existe o objeto r'''
        self.assertTrue(self.v1)
        print ". objeto existe"

    #teste2
    def teste_Lista(self):
        ''' teste se o objeto e o metodo existe'''
        self.assertTrue(self.v1.lista())

    #teste 3
    def teste_resultaodo_lista_iguais(self):
        ''' teste o resultado '''
        lista = [2,2,2,2,2]
        self.assertEqual(self.v1.lista(),lista)
    
    #teste 4
    def teste_resultado_crescente(self):
        lista =[1,2,3,4,5]
        self.assertEqual(self.v2.lista(),lista)

    #teste 5
    def teste_desordenado(self):
        lista =[90,2,34,89,56]
        self.assertEqual(self.v3.lista(),lista)

    #teste 6
    def teste_resultado_decrescente(self):
        lista = [90,80,70,60,50]
        self.assertEqual(self.v4.lista(),lista)


    #teste 7
    def teste_soma(self):
        ''' teste de somar'''
        self.assertEqual(self.v1.soma(),10)




   
        
# executa teste
if __name__ == '__main__':
    unittest.main()

   
