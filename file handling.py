with open(r"C:\Users\semmo\Documents\hello.txt","w") as f:
    f.write("hello world\n")
    f.write("this is a test\n")
    f.write("this is my victory\n")

import os
print("current working directory:",os.getcwd())
f=open("my new file.txt","w")
f.write("show me what u have got\n")
f.write("i can achieve anything in my life\n")
f.write("iam the best\n")
f.write("i want to leave india\n")
print("my new file,my new file.txt created successfully")
print("file closed successfully")
print("my new file:",os.path.getsize("my new file.txt"),"bytes")
f.close()


import os
os.remove("my new file.txt")
print("my new file.txt deleted successfully")
