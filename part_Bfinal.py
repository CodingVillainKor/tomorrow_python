standard_volume = 30000
file_data = dict()

class StockAnalyzer:
    def __init__(self, paths):
        self.entire_data = []
        for p in paths:
            self.entire_data += self.get_file_data(p)

    @staticmethod
    def get_file_data(path):
        f = open(path, "r", encoding="utf-8")
        entire_txt = f.read()
        f.close()
        return entire_txt.split("\n")[1:]
    def get_target_dates(self, standard):
        return [d for d, v in zip(self.dates, self.vols) if int(v) > standard]

    def get_target_ma(self):
        return [sum(self.ends[j-2:j+1])/3 for j in range(len(self.ends)) if j >= 2]
    
    def get_end_price_target_dates(self, standard):
        return [e for e, v in zip(self.ends, self.vols) if int(v) > standard]
    
    @property
    def dates(self):
        return [line.split(",")[0] for line in self.entire_data]
    @property
    def ends(self):
        return [int(line.split(",")[4]) for line in self.entire_data]
    @property
    def vols(self):
        return [line.split(",")[5] for line in self.entire_data]


paths = ["stock{}.txt".format(i) for i in range(1, 4+1)]
sa = StockAnalyzer(paths)
file_data["target_dates.txt"] = sa.get_target_dates(standard_volume)
file_data["target_ma.txt"] = sa.get_target_ma()
end_price_target_dates = sa.get_end_price_target_dates(standard_volume)

mean_target_end = sum(end_price_target_dates) / len(end_price_target_dates)

for name, data in file_data.items():
    f = open(name, "w", encoding="utf-8")
    for d in data:
        f.write(str(d)+"\n")
    f.close()