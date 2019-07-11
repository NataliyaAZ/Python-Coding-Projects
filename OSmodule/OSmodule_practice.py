import os
import time

fPath = "D:\\Natasha\\Coding\\GitHub\\Basic-Python-Projects\\OSmodule\\"

fList = os.listdir(fPath)

for f in fList:
    if f.endswith('.txt'):
        text_files = os.path.join(fPath,f)
        mod_time = time.localtime(os.path.getmtime(fPath))
        fm_time = time.strftime("%m/%d/%Y, %H:%M:%S", mod_time)
        print("File Name:", text_files,"Modified:", fm_time)
