standard_volume = 30000
volume_too_low = 10000

target_dates = []
end_price_target_dates = []
ends = []
ma3_end = []
cumul_ends = [0]

for i in range(1, 4+1):
    file_name = "stock{}.txt".format(i)

    f = open(file_name, "r", encoding="utf-8")
    entire_txt = f.read()
    f.close()

    lines = entire_txt.split("\n")
    lines_values = lines[1:]
    
    for j in range(len(lines_values)):
        line = lines_values[j]
        values = line.split(",")
        date = values[0]
        start = values[1]
        high = values[2]
        low = values[3]
        end = values[4]
        volume = values[5]
        amount = values[6]
        fluc_rate = values[7]
        
        if int(volume) > standard_volume:
            print("At {}, trading volume is larger than target".format(date))
            target_dates = target_dates + [date]
            end_price_target_dates += [int(end)]
        elif int(volume) < volume_too_low:
            print("At {}, trading volume is too low".format(date))
        
        ends = ends + [int(end)]

for j in range(len(ends)):
    if j > 2:
        moving_avg = (ends[j-2] + ends[j-1] + ends[j]) / 3 
        ma3_end += [moving_avg]


mean_target_end = sum(end_price_target_dates) / len(end_price_target_dates)

dates_name = "target_dates.txt"
f = open(dates_name, "w", encoding="utf-8")
for date in target_dates:
    f.write(date)
f.close()

ma_name = "target_ma.txt"
f = open(ma_name, "w", encoding="utf-8")
for ma in ma3_end:
    f.write(str(ma))
f.close()