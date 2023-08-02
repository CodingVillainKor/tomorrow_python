import urllib.request
text_all = urllib.request.urlopen("https://finance.naver.com/marketindex/").read().decode("cp949")

idx = text_all.find("미국 달러")
print(text_all[idx-65:idx-59])

lines = text_all.split("\n")
for l in lines:
    if "미국 달러" in l:
        print(l.split("\"")[1])
        break

for l in lines:
    if "유럽연합 유로" in l:
        print(l.split("\"")[1])
        break