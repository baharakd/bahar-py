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

print("\n")

#3.3- مدت زمان توالی S ها
new_data = [200, 800, 900, 1500, 2000, 2200, 2400, 2900, 3400, 3600, 3800, 4500, 5000, 5200
            , 5400, 5600, 5800, 6500, 7000, 7200, 8000]
new_dur = [600, 100, 600, 500, 200, 200, 500, 500, 200, 200, 700, 500, 200, 200, 200, 200, 700, 500, 200, 800]
new_dur_str = "LSLLSSLLSSSLLSSSSLLSL"
s_seq = 0
for p in range(len(new_dur_str)-1):
    if new_dur_str[p] == "L" and new_dur_str[p+1] == "S" and new_dur_str[p+2] == "L":
        s_seq = new_data[p+2] - new_data[p+1]
        print("S duration in LSL is:",s_seq)
for p in range(len(new_dur_str)-1):
    if new_dur_str[p] == "L" and new_dur_str[p+1] == "S" and new_dur_str[p+2] == "S" and new_dur_str[p+3] == "L":
        s_seq = new_data[p+3] - new_data[p+1]
        print("S duration in LSSL is:",s_seq)
for p in range(len(new_dur_str)-1):
    if new_dur_str[p] == "L" and new_dur_str[p+1] == "S" and new_dur_str[p+2] == "S" and new_dur_str[p+3] == "S"\
            and new_dur_str[p+4] == "L":
        s_seq = new_data[p+4] - new_data[p+1]
        print("S duration in LSSSL is:",s_seq)
for p in range(len(new_dur_str) - 1):
    if new_dur_str[p] == "L" and new_dur_str[p + 1] == "S" and new_dur_str[p + 2] == "S" and new_dur_str[p + 3] == "S" \
            and new_dur_str[p+4] == "S" and new_dur_str[p + 5] == "L":
        s_seq = new_data[p + 5] - new_data[p + 1]
        print("S duration in LSSSSL is:", s_seq)




