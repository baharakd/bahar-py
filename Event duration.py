import math

data = [50.3, 338.4, 626.5, 959.4, 1317.9,
        1716.7, 2134.3, 2565.5, 3085.6,3626.7]


# 1- ساختن لیست Duration :
new_item = 0
duration = []
for i in range(len(data)-1):
    new_item = round(data[i+1] - data[i], 2)
    duration.append(new_item)
dur_lst = duration.copy()
print("Duration List:", dur_lst, "\n")



# 2- ساختن رشته توصیف کننده اتفاقات :
t1 = 300
t2 = 400
str_lst = []
for j in range(len(duration)):
    if duration[j] <= t1:
        duration[j] = "S"
    elif duration[j] >= t2:
        duration[j] = "L"
    else:
        duration[j] = "M"
    str_lst.append(duration[j])
str_dur = "".join(str_lst)
print("Duration String:", str_dur, "\n")



#Searching for special events like LSL,LSSL,LSSSL,LSSSSL -3.1
str_dur = "LSLLSLSSLSSSLSSSSLLSLLMSLSML"
print("There is", str_dur.count("LSL"), "LSL in duration string")
print("There is", str_dur.count("LSSL"), "LSSL in duration string")
print("There is", str_dur.count("LSSSL"), "LSSSL in duration string")
print("There is", str_dur.count("LSSSSL"), "LSSSSL in duration string")
print("\n")

# 3.2- زمان شروع و پایان هر اتفاق روی لیست data
for k in range(len(data)-1):
    print("event number", k + 1, "is", dur_lst[k], "it's begins at:", data[k], "and ends at", data[k + 1])



#3.3- مدت زمان توالی S ها
