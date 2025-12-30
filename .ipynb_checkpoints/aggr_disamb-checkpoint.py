def replace_with(string, span, repl):
    begin, end = span
    return string[:begin] + repl + string[end:]


rightTAGSemerged = list()
right_tag_emerged = list()
right_alts = list()
sep = '|'
#Сюда ещё вставить снова чтение файла
with open(file, 'r', encoding='UTF-8', newline='') as f:
        word_morph = list(csv.reader(f, delimiter='\t'))
            
row_num = -1
for row in word_morph:
    row_num = row_num + 1
    rightTAGSemerged = list()
    all_right_tags = list()
    # [-А-яЁё]+{[-А-яЁё]+=((ANUM)|A|(APRO))=[^}(кр)]+?} [-А-яЁё]+{[-А-яЁё]+=S,[^}]+?}
    tags = list(re.finditer(r'(?P<firwd>[-А-яЁё]+){(?P<firalts>[-А-яЁё]+=(ANUM|A|APRO)=[^}]*?(им|род|дат|вин|твор|пр)[^}]+?)} (?P<secwd>[-А-яЁё]+){(?P<secalts>[-А-яЁё]+?=S[а-я,]*?(муж|жен|сред)[=,][^}]+?)}',row[2]))
    #print(len(tags))
    for tag in tags :
        right_tag_emerged = list()
        right_noun_alts = list()
        right_attr_alts = list()
        attr_keys = list()
        noun_keys = list()
        right_noun_indexes = list()
        right_attr_indexes = list()
        attr_alts = tag['firalts'].split('|')
        noun_alts = tag['secalts'].split('|')
        for attr_alt in attr_alts:  #ATTRIBUTE
            attr_gend = re.search('[,=](муж|жен|сред)[,]?',attr_alt)#GENDER
            attr_num = re.search('[,=](ед|мн)[,]?',attr_alt)#NUMBER
            attr_case = re.search('[,=](им|род|дат|вин|твор|пр)[,]?',attr_alt)#CASE
            if attr_gend == None:
                attr_key = [attr_num[1], attr_case[1]]
            else:
                attr_key = [attr_gend[1], attr_num[1], attr_case[1]]
            attr_keys.append(attr_key)

        
        for noun_alt in noun_alts:  #NOUN
            noun_gend = re.search('[,](жен|сред|муж)[=,]',noun_alt)#GENDER
            noun_num = re.search('[=,](ед|мн)[,]?', noun_alt)#NUMBER
            noun_case = re.search('[=,](им|род|дат|вин|твор|пр|местн|парт)[,]?',noun_alt)#CASE
            noun_key = [noun_gend[1],noun_num[1],noun_case[1]]
            if noun_key[1] == 'мн':
                noun_key.pop(0)
            noun_keys.append(noun_key)
        
        for n in range(len(noun_keys)):      #FIND OUT THE RIGHT INDEXES
            for j in range(len(attr_keys)):
                if len(noun_keys[n])==3 and noun_keys[n][2] == 'местн':
                    noun_keys[n][2] = 'пр'
                if len(noun_keys[n])==3 and noun_keys[n][2] == 'парт':
                    noun_keys[n][2] = 'род'
                if noun_keys[n] == attr_keys[j]:
                    right_noun_indexes.append(n)
                    right_attr_indexes.append(j)
                    
        for n in right_noun_indexes:
            right_noun_alts.append(noun_alts[n])
        for j in right_attr_indexes:
            right_attr_alts.append(attr_alts[j])
        right_tag_emerged = tag['firwd']+'{'+sep.join(right_attr_alts)+'} '+tag['secwd']+'{'+sep.join(right_noun_alts)+'}'
        rightTAGSemerged.append(right_tag_emerged)
            

    if len(tags) == len(rightTAGSemerged) :
        
        a=-1 
        for i in rightTAGSemerged:
            a=a+1
            row[2] = replace_with(row[2], tags[a].span(), '/'*(tags[a].span()[1]-tags[a].span()[0]))
        a=-1
        for i in rightTAGSemerged:
            a=a+1
            
            print(str(row_num + 1) + ' ' + str(rightTAGSemerged[a]))
            row[2] = re.sub(r'/+',rightTAGSemerged[a],row[2], count = 1)
        word_morph[row_num][2] = row[2]
        with open(file, 'w', encoding='UTF-8', newline='') as f:
            csv.writer(f, delimiter='\t', quotechar=None).writerows(word_morph)    
###################################################################################################################################################################################
 
####################################################################################################################################################################################

