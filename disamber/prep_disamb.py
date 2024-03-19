#import os
#os.chdir('C:/Users/ilso61/Desktop/1st_grade/python')

import time
import argparse
import csv
import re

def replace_with(string, span, repl):
    begin, end = span
    return string[:begin] + repl + string[end:]

sep = '|'

file = input('ВВЕДИТЕ ИМЯ TXT ФАЙЛА\t')
with open(file, 'r', encoding='UTF-8', newline='') as f:
        text = f.readlines()
OR_amount = len(re.findall('\|',' '.join(text)))

with open(file, 'r', encoding='UTF-8', newline='') as f:
        word_morph = list(csv.reader(f, delimiter='\t'))
row_num = -1
for row in word_morph :
    row_num = row_num + 1
    row[2] = re.sub('{э=S,сокр=[^}]+?}', '{э=INTJ=}', row[2])
    row[2] = re.sub('{ц=S,сокр=[^}]+?}', '{ц=INTJ=}', row[2])
    row[2] = re.sub('{ф=S,сокр=[^}]+?}', '{ф=INTJ=}', row[2])
    row[2] = re.sub('{о=S,сокр=[^}]+?}', '{о=INTJ=}', row[2])
    row[2] = re.sub('{мм=S,.+?}', '{мм=INTJ=}', row[2])
    row[2] = re.sub('{в=S,сокр=[^}]+?}', '{в=PR=}', row[2])
    row[2] = re.sub('{у=S,сокр=[^}]+?}', '{у=PR=}', row[2])
    row[2] = re.sub('{с=S,сокр=[^}]+?}', '{с=PR=}', row[2])
    row[2] = re.sub('{к=S,сокр=[^}]+?}', '{к=PR=}', row[2])
    row[2] = re.sub('{о=S,сокр=[^}]+?}', '{о=PR=\|о=INTJ=}', row[2])
    row[2] = re.sub('{а=S,сокр=[^}]+?}', '{а=PR=\|а=INTJ=}', row[2])
    row[2] = re.sub('{[А-я]=INTJ=}-', '-', row[2])
    row[2] = re.sub('{[А-я]=PR=}-', '-', row[2])
    row[2] = re.sub('}-в{в=PR=}', '}-в', row[2])
    row[2] = re.sub('}-у{у=PR=}', '}-у', row[2])
    row[2] = re.sub('}-с{с=PR=}', '}-с', row[2])
    row[2] = re.sub('}-к{в=PR=}', '}-к', row[2])
    row[2] = re.sub('-к{к=PR=}', '-к', row[2])
    row[2] = re.sub('Ничё{[^}]+?}', 'Ничё{ничто=SPRO,ед,сред=род}', row[2])
    row[2] = re.sub('ничё{[^}]+?}', 'ничё{ничто=SPRO,ед,сред=род}', row[2])
    row[2] = re.sub('Чё{[^}]+?}-нить{[^}]+?}', 'Чё-нить{что-нибудь=SPRO,ед,сред,неод=вин|что-нибудь=SPRO,ед,сред,неод=им|что-нибудь=SPRO,ед,сред,неод=род}', row[2])
    row[2] = re.sub('чё{[^}]+?}-нить{[^}]+?}', 'чё-нить{что-нибудь=SPRO,ед,сред,неод=вин|что-нибудь=SPRO,ед,сред,неод=им|что-нибудь=SPRO,ед,сред,неод=род}', row[2])
    row[2] = re.sub('Чё{[^}]+?}-нибудь{[^}]+?}', 'Чё-нибудь{что-нибудь=SPRO,ед,сред,неод=вин|что-нибудь=SPRO,ед,сред,неод=им|что-нибудь=SPRO,ед,сред,неод=род}', row[2])
    row[2] = re.sub('чё{[^}]+?}-нибудь{[^}]+?}', 'чё-нибудь{что-нибудь=SPRO,ед,сред,неод=вин|что-нибудь=SPRO,ед,сред,неод=им|что-нибудь=SPRO,ед,сред,неод=род}', row[2])
    row[2] = re.sub('Чё{[^}]+?}-либо{[^}]+?}', 'Чё-либо{что-либо=SPRO,ед,сред,неод=вин|что-либо=SPRO,ед,сред,неод=им|что-либо=SPRO,ед,сред,неод=род}', row[2])
    row[2] = re.sub('чё{[^}]+?}-либо{[^}]+?}', 'чё-либо{что-либо=SPRO,ед,сред,неод=вин|что-либо=SPRO,ед,сред,неод=им|что-либо=SPRO,ед,сред,неод=род}', row[2])
    row[2] = re.sub('Чё{[^}]+?}', 'Чё{что=SPRO,ед,сред,неод=вин|что=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub('чё{[^}]+?}', 'чё{что=SPRO,ед,сред,неод=вин|что=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub('Чё{[^}]+?}-то{[^}]+?}', 'Чё-то{что-то=SPRO,ед,сред,неод=вин|что-то=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub('чё{[^}]+?}-то{[^}]+?}', 'чё-то{что-то=SPRO,ед,сред,неод=вин|что-то=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub('Чё{[^}]+?}-т{[^}]+?}', 'Чё-т{что-то=SPRO,ед,сред,неод=вин|что-то=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub('чё{[^}]+?}-т{[^}]+?}', 'чё-т{что-то=SPRO,ед,сред,неод=вин|что-то=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub('то{то=CONJ=} есть{[^}]+?}', 'то{то=CONJ=} есть{быть=V,нп=непрош,ед,изъяв,3-л,несов}', row[2])
    row[2] = re.sub('То{то=CONJ=} есть{[^}]+?}', 'То{то=CONJ=} есть{быть=V,нп=непрош,ед,изъяв,3-л,несов}', row[2])
    row[2] = re.sub('то{то=CONJ=} есь{[^}]+?}', 'то{то=CONJ=} есь{быть=V,нп=непрош,ед,изъяв,3-л,несов}', row[2])
    row[2] = re.sub('То{то=CONJ=} есь{[^}]+?}', 'То{то=CONJ=} есь{быть=V,нп=непрош,ед,изъяв,3-л,несов}', row[2])
    row[2] = re.sub('то{то=PART=} есть{[^}]+?}', 'то{то=PART=} есть{быть=V,нп=непрош,ед,изъяв,3-л,несов}', row[2])
    row[2] = re.sub('То{то=PART=} есть{[^}]+?}', 'То{то=PART=} есть{быть=V,нп=непрош,ед,изъяв,3-л,несов}', row[2])
    row[2] = re.sub('то{то=PART=} есь{[^}]+?}', 'то{то=PART=} есь{быть=V,нп=непрош,ед,изъяв,3-л,несов}', row[2])
    row[2] = re.sub('То{то=PART=} есь{[^}]+?}', 'То{то=PART=} есь{быть=V,нп=непрош,ед,изъяв,3-л,несов}', row[2])
    row[2] = re.sub('Где{где=ADVPRO=}-нить{[^}]+?}', 'Где-нить{где-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub('где{где=ADVPRO=}-нить{[^}]+?}', 'где-нить{где-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub('Куда{куда=ADVPRO=}-нить{[^}]+?}', 'Куда-нить{куда-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub('куда{куда=ADVPRO=}-нить{[^}]+?}', 'куда-нить{куда-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub('Откуда{откуда=ADVPRO=}-нить{[^}]+?}', 'Откуда-нить{откуда-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub('откуда{откуда=ADVPRO=}-нить{[^}]+?}', 'откуда-нить{откуда-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub('Как{как=ADVPRO=}-нить{[^}]+?}', 'Как-нить{как-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub('как{как=ADVPRO=}-нить{[^}]+?}', 'как-нить{как-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub('Когда{когда=ADVPRO=}-нить{[^}]+?}', 'Когда-нить{когда-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub('когда{когда=ADVPRO=}-нить{[^}]+?}', 'когда-нить{когда-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub('З{1}{з=S,сокр=[^}]+?}-', 'З-', row[2])
    row[2] = re.sub('з{1}{з=S,сокр=[^}]+?}-', 'з-', row[2])

    word_morph[row_num][2] = row[2]
    with open(file, 'w', encoding='UTF-8', newline='') as f:
            csv.writer(f, delimiter='\t', quotechar=None).writerows(word_morph)

        
rightTAGSemerged = list()
right_tag_emerged = list()

with open(file, 'r', encoding='UTF-8', newline='') as f:
        word_morph = list(csv.reader(f, delimiter='\t'))
with open('preps.txt', 'r', encoding='UTF-8', newline='') as dic:
        PrepsList = list(csv.reader(dic, delimiter=','))

row_num = -1
for row in word_morph:
    row_num = row_num + 1
    all_right_tags = list()
    tags = list(re.finditer(r'(?P<prepword>[-А-яЁё]+){(?P<prep>[-А-яЁё]+)=PR=} (?P<word>[-А-яЁё]+){(?P<alts>[^}]+\|.+?)}', row[2]))
    rightTAGSemerged = list()
    tags_to_edit = list()
    
    for tag in tags:
        for Prep in PrepsList:
            alts = tag['alts'].split('|')
                
            
            
            if re.search(Prep[0] + ' (?P<word>[-А-яЁё]+){(?P<alts>[^}]+|.+?)}',tag['prepword']+'{'+tag['prep']+'=PR=} '+tag['word']+'{'+tag['alts']+'}') != None:
                right_alts = list()
                tags_to_edit.append(tag)
                    #HERE IS THE PROBLEM I THINK               
                if len(Prep) == 3 :
                    
                    for alt in alts:
                        
                        if re.search('.+?=.*?' + Prep[1] + '.*?', alt) != None or re.search('.+?=.*?' + Prep[2] + '.*?', alt) != None  :
                            right_alts.append(alt)
                elif len(Prep) == 4 :
                    
                    for alt in alts:
                        
                        if re.search('.+?=.*?' + Prep[1] + '.*?', alt) != None or re.search('.+?=.*?' + Prep[2] + '.*?', alt) != None or re.search('.+?=.*?' + Prep[3] + '.*?', alt) != None :
                            right_alts.append(alt)
                                                        

                else:
                    
                    for alt in alts:
                        
                        if alt.find(Prep[1]) > -1 :
                            right_alts.append(alt)
                                
        right_tag_emerged = tag['prepword'] + '{' + tag['prep'] + '=PR=}' + ' '+ tag['word'] + '{' + sep.join(right_alts) + '}'
            
        rightTAGSemerged.append(right_tag_emerged)
    
    
    if len(tags_to_edit) == len(rightTAGSemerged) :
        
        a=-1 
        for i in rightTAGSemerged:
            a=a+1
            row[2] = replace_with(row[2], tags_to_edit[a].span(), '/'*(tags_to_edit[a].span()[1]-tags_to_edit[a].span()[0]))
        a=-1
        for i in rightTAGSemerged:
            a=a+1
            
            print(str(row_num + 1) + ' ' + str(rightTAGSemerged[a]))
            row[2] = re.sub('/+',rightTAGSemerged[a],row[2], count = 1)
        word_morph[row_num][2] = row[2]
        with open(file, 'w', encoding='UTF-8', newline='') as f:
            csv.writer(f, delimiter='\t', quotechar=None).writerows(word_morph)
#######################################################################################################################################################################################################################
with open(file, 'r', encoding='UTF-8', newline='') as f:
        text = f.readlines()

print('\nКОЛИЧЕСТВО ЗНАКОВ "ИЛИ" ДО: ' + str(OR_amount))
print('КОЛИЧЕСТВО ЗНАКОВ "ИЛИ" ПОСЛЕ: ' + str(len(re.findall('\|',' '.join(text)))))
print('КОЛИЧЕСТВО ПУСТЫХ ФИГУРНЫХ СКОБОК: ' + str(len(re.findall('\{\}',' '.join(text)))))
time.sleep(1)
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

