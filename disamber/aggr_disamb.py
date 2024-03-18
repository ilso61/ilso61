import os
import time

import argparse
import csv
import re

def replace_with(string, span, repl):
    begin, end = span
    return string[:begin] + repl + string[end:]


rightTAGSemerged = list()
right_tag_emerged = list()
right_alts = list()
sep = '|'

file = input('ВВЕДИТЕ ИМЯ TXT ФАЙЛА\t')
with open(file, 'r', encoding='UTF-8', newline='') as f:
        text = f.readlines()
OR_amount = len(re.findall('\|',' '.join(text)))

#Сюда ещё вставить снова чтение файла
with open(file, 'r', encoding='UTF-8', newline='') as f:
        word_morph = list(csv.reader(f, delimiter='\t'))
            
row_num = -1
for row in word_morph:
    row_num = row_num + 1
    rightTAGSemerged = list()
    all_right_tags = list()
    tags_to_edit = list()
    # [-А-яЁё]+{[-А-яЁё]+=((ANUM)|A|(APRO))=[^}(кр)]+?} [-А-яЁё]+{[-А-яЁё]+=S,[^}]+?}
    tags = list(re.finditer(r'(?P<firwd>[-А-яЁё]+){(?P<firalts>[-А-яЁё]+=((ANUM)|A|(APRO))=[^}(кр)]+?)} (?P<secwd>[-А-яЁё]+){(?P<secalts>[-А-яЁё]+=S,[^}]+?)}',row[2]))
    #print(len(tags))
    for tag in tags :
        right_tag_emerged = list()
        right_alts = list()
        
        
        #print(tag['firwd']+'{'+tag['firalts']+'} '+ tag['secwd']+'{'+tag['secalts']+'}')

        attr_alts = tag['firalts'].split('|')
        noun_alts = tag['secalts'].split('|')
        if len(attr_alts)<len(noun_alts) :
            tags_to_edit.append(tag)
            for alt_attr in attr_alts :
                right_case = re.search('=[A-Z]+=.*?(?P<case>((им)|(род)|(дат)|(вин)|(твор)|(пр))).*?$',alt_attr)
                right_num = re.search('=[A-Z]+=.*?(?P<num>((ед)|(мн))).*?$',alt_attr)
                #print(right_case['case'] +' '+ right_num['num'])
                for alt_noun in noun_alts :
                    if re.search('=S,.+?=.*?'+right_case['case']+'.*',alt_noun)!=None and re.search('=S,.+?=.*?'+right_num['num']+'.*',alt_noun)!=None :
                        right_alts.append(alt_noun)
                        #print(alt_attr)

        elif len(attr_alts)>len(noun_alts) :
            tags_to_edit.append(tag)
            for alt_noun in noun_alts :
                right_case = re.search('=S,.+?=.*?(?P<case>((им)|(род)|(дат)|(вин)|(твор)|(пр)|(местн))).*?$',alt_noun)
                if right_case['case'] == 'местн':
                    right_case['case'] = 'пр'
                right_num = re.search('=S,.*?(?P<num>((ед)|(мн))).*?$',alt_noun)
                if right_num == None :
                    print(alt_noun)
                for alt_attr in attr_alts :
                    
                    if re.search('=[A-Z]+=.*?'+right_case['case']+'.*',alt_attr)!=None and re.search('=[A-Z]+=.*?'+right_num['num']+'.*',alt_attr)!=None :
                        right_alts.append(alt_attr)
                        #print(alt_noun)
        if len(attr_alts)<len(noun_alts) :
            right_tag_emerged = tag['firwd']+'{'+tag['firalts']+'} '+tag['secwd']+'{'+sep.join(right_alts)+'}'
        elif len(attr_alts)>len(noun_alts) :
            right_tag_emerged = tag['firwd']+'{'+sep.join(right_alts)+'} '+tag['secwd']+'{'+tag['secalts']+'}'
        #print(right_tag_emerged)
        if right_tag_emerged != list() :
            rightTAGSemerged.append(right_tag_emerged)
                    
    #print(rightTAGSemerged)
    #print('\n')
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
###################################################################################################################################################################################
rightTAGSemerged = list()
right_tag_emerged = list()
right_alts = list()

#Сюда ещё вставить снова чтение файла
with open(file, 'r', encoding='UTF-8', newline='') as f:
        word_morph = list(csv.reader(f, delimiter='\t'))
            
row_num = -1
for row in word_morph:
    row_num = row_num + 1
    rightTAGSemerged = list()
    all_right_tags = list()
    tags_to_edit = list()
    # [-А-яЁё]+{[-А-яЁё]+=((ANUM)|A|(APRO))=[^}(кр)]+?} [-А-яЁё]+{[-А-яЁё]+=S,[^}]+?}
    tags = list(re.finditer(r'(?P<firwd>[-А-яЁё]+){(?P<firalts>[-А-яЁё]+=((ANUM)|A|(APRO))=[^}(кр)]+?)} (?P<secwd>[-А-яЁё]+){(?P<secalts>[-А-яЁё]+=S,[^}]+?)}',row[2]))
    #print(len(tags))
    for tag in tags :
        right_tag_emerged = list()
        right_alts = list()
        
        
        #print(tag['firwd']+'{'+tag['firalts']+'} '+ tag['secwd']+'{'+tag['secalts']+'}')

        attr_alts = tag['firalts'].split('|')
        noun_alts = tag['secalts'].split('|')
        if re.search('=[A-Z]+=.*?(?P<num>мн).*?$',attr_alts[0])==None and re.search('=S,.*?(?P<gender>((муж)|(жен)|(сред))).*?=',noun_alts[0])!=None :
            tags_to_edit.append(tag)
            right_gender = re.search('=S,.*?(?P<gender>((муж)|(жен)|(сред))).*?=',noun_alts[0])
            for alt_attr in attr_alts :

                if re.search('=[A-Z]+=.*?'+right_gender['gender']+'.*?$',alt_attr)!=None :
                        right_alts.append(alt_attr)
                        #print(alt_attr)
#=[A-Z]+=.*?(?P<case>((им)|(род)|(дат)|(вин)|(твор)|(пр))).*?$

            right_tag_emerged = tag['firwd']+'{'+sep.join(right_alts)+'} '+tag['secwd']+'{'+tag['secalts']+'}'

        #print(right_tag_emerged)
        if right_tag_emerged != list() :
            rightTAGSemerged.append(right_tag_emerged)
                    
    #print(rightTAGSemerged)
    #print('\n')
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
####################################################################################################################################################################################
with open(file, 'r', encoding='UTF-8', newline='') as f:
        text = f.readlines()

print('\nКОЛИЧЕСТВО ЗНАКОВ "ИЛИ" ДО: ' + str(OR_amount))
print('КОЛИЧЕСТВО ЗНАКОВ "ИЛИ" ПОСЛЕ: ' + str(len(re.findall('\|',' '.join(text)))))
print('КОЛИЧЕСТВО ПУСТЫХ ФИГУРНЫХ СКОБОК: ' + str(len(re.findall('\{\}',' '.join(text)))))

os.rename('attr.cfg','attr.mp4')
time.sleep(1)

try:
    os.startfile('attr.mp4')
    time.sleep(5)
    os.rename('attr.mp4','attr.cfg')

except:
    os.rename('attr.mp4','attr.cfg')
