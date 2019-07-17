import datetime
import re

sub_txt = open("subtitle.srt", mode="r", encoding="utf-8").read()
sections = sub_txt.split("\n\n")



def convert_time(input_time):
    """
    add 5 second to the input time and returns the new time
    :param t1:
    :return:
    """
    delta = datetime.timedelta(seconds=5)
    h = int(input_time[0:2])
    m = int(input_time[3:5])
    s = int(input_time[6:8])
    ms = input_time[9:]
    t1 = datetime.datetime(1900, 1, 1, h, m, s)
    t2 = t1 + delta
    t3 = t2.time()
    new_time = str(t3) + "," + ms
    return new_time


def make_new_time(time1, time2):
    srttime = time1 + " --> " + time2
    return srttime


def join_with_content(line0, line1, line2, line3):
    srt_lines_list = []
    srt_lines_list[0] = line0
    srt_lines_list[1] = line1
    srt_lines_list[2] = line2
    srt_lines_list[3] = line3
    return srt_lines_list


new_times_list = []
for i in range(len(sections)):
    line = sections[i].split("\n")
    for j in range(len(line)):
        prime_times = line[1]
        beginning_t = prime_times[0:11]
        end_t = prime_times[17:28]
        new_b_t = convert_time(beginning_t)
        new_e_t = convert_time(end_t)
        new_times_srtformat = make_new_time(new_b_t, new_e_t)
        new_times_list.append(new_times_srtformat)

        # new_srtlist_items = join_with_content(line[0],new_times_srtformat,line[2],line[3])
        # appent to new_subtitle.srt file
new_sub =  open("new_subtitle.srt", mode="a")
for f in range(len(sections)):
    text = sections[f]
    for k in range(len(new_times_list)):
        rep = new_times_list[k]
        pat = "\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}"
        new_text = re.sub(pat, rep, text)
        #new_sub.write(new_text)




print(new_times_list)
print(sections)
