import glob

list_of_no_parents=[]
num_of_no_parents = 0
list_of_files = glob.glob('./files/*.txt')
for f in list_of_files:
    child = f[8:-4]
    parent = open(f).read()
    if parent == "0":
        list_of_no_parents.append(child)
        num_of_no_parents += 1
print(num_of_no_parents, "files has no parent.")
print("list of files that has no parent:", list_of_no_parents)

