# فایل خروجی با اسم out_words_count.txt ایجاد کنید که تعداد کل کلمات شعر wasteland و
# تعداد کلمات بدون احتساب تکرارشان را در دو خط مجزا بنویسد

f = open('poem.txt', mode='r', encoding='utf8')
text = f.read()
num_words=0
for line in f:
    words = line.split()
    num_words+=len(words)
print(num_words)
