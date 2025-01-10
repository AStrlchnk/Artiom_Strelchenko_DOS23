import os

os.makedirs("mydir")

os.chdir("mydir")

for filename in ["file1.txt", "file2.txt", "file3.txt"]:
    with open(filename, "w") as file:
        pass 

print("List of files in the directory 'mydir':", os.listdir("."))