standard_volume = 30000
file_data = dict()

def get_file_data(path):
    f = open(path, "r", encoding="utf-8")
    entire_txt = f.read()
    f.close()
    return entire_txt.split("\n")[1:]

entire_data = []
for i in range(1, 4+1):
    entire_data += get_file_data("stock{}.txt".format(i))

def get_target_dates(data, standard):
    dates = [line.split(",")[0] for line in data]
    vols = [line.split(",")[5] for line in data]
    target_dates = [d for d, v in zip(dates, vols) if int(v) > standard]

    return target_dates

def get_target_ma(data):
    ends = [int(line.split(",")[4]) for line in data]
    target_ma = [sum(ends[j-2:j+1])/3 for j in range(len(ends)) if j >= 2]

    return target_ma

def get_end_price_target_dates(data, standard):
    ends = [int(line.split(",")[4]) for line in data]
    vols = [line.split(",")[5] for line in data]
    end_price_target_dates = [e for e, v in zip(ends, vols) if int(v) > standard]

    return end_price_target_dates

file_data["target_dates.txt"] = get_target_dates(entire_data, standard_volume)
file_data["target_ma.txt"] = get_target_ma(entire_data)
end_price_target_dates = get_end_price_target_dates(entire_data, standard_volume)
mean_target_end = sum(end_price_target_dates) / len(end_price_target_dates)

for name, data in file_data.items():
    f = open(name, "w", encoding="utf-8")
    for d in data:
        f.write(str(d)+"\n")
    f.close()
