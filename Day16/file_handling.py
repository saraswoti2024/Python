##file banauxa x lae
# f1 = open("file1.txt","x") #ekchoti run garepaxi feri run garda feri banauna khojxa twra already exist xa so will throw erro

##to read the file(exisiting file matrai read garna milxa)
# f1 = open("file1.txt","r")
# data = f1.read()
# print(data)

##write mode->it will ovveride if file already exist,content pani override garxa
##it creates new file if the file doesnot exists

# f1 = open("file2.txt","w") ##if we run only this then the exisiting content in that file will be erased and it will be blank
# f1.write("overwrites from write file,already exist file ma new content haleko")
# print(f1.tell())
# f1.write("write")
# print(f1.tell())

# f1 = open("file2.txt","w")
# f1.write("new file aafai create vayo ani write gareko")

# print(f1.read()) #will throw error kna vanae mode write ma xa so write matrai support garxa

###r+-> if file doesnot exist it will give error
##first read then write hunxa
# f1 = open("file3.txt","x")
# f1 = open("file3.txt","r+")
# print(f1.tell()) #0 position ma hunxa
# f1.write("hi") #yesle 0,1 poistion ma hi lekhxa j content vayeni teskai mathi
# print(f1.tell()) #2 position ma aayo
# print(f1.read()) #2 position dekhi read garxa
# print(f1.tell()) #37 sabai read garepaxi

###w+ mode
##creates new file if file doesnot exists,totally overwrites if content already present 
# f2 = open("file2.txt","w+") #if execute only this same as write mode ,the exisiting content will be erased and it will be blank
# print(f2.tell())
# f2.write("hi sara ")
# print(f2.tell())
# f2.write("this is next write which will append")
# print(f2.tell())
# f2.seek(0) ##this initialized position to of yo string to 0 again ani balla read ma dekhauxa 
# print(f2.tell())
# print(f2.read())
# print(f2.tell())

###append mode(a+)-> creates new file if file doesnot exists, kai lekhya xa ani last ma add garxa lekheko kura lai append mode bata doesnot erase or overwrites like aaru mode
# f1 = open("file4.txt","a+")
# # f1.write("append mode ma aarko lekheko, yesari add hunxa yo lekheko overwrite haru gardaina")
# print(f1.tell())
# f1.seek(0) #yesari index 0 mai rakhnu parxa feri read garauna
# print(f1.read()) ##only a mode ma kholyam vanae read garna mildaina
# # f1.write("after read print this will not be read mathi ko lae") ##harek time yo execute vayo feri value append garirakhxa
# f1.seek(0)
# print(f1.read())

###if we want to open file of the desktop then give full path, in any mode it can be open
# f1 = open("E:\learn\django\python file.txt","a+")
# # f1.write("writing in desktop ko file")
# f1.seek(0)
# print(f1.read())
# f1.write("feri appending") ##changes aauxa extenal(desktop) ma vako file ma

##opening images and coping images -> images is in binary so use b last ma jun pani mode ma
f1 = open(r"E:\learn\Python\images\saraswoti.png","rb")
print(f1.read())

#coping 
f2 = open(r"E:\learn\Python\Day16\image.png","wb")
for i in f1:
    f2.write(i)
f1.close()
f2.close()

