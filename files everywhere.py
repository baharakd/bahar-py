import glob

child_lst = []
parent_lst = []
list_of_no_child = []
list_of_no_parents=[]
num_of_no_parents = 0
list_of_files = glob.glob('./files/*.txt')
for f in list_of_files:
    child = f[8:-4]
    child_lst.append(child)
    parent = open(f).read()
    parent_lst.append(parent)

# فایلی که هیچ parent ی ندارد را بیابید

    if parent == "0":
        list_of_no_parents.append(child)
        num_of_no_parents += 1
print(num_of_no_parents, "files has no parent.")
print("list of files that has no parent:", list_of_no_parents)

#لیستی از تمامی فایل‌هایی که هیچ childی ندارد را (به صورت sort شده) در فایل no_children.txt ذخیره کنید

def difference (list1, list2):
   list_dif = [i for i in list1 + list2 if i not in list2]
   return list_dif

no_child_list = difference(child_lst,parent_lst)

no_children = open("no_children.txt", mode="a")
for i in range(len(no_child_list)):
    no_children.write(no_child_list[i])
    no_children.write("\n")

#طولانی ترین مسیر ممکن را پیدا کنید و تمام اعضایی که در مسیر آن دیده شده را در فایل longest_path.txt ذخیره کنید.


