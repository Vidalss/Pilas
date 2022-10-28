#Escribir un programa que, haciendo uso de una pila, procese cada uno de los
#caracteres de una expresion que viene dada en una línea. La finalidad es
#verificar el equilbrio de paréntesis, llaves y corchetes. Por ejemplo:
#La siguiente expresión tiene un número de paréntesis equilibrado ((a+b)*6) -7
#A esta otra expresión le falta un corchete: [(a+b/2.5) + x -7
from Pila import *

class BalanceParentesis:
    __linea = ""

    def balancear(self, linea):
        self.__linea = linea
        pila = PilaDinamica()
        #quitar espacios
        elementos = list(self.__linea)
        for x in elementos:
            if (x == '(' or x == '[' or x == '{'):
                pila.push(x)
            if (x == ')' or x == ']' or x == '}'):
                apertura = ord(pila.pop())
                cierre = ord(x)
                if (cierre - apertura > 2 ):
                    return "Error de parentesis"
        print(pila.stackempty())
        if not (pila.stackempty()):
            return "Falta cerrar un corchete, una llave o un parentesis"
        else:
            return "Correcto"



if __name__==  '__main__':
    balance = BalanceParentesis()
    linea = input()
    print(balance.balancear(linea))