def replace_with(string, span, repl):
    begin, end = span
    return string[:begin] + repl + string[end:]

sep = '|'

with open(file, 'r', encoding='UTF-8', newline='') as f:
        word_morph = list(csv.reader(f, delimiter='\t'))
row_num = -1
for row in word_morph :
    row_num = row_num + 1
    row[2] = re.sub(r'{э=S,сокр=[^}]+?}', '{э=INTJ=}', row[2])
    row[2] = re.sub(r'{ц=S,сокр=[^}]+?}', '{ц=INTJ=}', row[2])
    row[2] = re.sub(r'{ф=S,сокр=[^}]+?}', '{ф=INTJ=}', row[2])
    row[2] = re.sub(r'{о=S,сокр=[^}]+?}', '{о=INTJ=}', row[2])
    row[2] = re.sub(r'{мм=S,.+?}', '{мм=INTJ=}', row[2])
    row[2] = re.sub(r'{в=S,сокр=[^}]+?}', '{в=PR=}', row[2])
    row[2] = re.sub(r'{у=S,сокр=[^}]+?}', '{у=PR=}', row[2])
    row[2] = re.sub(r'{с=S,сокр=[^}]+?}', '{с=PR=}', row[2])
    row[2] = re.sub(r'{к=S,сокр=[^}]+?}', '{к=PR=}', row[2])
    row[2] = re.sub(r'{о=S,сокр=[^}]+?}', '{о=PR=|о=INTJ=}', row[2])
    row[2] = re.sub(r'{а=S,сокр=[^}]+?}', '{а=CONJ=|а=INTJ=}', row[2])
    row[2] = re.sub(r'{[А-я]=INTJ=}-', '-', row[2])
    row[2] = re.sub(r'{[А-я]=PR=}-', '-', row[2])
    row[2] = re.sub(r'}-в{в=PR=}', '}-в', row[2])
    row[2] = re.sub(r'}-у{у=PR=}', '}-у', row[2])
    row[2] = re.sub(r'}-с{с=PR=}', '}-с', row[2])
    row[2] = re.sub(r'}-к{в=PR=}', '}-к', row[2])
    row[2] = re.sub(r'-к{к=PR=}', '-к', row[2])
    row[2] = re.sub(r'Ничё{[^}]+?}', 'Ничё{ничто=SPRO,ед,сред=род|ничто=SPRO,ед,сред=вин}', row[2])
    row[2] = re.sub(r'ничё{[^}]+?}', 'ничё{ничто=SPRO,ед,сред=род|ничто=SPRO,ед,сред=вин}', row[2])
    row[2] = re.sub(r'Чё{[^}]+?}-нить{[^}]+?}', 'Чё-нить{что-нибудь=SPRO,ед,сред,неод=вин|что-нибудь=SPRO,ед,сред,неод=им|что-нибудь=SPRO,ед,сред,неод=род}', row[2])
    row[2] = re.sub(r'чё{[^}]+?}-нить{[^}]+?}', 'чё-нить{что-нибудь=SPRO,ед,сред,неод=вин|что-нибудь=SPRO,ед,сред,неод=им|что-нибудь=SPRO,ед,сред,неод=род}', row[2])
    row[2] = re.sub(r'Чё{[^}]+?}-нибудь{[^}]+?}', 'Чё-нибудь{что-нибудь=SPRO,ед,сред,неод=вин|что-нибудь=SPRO,ед,сред,неод=им|что-нибудь=SPRO,ед,сред,неод=род}', row[2])
    row[2] = re.sub(r'чё{[^}]+?}-нибудь{[^}]+?}', 'чё-нибудь{что-нибудь=SPRO,ед,сред,неод=вин|что-нибудь=SPRO,ед,сред,неод=им|что-нибудь=SPRO,ед,сред,неод=род}', row[2])
    row[2] = re.sub(r'Чё{[^}]+?}-либо{[^}]+?}', 'Чё-либо{что-либо=SPRO,ед,сред,неод=вин|что-либо=SPRO,ед,сред,неод=им|что-либо=SPRO,ед,сред,неод=род}', row[2])
    row[2] = re.sub(r'чё{[^}]+?}-либо{[^}]+?}', 'чё-либо{что-либо=SPRO,ед,сред,неод=вин|что-либо=SPRO,ед,сред,неод=им|что-либо=SPRO,ед,сред,неод=род}', row[2])
    row[2] = re.sub(r'Чё{че[^}]+?}', 'Чё{что=SPRO,ед,сред,неод=вин|что=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub(r'чё{че[^}]+?}', 'чё{что=SPRO,ед,сред,неод=вин|что=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub(r'Чё{[^}]+?}-то{[^}]+?}', 'Чё-то{что-то=SPRO,ед,сред,неод=вин|что-то=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub(r'чё{[^}]+?}-то{[^}]+?}', 'чё-то{что-то=SPRO,ед,сред,неод=вин|что-то=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub(r'Чё{[^}]+?}-т{[^}]+?}', 'Чё-т{что-то=SPRO,ед,сред,неод=вин|что-то=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub(r'чё{[^}]+?}-т{[^}]+?}', 'чё-т{что-то=SPRO,ед,сред,неод=вин|что-то=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub(r'то{то=[^}]+?} есть{[^}]+?}', 'то{то=SPRO,ед,сред,неод=им} есть{быть=V,нп=непрош,ед,изъяв,3-л,несов}', row[2])
    row[2] = re.sub(r'То{то=[^}]+?} есть{[^}]+?}', 'То{то=SPRO,ед,сред,неод=им} есть{быть=V,нп=непрош,ед,изъяв,3-л,несов}', row[2])
    row[2] = re.sub(r'то{то=[^}]+?} есь{[^}]+?}', 'то{то=SPRO,ед,сред,неод=им} есь{быть=V,нп=непрош,ед,изъяв,3-л,несов}', row[2])
    row[2] = re.sub(r'То{то=[^}]+?} есь{[^}]+?}', 'То{то=SPRO,ед,сред,неод=им} есь{быть=V,нп=непрош,ед,изъяв,3-л,несов}', row[2])
    row[2] = re.sub(r'Где{где=ADVPRO=}-нить{[^}]+?}', 'Где-нить{где-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub(r'где{где=ADVPRO=}-нить{[^}]+?}', 'где-нить{где-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub(r'Куда{куда=ADVPRO=}-нить{[^}]+?}', 'Куда-нить{куда-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub(r'куда{куда=ADVPRO=}-нить{[^}]+?}', 'куда-нить{куда-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub(r'Откуда{откуда=ADVPRO=}-нить{[^}]+?}', 'Откуда-нить{откуда-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub(r'откуда{откуда=ADVPRO=}-нить{[^}]+?}', 'откуда-нить{откуда-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub(r'Как{как=ADVPRO=}-нить{[^}]+?}', 'Как-нить{как-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub(r'как{как=ADVPRO=}-нить{[^}]+?}', 'как-нить{как-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub(r'Когда{когда=ADVPRO=}-нить{[^}]+?}', 'Когда-нить{когда-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub(r'когда{когда=ADVPRO=}-нить{[^}]+?}', 'когда-нить{когда-нибудь=ADVPRO=}', row[2])
    row[2] = re.sub(r'З{1}{з=S,сокр=[^}]+?}-', 'З-', row[2])
    row[2] = re.sub(r'з{1}{з=S,сокр=[^}]+?}-', 'з-', row[2])
    row[2] = re.sub(r'Допустим{допускать=V[^}]+?}', 'Допустим{допускать=V=мн,пов,1-л,сов}', row[2])
    row[2] = re.sub(r'допустим{допускать=V[^}]+?}', 'допустим{допускать=V=мн,пов,1-л,сов}', row[2])
    row[2] = re.sub(r'На{на=PR=} самом{[^}]+?} деле{[^}]+?}', 'На{на=PR=} самом{самый=APRO=пр,ед,сред} деле{дело=S,сред,неод=пр,ед}', row[2])
    row[2] = re.sub(r'на{на=PR=} самом{[^}]+?} деле{[^}]+?}', 'на{на=PR=} самом{самый=APRO=пр,ед,сред} деле{дело=S,сред,неод=пр,ед}', row[2])
    row[2] = re.sub(r'Всё{[^}]+?} равно{[^}]+?}', 'Всё{все=SPRO,мн=им} равно{равный=A=ед,кр,сред}', row[2])
    row[2] = re.sub(r'всё{[^}]+?} равно{[^}]+?}', 'всё{все=SPRO,мн=им} равно{равный=A=ед,кр,сред}', row[2])
    row[2] = re.sub(r'Есь{есь\?=[^}]+?}', 'Есь{быть=V,нп=непрош,ед,изъяв,3-л,несов|быть=V,нп=непрош,мн,изъяв,3-л,несов|быть=V,нп=наст,мн,изъяв,1-л,несов|быть=V,нп=наст,ед,изъяв,1-л,несов|быть=V,нп=наст,мн,изъяв,2-л,несов|быть=V,нп=наст,ед,изъяв,2-л,несов|быть=V,нп=наст,мн,изъяв,3-л,несов|быть=V,нп=наст,ед,изъяв,3-л,несов}', row[2])
    row[2] = re.sub(r'есь{есь\?=[^}]+?}', 'есь{быть=V,нп=непрош,ед,изъяв,3-л,несов|быть=V,нп=непрош,мн,изъяв,3-л,несов|быть=V,нп=наст,мн,изъяв,1-л,несов|быть=V,нп=наст,ед,изъяв,1-л,несов|быть=V,нп=наст,мн,изъяв,2-л,несов|быть=V,нп=наст,ед,изъяв,2-л,несов|быть=V,нп=наст,мн,изъяв,3-л,несов|быть=V,нп=наст,ед,изъяв,3-л,несов}', row[2])
    row[2] = re.sub(r'Эм{эм=S[^}]+?}', 'Эм{эм=INTJ=}', row[2])
    row[2] = re.sub(r'эм{эм=S[^}]+?}', 'эм{эм=INTJ=}', row[2])
    row[2] = re.sub(r'Ваще{ващ\?=S[^}]+?}', 'Ваще{вообще=ADV,вводн=}', row[2])
    row[2] = re.sub(r'ваще{ващ\?=S[^}]+?}', 'ваще{вообще=ADV,вводн=}', row[2])
    row[2] = re.sub(r'Вапще{вапщ[^}]+?}', 'Вапще{вообще=ADV,вводн=}', row[2])
    row[2] = re.sub(r'вапще{вапщ[^}]+?}', 'вапще{вообще=ADV,вводн=}', row[2])
    row[2] = re.sub(r'По{по=PR=} сути{суть=S[^}]+?}', 'По{по=PR=} сути{суть=S,жен,неод=дат,ед}', row[2])
    row[2] = re.sub(r'по{по=PR=} сути{суть=S[^}]+?}', 'по{по=PR=} сути{суть=S,жен,неод=дат,ед}', row[2])
    row[2] = re.sub(r'В{в=PR=} общем{[^}]+?}', 'В{в=PR=} общем{общий=A=пр,ед,полн,сред}', row[2])
    row[2] = re.sub(r'в{в=PR=} общем{[^}]+?}', 'в{в=PR=} общем{общий=A=пр,ед,полн,сред}', row[2])
    row[2] = re.sub(r'Ещё{еще=ADV=} раз{[^}]+?}', 'Ещё{еще=ADV=} раз{раз=S,муж,неод=вин,ед}', row[2])
    row[2] = re.sub(r'ещё{еще=ADV=} раз{[^}]+?}', 'ещё{еще=ADV=} раз{раз=S,муж,неод=вин,ед}', row[2])
    row[2] = re.sub(r'Даж{даж\?=S,муж,неод=им,ед}', 'Даж{даже=PART=}', row[2])
    row[2] = re.sub(r'даж{даж\?=S,муж,неод=им,ед}', 'даж{даже=PART=}', row[2])
    row[2] = re.sub(r'Канеш{канеш\?=S,имя,муж,од=им,ед}', 'Канеш{конечно=ADV,вводн=}', row[2])
    row[2] = re.sub(r'канеш{канеш\?=S,имя,муж,од=им,ед}', 'канеш{конечно=ADV,вводн=}', row[2])
    row[2] = re.sub(r'Канешн{канешн\?=S,[^}]?+}', 'Канешн{конечно=ADV,вводн=}', row[2])
    row[2] = re.sub(r'канешн{канешн\?=S,[^}]?+}', 'канешн{конечно=ADV,вводн=}', row[2])
    row[2] = re.sub(r'Мож{мож\?=S,гео,муж,неод=вин,ед\|мож?=S,гео,муж,неод=им,ед}', 'Мож{может=ADV,вводн=}', row[2])
    row[2] = re.sub(r'мож{мож\?=S,гео,муж,неод=вин,ед\|мож?=S,гео,муж,неод=им,ед}', 'мож{может=ADV,вводн=}', row[2])
    row[2] = re.sub(r'Мош{мош=S,имя,муж,од=им,ед}', 'Мош{может=ADV,вводн=}', row[2])
    row[2] = re.sub(r'мош{мош=S,имя,муж,од=им,ед}', 'мош{может=ADV,вводн=}', row[2])
    row[2] = re.sub(r'Грит{грита=S,имя,жен,од=вин,мн\|грита=S,имя,жен,од=род,мн}', 'Грит{говорить=V,несов,пе=непрош,ед,изъяв,3-л}', row[2])
    row[2] = re.sub(r'грит{грита=S,имя,жен,од=вин,мн\|грита=S,имя,жен,од=род,мн}', 'грит{говорить=V,несов,пе=непрош,ед,изъяв,3-л}', row[2])
    row[2] = re.sub(r'Грят{грята\?=S,[^}]+?}', 'Грят{говорить=V,несов,пе=непрош,мн,изъяв,3-л}', row[2])
    row[2] = re.sub(r'грят{грята\?=S,[^}]+?}', 'грят{говорить=V,несов,пе=непрош,мн,изъяв,3-л}', row[2])
    row[2] = re.sub(r'Грю{грю\?=S,[^}]+?}', 'Грю{Говорить=V,несов,пе=непрош,ед,изъяв,1-л}', row[2])
    row[2] = re.sub(r'грю{грю\?=S,[^}]+?}', 'грю{говорить=V,несов,пе=непрош,ед,изъяв,1-л}', row[2])
    row[2] = re.sub(r'Грится{гриться\?=V,несов,нп=непрош,ед,изъяв,3-л}', 'Гриться{говориться=V,несов,нп=непрош,ед,изъяв,3-л}', row[2])
    row[2] = re.sub(r'грится{гриться\?=V,несов,нп=непрош,ед,изъяв,3-л}', 'гриться{говориться=V,несов,нп=непрош,ед,изъяв,3-л}', row[2])
    row[2] = re.sub(r'Сёдня{седний\?=A=ед,кр,жен}', 'Сёдня{сегодня=ADV=}', row[2])
    row[2] = re.sub(r'cёдня{седний\?=A=ед,кр,жен}', 'cёдня{сегодня=ADV=}', row[2])
    row[2] = re.sub(r'Тока{ток=S,муж,неод=вин,мн\|ток=S,муж,неод=род,ед\|ток=S,муж,неод=им,мн}', 'Тока{только=PART=}', row[2])
    row[2] = re.sub(r'тока{ток=S,муж,неод=вин,мн\|ток=S,муж,неод=род,ед\|ток=S,муж,неод=им,мн}', 'тока{только=PART=}', row[2])
    row[2] = re.sub(r'Пусь{пуся\?=[^}]+?}', 'Пусь{пусть=PART=}', row[2])
    row[2] = re.sub(r'пусь{пуся\?=[^}]+?}', 'пусь{пусть=PART=}', row[2])
    row[2] = re.sub(r'Еси{еси\?=S,[^}]+?}', 'Еси{если=CONJ=}', row[2])
    row[2] = re.sub(r'еси{еси\?=S,[^}]+?}', 'еси{если=CONJ=}', row[2])
    row[2] = re.sub(r'Чёт{чет=S,муж,неод=вин,ед\|чет=S,муж,неод=им,ед}', 'Чёт{что-то=SPRO,ед,сред,неод=вин|что-то=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub(r'чёт{чет=S,муж,неод=вин,ед\|чет=S,муж,неод=им,ед}', 'чёт{что-то=SPRO,ед,сред,неод=вин|что-то=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub(r'Шоб{шоб\?=S,[^}]+?}', 'Шоб{чтобы=CONJ=}', row[2])
    row[2] = re.sub(r'шоб{шоб\?=S,[^}]+?}', 'шоб{чтобы=CONJ=}', row[2])
    row[2] = re.sub(r'Шо{шо\?=S,[^}]+?}', 'Шо{что=SPRO,ед,сред,неод=вин|что=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub(r'шо{шо[^}а-я]+?}', 'шо{что=SPRO,ед,сред,неод=вин|что=SPRO,ед,сред,неод=им}', row[2])
    row[2] = re.sub(r'Када{кад\?=S,муж,неод=род,ед}', 'Када{когда=ADVPRO=|когда=CONJ=}', row[2])
    row[2] = re.sub(r'када{кад\?=S,муж,неод=род,ед}', 'када{когда=ADVPRO=|когда=CONJ=}', row[2])
    row[2] = re.sub(r'Никада{никада\?=S,жен,од=им,ед}', 'Никада{никогда=ADVPRO=}', row[2])
    row[2] = re.sub(r'никада{никада\?=S,жен,од=им,ед}', 'никада{никогда=ADVPRO=}', row[2])
    row[2] = re.sub(r'тошто{тошто?=[^}]+?}', 'тошто{что=CONJ=}', row[2])
    row[2] = re.sub(r'Тошто{тошто?=[^}]+?}', 'Тошто{что=CONJ=}', row[2])
    row[2] = re.sub(r'ни{ни=PART=} разу{раз=S,[^}]+?}', 'ни{ни=PART=} разу{раз=S,муж,неод=парт,ед}', row[2])
    row[2] = re.sub(r'Ни{ни=PART=} разу{раз=S,[^}]+?}', 'Ни{ни=PART=} разу{раз=S,муж,неод=парт,ед}', row[2])
    row[2] = re.sub(r'в{в=PR=} основном{основной=A=[^}]+?}', 'в{в=PR=} основном{основной=A=пр,ед,полн,сред}', row[2])
    row[2] = re.sub(r'В{в=PR=} основном{основной=A=[^}]+?}', 'В{в=PR=} основном{основной=A=пр,ед,полн,сред}', row[2])
    
    
    
    
    

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
    #all_right_tags = list()

    ################################### NUMERALS IN NOMINATIVE-like CASE
    rightTAGS_NUM_emerged = list()
    tags_num = list(re.finditer(r'(?P<num>[-А-яЁё]+?){(?P<numalts>[-А-яЁё]+?=NUM[^}]*?[=,]им[^}]*?)} (?P<word>[-А-яЁё]+){(?P<alts>[^}]+?[=,]род[^}]*?)}', row[2]))
    for tag_num in tags_num:
        alts_num = tag_num['alts'].split('|')
        right_alts_num = list()
        for alt_num in alts_num:
            if re.search('[^а-я]род[^а-я]*?', alt_num) != None:
                right_alts_num.append(alt_num)
        if tag_num['num'] == 'два' or tag_num['num'] == 'две' or tag_num['num'] == 'три' or tag_num['num'] == 'четыре':
            two_four_num = list()
            for right_alt_num in right_alts_num:
                if re.search('[^а-я]ед[^а-я]*?', right_alt_num) != None:
                    two_four_num.append(right_alt_num)
            right_alts_num = two_four_num
        right_tag_num_emerged = tag_num['num']+'{'+tag_num['numalts']+'} '+tag_num['word']+'{'+sep.join(right_alts_num)+'}'
        rightTAGS_NUM_emerged.append(right_tag_num_emerged)        
    if len(tags_num) == len(rightTAGS_NUM_emerged) :
        v=-1
        for i in rightTAGS_NUM_emerged:
            v=v+1
            row[2] = replace_with(row[2], tags_num[v].span(), '+'*(tags_num[v].span()[1]-tags_num[v].span()[0]))
        v=-1
        for i in rightTAGS_NUM_emerged:
            v=v+1
            print(str(row_num + 1) + ' ' + str(rightTAGS_NUM_emerged[v]))
            row[2] = re.sub(r'\++',rightTAGS_NUM_emerged[v],row[2], count = 1)
        word_morph[row_num][2] = row[2]
        with open(file, 'w', encoding='UTF-8', newline='') as f:
            csv.writer(f, delimiter='\t', quotechar=None).writerows(word_morph)        
    ################################### PREPOSITIONS

row_num = -1
for row in word_morph:
    row_num = row_num + 1
    all_right_tags = list()
    tags = list(re.finditer(r'(?P<prepword>[-А-яЁё]+){(?P<prep>[-А-яЁё]+)=PR=} (?P<word>[-А-яЁё]+){(?P<alts>[а-яё]+?=(S|SPRO|A|APRO|NUM|ANUM)[,=][^}]+\|[^}]+?)}', row[2]))
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
                        
                        if re.search('[^=]+?=[A-Z]+?.*?=.*?[=,]?' + Prep[1] + '.*?$', alt) != None or re.search('[^=]+?=[A-Z]+?.*?=.*?[=,]?' + Prep[2] + '.*?$', alt) != None  :
                            right_alts.append(alt)
                elif len(Prep) == 4 :
                    
                    for alt in alts:
                        
                        if re.search('[^=]+?=[A-Z]+?.*?=.*?[=,]?' + Prep[1] + '.*?$', alt) != None or re.search('[^=]+?=[A-Z]+?.*?=.*?[=,]?' + Prep[2] + '.*?$', alt) != None or re.search('[^=]+?=[A-Z]+?.*?=.*?[=,]?' + Prep[3] + '.*?$', alt) != None :
                            
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
            row[2] = re.sub(r'/+',rightTAGSemerged[a],row[2], count = 1)

        word_morph[row_num][2] = row[2]
        with open(file, 'w', encoding='UTF-8', newline='') as f:
            csv.writer(f, delimiter='\t', quotechar=None).writerows(word_morph)
#######################################################################################################################################################################################################################


