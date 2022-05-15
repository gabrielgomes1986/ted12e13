#Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão, 
# chame este dicionário de glossário.

from time import sleep
glossário={'RAM':' uma memória não permanente','ROM':' uma memória permanente','Linux':' um sistema operacional',
           'Processador':'um hardware que processa informações relacionadas ao computador','Cooler':'hardware que resfria o processador'}
for i in glossário:
    sleep(1)
    print('\n-----------------------------------------------------------------------------------')
    print(f'{i} é {glossário[i]}')
    