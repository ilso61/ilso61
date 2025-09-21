import os
import time
import csv
import re

print('Auto-disamber v1.2 by ilso61')
time.sleep(2)

file = input('ВВЕДИТЕ ИМЯ TXT ФАЙЛА\t')

with open(file, 'r', encoding='UTF-8', newline='') as f:
        text = f.readlines()
OR_amount = len(re.findall(r'\|',' '.join(text)))

with open('prep_num_disamb.py',"r",encoding="utf8") as f:
    exec(f.read())

with open('aggr_disamb.py',"r",encoding="utf8") as f:
    exec(f.read())
    
    
with open(file, 'r', encoding='UTF-8', newline='') as f:
    text = f.readlines()

print('\nКОЛИЧЕСТВО ЗНАКОВ "ИЛИ" ДО: ' + str(OR_amount))
print('КОЛИЧЕСТВО ЗНАКОВ "ИЛИ" ПОСЛЕ: ' + str(len(re.findall(r'\|',' '.join(text)))))
print('КОЛИЧЕСТВО ПУСТЫХ ФИГУРНЫХ СКОБОК: ' + str(len(re.findall(r'\{\}',' '.join(text)))))

try:
    os.rename('attr.mp4','attr.cfg')
    
except:
    os.rename('attr.cfg','attr.mp4')
    time.sleep(1)
    try:
        os.startfile('attr.mp4')
        print(' @@@   @@@   Ты лучший!!!!!!!!!!!!!!!!!!!!!!!')
        time.sleep(2)
        print('@@@@@ @@@@@  Ты лучшая!!!!!!!!!!!!!!!!!!!!!!!!!')
        time.sleep(2)
        print('@@@@@@@@@@@  You are the best!!!!!!!!!!!!!!!!!!!!')
        time.sleep(2)
        print(' @@@@@@@@@   Jesteś nailepszy!!!!!!!!!!!!!!!!!!!!!')
        time.sleep(2)
        print('  @@@@@@@    Jesteś nailepsza!!!!!!!!!!!!!!!!!!!!!')
        time.sleep(2)
        print('   @@@@@     Sei il migliore!!!!!!!!!!!!!!!!!!!!!')
        time.sleep(2)
        print('    @@@      Sei la migliore!!!!!!!!!!!!!!!!!!!')
        time.sleep(2)
        print('     @       Чахсының чахсызы полчазың!!!!!!!')
        print('Se avete degli errori, scrivetemi in VK\thttps://vk.com/id412243657')
        time.sleep(198)
        os.rename('attr.mp4','attr.cfg')

    except:
        os.rename('attr.mp4','attr.cfg')