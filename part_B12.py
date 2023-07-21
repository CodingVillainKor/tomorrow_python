standard_volume = 30000
volume_too_low = 10000

file_data = {"target_dates.txt": [], "target_ma.txt": []}
end_price_target_dates = []
ends = []
cumul_ends = [0]

for i in range(1, 4+1):
    file_name = "stock{}.txt".format(i)

    f = open(file_name, "r", encoding="utf-8")
    entire_txt = f.read()
    f.close()

    lines = entire_txt.split("\n")
    lines_values = lines[1:]
    dates_i = [line.split(",")[0] for line in lines_values]
    ends_i = [int(line.split(",")[4]) for line in lines_values]
    vols_i = [line.split(",")[5] for line in lines_values]
    ends += ends + ends_i
    tds_i = [d for d, v in zip(dates_i, vols_i) if int(v) > standard_volume]
    eptds_i = [e for e, v in zip(ends_i, vols_i) if int(v) > standard_volume]
    file_data["target_dates.txt"] += tds_i
    end_price_target_dates += eptds_i

file_data["target_ma.txt"] = [sum(ends[j-2:j+1])/3 for j in range(len(ends)) if j >= 2]

mean_target_end = sum(end_price_target_dates) / len(end_price_target_dates)

for name, data in file_data.items():
    f = open(name, "w", encoding="utf-8")
    for d in data:
        f.write(str(d)+"\n")
    f.close()