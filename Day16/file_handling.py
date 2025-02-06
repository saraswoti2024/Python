##file banauxa x lae
# f1 = open("file1.txt","x") #ekchoti run garepaxi feri run garda feri banauna khojxa twra already exist xa so will throw erro

##to read the file(exisiting file matrai read garna milxa)
# f1 = open("file1.txt","r")
# data = f1.read()
# print(data)

##write mode->it will ovveride if file already exist,content pani override garxa
##it creates new file if the file doesnot exists

# f1 = open("file1.txt","w")
# f1.write("overwrites from write file,already exist file ma new content haleko")
# f1.write("write")

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

