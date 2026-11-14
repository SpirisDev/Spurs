from spurs.basics import MultiopBasic, GeneralBasic

m = MultiopBasic()
gb = GeneralBasic()

class BasicStatistics:
    def _check_data(self, data: float):
        if len(data) == 0: raise ValueError("data must not be empty")

    def mean(self, data: float):
        self._check_data(data)
        return sum(data)/len(data)

    def median(self, data: float):
        self._check_data(data)
        ordered = sorted(data)
        n = len(ordered)
        mid = n // 2
        if n % 2: return ordered[mid]
        return (ordered[mid - 1] + ordered[mid]) / 2

    def mode(self, data):
        self._check_data(data)
        counts = {}
        for value in data: counts[value] = counts.get(value, 0) + 1
        highest = max(counts.values())
        return [
            value for value, count in counts.items()
            if count == highest
        ]

    def data_range(self, data: float):
        self._check_data(data)
        return max(data)-min(data)

    def range_avg(self, data: float):
        self._check_data(data)
        return self.data_range(data)/2

    def geo_mean(self, data: float):
        self._check_data(data)
        return gb.root(m.mul(data),len(data))

    def harmonic_mean(self, data: float):
        self._check_data(data)
        rec = []
        for n in data: rec.append(1/n)
        return len(rec)/(sum(rec))

class Dispersion:
    def __init__(self):
        self.b = BasicStatistics()

    def variance(self, data: float):
        self.b._check_data(data)
        mean = self.b.mean(data)
        re = []
        for n in data:
            re.append((n-mean) ** 2)
        return sum(re)/len(data)

    def sample_variance(self, data: float):
        self.b._check_data(data)
        mean = self.b.mean(data)
        re = []
        for n in data:
            re.append((n-mean) ** 2)
        return sum(re)/(len(data)-1)

    def std_deviation(self, data):
        self.b._check_data(data)
        return gb.root(self.variance(data),2)

    def sample_std_deviation(self, data):
        self.b._check_data(data)
        return gb.root(self.sample_variance(data),2)