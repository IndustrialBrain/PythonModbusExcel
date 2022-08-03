
import pandas as pd
import numpy as np
from pyModbusTCP.client import ModbusClient
import time

# Inicia configuração TCP
c = ModbusClient(host="192.168.0.239", port=502, unit_id=1, auto_open=True)
# Parametros conexão
c = ModbusClient()
regs=[1,0,0,0]




def Modbus():
    # Abre conexão TCP
    c.open()

    #Leitura de 5 registros a partir do 40001
    regs = c.read_holding_registers(0, 5)
    if regs:
        print(regs)
        if regs[4]==1:
            try:
                escrita(regs)
                if c.write_multiple_registers(4, [0]):
                    print("write ok")
                else:
                    print("write error")
            except:
                print ("Falha na escrita")
            
    else:
        print("read error")
    #Fecha conexão    
    c.close()



def escrita(regs):
    # Create multiple lists
    OrdemProducao=[regs[0]]
    PecasProduzidas =  [regs[1]]
    TempoParada = [regs[2]]
    Rejeito = [regs[3]]
    columns=['OrdemProducao','PecasProduzidas','TempoParada','Rejeito']

    df = pd.DataFrame(list(zip(OrdemProducao,PecasProduzidas,TempoParada,Rejeito)), columns=columns)
    df.to_excel('Prod.xlsx', index=False)   


try:
    while True:  
        Modbus()
        time.sleep(5)

except:
    print ("Falha de Leitura")
    c.close()


