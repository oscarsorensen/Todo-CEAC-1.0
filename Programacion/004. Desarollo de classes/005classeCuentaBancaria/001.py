

limitediferenciasaldo = 1000

class CuentaBancaria():
    def __init__(self):
        self.__saldo = 0
        self.__cliente = ""
#Definir setters y getters para el saldo y el cliente
    def setSaldo(self, nuevosaldo):
        #establezco una condicion de que valida si el saldo nuevo es mayor de 100 euros
        if nuevosaldo > self.__saldo + 100:
            #si salta la alarma, avisa y no cambia el saldo
            print("Voy a avisar a la entidad de un ingreso my grande")
        else:
            #si pasa el filtro, solo entonces se cambia el saldo
            self.__saldo = nuevosaldo
        
    def getSaldo(self):
        return self.__saldo
    
cuentacliente1 = CuentaBancaria()
cuentacliente1.setSaldo(10000000)
print(cuentacliente1.getSaldo())