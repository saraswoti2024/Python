# ##text data types- string

# #string-> (''/"","""/'''->for multiline)\
# #immutable-> original value change hudaina jati slicing,indexing j gareni
# name = 'asdfsdf dgdrg'
# print(type(name))
# print(name)

# name1 = """ hii
#                 this is multi-line string"""
# print(name1)
# print(type(name1))

# #length->length of character, space also counted 
# print(len(name))

# #indexing in string-> position of words
# print(name[2]) #d #starts from 0,1,2,......
# print(name[-2]) #r #ulto bata last ko print garya starts from -1,-2..

# #slicing in string starting:ending:steps(starts from 1)
# name = "my name is saraswoti khadka"
# print(name[0:7:1]) #o dekhi :6samma+1 garnu parxa: harek step #my name
# print(name[0:7:2]) #2 (0,1->2 number,1 ma pugeko value) step xodai garxa # ae

# #for reverse #starting(endingvalue):ending(startingvalue):steps(-1) for negative
# print(name[6:2:-1]) #ending:starting-1 garnu parxa: negativeindexing(reverse bata aauna)#eman #reverse garna 
# print(name[6:2:-2]) #mn

# print(name[3:]) #sabai print hunxa : yo matra rakhda
# print(name[::4]) #sabai string bata 4 step(0,1,2,3->3 ma pugeko value)
# print(name[::-3]) #aa oasim
# print(name)

# #string methods-> direct original values change hudaina method use garda ni aarko variable ma store garerw garda hunxa
# #1. upper()
# value = name.upper()
# print(value)

# #2.lower
# # yesto garda ni direct change hudaina kna vane tyo aarko var ni string vaisakyo ,feri aarko var banaunuparxa and so on
# value.lower()
# print(value) #output: MY NAME IS SARASWOTI KHADKA

# value1 = value.lower()
# print(value1) #my name is saraswoti khadka

# #3.swapcase->converts lower to upper and upper to lower
# intro = "SArAswoathi KHADKA hello hahahahah"
# intro1 = intro.swapcase()
# print(intro1) #output: sARaSWOTI khadka HELLO

# #4.capitalize -> first letter lai matra capital
# capital = intro.capitalize()
# print(capital)

# #5.count -> kati oota letter xa aaba only a only b(Case sensitive so a,A is different in python)
# countress = intro.count("haha") #sangai xa vane matrai count hunxa yo casema
# countres = intro.count("a") 
# print(countres)
# print(countress)

# #6.find-> kun index ma xa tyo letter vanxa
# find1 = intro.find("Asw") #yo word ko first sentence #3
# find2 = intro.find("a") #first ma jun xa tahi #7
# find3 = intro.find("z") #navako string ma -1 output dinxa
# print(find1)
# print(find2)
# print(find3)

# #7.replace-> word replace garna  string.replace(old, new, count=-1)
# new_Value = "hello whatsup sara sara khadka khadka"
# replace1 = new_Value.replace("sara","saraswoti") #jati oota sara xa sabai ma saraswoti aauxa
# replace2 = new_Value.replace("a","v",2) #2 oota a lai replace garxa
# replace4 = new_Value.replace("s","v",-1) #-1 default-> sabai replace aaru -2,-3 rakhna mildaina

# # replace3 = new_Value.replace("sara","saraswoti","khadka") #output:error
# replace3 = new_Value.replace("sara", "saraswoti").replace("khadka", "another_value") #multiple garna

# print(replace1)
# print(replace2)
# print(replace3)
# print(replace4)

#8.strip->space hatauxa aagadi rw paxadi ko matrai, common words or letter xa vane aagadi rw paxadi common words or letter or space tyo sabai nai hatauxa
# stripvalue = "hi welcome ih"
# b_strip= stripvalue.strip("h")
# print(f"original value : {stripvalue}")
# print(b_strip)

# stripvalue = "hlo eisveriyone this ies hlo"
# #sabai word similar vako hatauxa even space h,l,o, ,e,i,s - h,l,o, ,s,e,i
# b_strip2 = stripvalue.strip("hlo ies")
# print(b_strip2)

# #paxadi ko matrai hatauna leftstrip
# b_strip2 = stripvalue.lstrip("h")

# #paxadi ko matrai hatauna rightstrip
# b_strip2 = stripvalue.rstrip("e") #jati oota continous e xa right ma sabai hatauxa forex: heeeeee(sabai e remove hunxa), heehee(only 2 oota e #output:heeh)

# #9.split-> aauta aauta word xutinxa ani list ko form ma aauxa (, ki tw space ki tw 'a' yesto letter wa word haru lae xutauna milxa)
# letters = "appleaorangeapears"
# letters2 = "apple orange pears"
# print(letters.split('a')) #output ['', 'pple', 'or', 'nge', 'pe', 'rs']
# print(letters2.split(' ')) #output ['apple', 'orange', 'pears']

#10. center(with argument)-> center ma lyauxa Hamro string lai kati rakhxam value tesko bichama hamro word lai rakhdinxa
# name = "saraswoti"
# center_value = name.center(15)
# center_value2 = name.center(15,"&")
# print(center_value)
# print(center_value2)
