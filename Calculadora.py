import math

class SolNum:

    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.num3 = None
       

    def valores(self):

        while self.num1 == None:
            
            try:
                self.num1 = float(input("Ingrese el primer número: "))
                           
            except ValueError:

                print ("El valor ingresado no es numérico, intente de nuevo")
        while self.num2 == None:
            
            try:
                self.num2 = float(input("Ingrese el segundo número: "))
                           
            except ValueError:

                print ("El valor ingresado no es numérico, intente de nuevo")
    
    def operacion(self):

        opc=input("Escriba la operación a realizar: \nsuma \nresta \nmultiplica \ndivide \n")
        opc1= opc.lower()

        if (opc1 == "suma"):
            self.num3 = self.num1 + self.num2
            print("El resultado de la",opc1, "es:", self.num3)
            """ return self.num3 """         
        elif (opc1 == "resta"):
            self.num3 = self.num1 - self.num2
            print("El resultado de la",opc1, "de", self.num1, "-", self.num2, "es:", self.num3)
            """ return self.num3 """
        elif (opc1 == "multiplica"):
            self.num3 = self.num1 * self.num2
            print("El resultado de la multiplicación es:", self.num3)
            """ return self.num3 """
        elif (opc1 == "divide"):
            try: 
                self.num3 = self.num1 / self.num2
                print("El resultado de la división de", self.num1, "en", self.num2, "es:", self.num3)
                """" return self.num3 """
            except ZeroDivisionError:
                print("No se puede dividir un número en cero")
                """ gsg.valores() """
               
        else:
            print("No se ha seleccionado operación")

      
miCal=SolNum()
miCal.valores()
miCal.operacion()
""" print(operacion()) """
"""como vuelvo a solicitar el número """
print("Fin del proceso")
#prueba actualización