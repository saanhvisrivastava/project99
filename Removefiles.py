import os
import shutil
path=input("Enter the directory name to be sorted: ")
days=int(input("Enter number of days: "))
days=time.time()
listoffiles=os.listdir(path)
print(listoffiles)

for file in listoffiles:
    name,ext=os.path.splitext(file)
    print(name,ext)
    ext=ext[1:]
    print(ext)
    if ext==" " :
        continue

    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+ "/"+ file)
    else:
        os.makedirs(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+ "/"+ file)

        

