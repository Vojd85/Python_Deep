# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

str1 = '''На долю Тихого океана приходится более 50 % всей биомассы Мирового океана. Жизнь в океане представлена обильно и разнообразно, особенно в тропической и субтропической зонах между побережьями Азии и Австралии, где огромные территории заняты коралловыми рифами и мангровыми зарослями. Фитопланктон Тихого океана в основном состоит из микроскопических одноклеточных водорослей, насчитывающих около 1300 видов. В тропиках особенно распространены фукусовые, крупные зелёные и особенно известные красные водоросли, которые наряду с коралловыми полипами являются рифообразующими организмами[12].

Растительный мир Атлантики отличается видовым разнообразием. В толще воды доминирует фитопланктон, состоящий из динофлагеллятов и диатомовых водорослей. В разгар их сезонного цветения море у берегов Флориды окрашивается в ярко-красный цвет, а в литре морской воды содержатся десятки миллионов одноклеточных растений. Донная флора представлена бурыми (фукусы, ламинарии), зелёными, красными водорослями и некоторыми сосудистыми растениями. В устьях рек растёт зостера морская, или взморник, а в тропиках преобладают зелёные (каулерпа, валония) и бурые (саргассы) водоросли. Для южной части океана характерны бурые водоросли (фукус, лесония, электус). Животный мир отличается большим — около сотни — числом биполярных видов, обитающих только в холодных и умеренных поясах и отсутствующих в тропиках. В первую очередь это крупные морские звери (киты, тюлени, котики) и океанские птицы. В тропических широтах обитают морские ежи, коралловые полипы, акулы, рыбы-попугаи и рыбы-хирурги. Дельфины часто встречаются в водах Атлантики. Жизнерадостные интеллектуалы животного мира охотно сопровождают большие и малые суда — иногда, к сожалению, попадая под безжалостные лезвия винтов. Коренными жителями Атлантики являются африканский ламантин и самое крупное млекопитающее планеты — синий кит.

Флора и фауна Индийского океана необычайно разнообразны. Тропическая область выделяется богатством планктона. Особенно обильна одноклеточная водоросль Триходесмиум (тип Цианобактерии), из-за которой поверхностный слой воды сильно мутнеет и меняет свою окраску. Планктон Индийского океана отличает большое число светящихся ночью организмов: перидиней, некоторых видов медуз, гребневиков, оболочников. Обильно встречаются ярко окрашенные сифонофоры, в том числе ядовитые физалии. В умеренных и арктических водах главными представителями планктона являются копеподы, эвфуазиды и диатомеи. Наиболее многочисленными рыбами Индийского океана являются корифены, тунцы, нототениевые и разнообразные акулы. Из пресмыкающихся имеются несколько видов гигантских морских черепах, морские змеи, из млекопитающих — китообразные (беззубые и синие киты, кашалоты, дельфины), тюлени, морские слоны. Большинство китообразных обитают в умеренных и приполярных областях, где благодаря интенсивному перемешиванию вод возникают благоприятные условия для развития планктонных организмов. Растительный мир Индийского океана представлен бурыми (саргассовые, турбинарии) и зелёными водорослями (каулерна). Пышно развиваются также известковые водоросли литотамнии и халимеда, которые участвуют вместе с кораллами в сооружении рифовых построек. Типичным для прибрежной зоны Индийского океана является фитоценоз, образуемый мангровыми зарослями. Для умеренных и приантарктических вод наиболее характерны красные и бурые водоросли, главным образом из групп фукусовых и ламинариевых, порфира, гелидиум. В приполярных областях южного полушария встречаются гигантские макроцистисы[13].

Причина бедности органического мира Северного Ледовитого океана — суровые климатические условия. Исключения составляют лишь Северо-Европейский бассейн, Баренцево и Белое моря с их чрезвычайно богатым животным и растительным миром. Флора океана представлена главным образом ламинариями, фукусами, анфельцией, а в Белом море — также зостерой. Крайне бедна фауна дна морей восточной Арктики, особенно центральной части Арктического бассейна. В Северном Ледовитом океане насчитывается более 150 видов рыб, среди них большое число промысловых (сельдь, тресковые, лососевые, скорпеновые, камбаловые и другие). Морские птицы в Арктике ведут преимущественно колониальный образ жизни и обитают на берегах. Млекопитающие представлены тюленями, моржами, белухами, китами (главным образом полосатиками и грендландскими китами), нарвалами. На островах встречаются лемминги, по ледяным мостам заходят песцы и северные олени. Представителем фауны океана следует считать также белого медведя, жизнь которого в основном связана с дрейфующими, паковыми льдами или береговым припаем. Большинство зверей и птиц круглый год (а некоторые только зимой) имеют белую или очень светлую окраску'''

dict_from_str = {}
symbols = ['.', ',', '!', '?', '—']

for item in symbols:
    str2 = str1.replace(item, ' ')

print(str2)

list_from_str = str2.split()

for word in list_from_str:
    if word in dict_from_str:
        dict_from_str[word] += 1
    else:
        dict_from_str[word] = 1

sorted_values = sorted(dict_from_str.values(), reverse=True)

for count in sorted_values[:10]:
    for key in dict_from_str:
        if dict_from_str[key] == count and key not in symbols:
            print(f'Слово "{key}" встречается {count} раза')
            dict_from_str.pop(key)
            break

print(sorted_values[:10])