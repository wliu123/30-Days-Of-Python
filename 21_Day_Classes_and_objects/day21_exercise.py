# Exercises: Level 1
# Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
class Statistics:
    def __init__(self):
        pass
    def count(self, ages):
        return len(ages)
    def sum(self, ages):
        return sum(ages)
    def min(self, ages):
        return min(ages)
    def max(self, ages):
        return max(ages)
    def range(self, ages):
        return max(ages) - min(ages)
    def mean(self, ages):
        return sum(ages) / len(ages)
    def median(self, ages):
        sorted_list = sorted(ages)
        mid = len(sorted_list) // 2
        if len(sorted_list) % 2 != 0:
            return sorted_list[mid]
        else:
            return (sorted_list[mid] + sorted_list[mid+1])/2
    def mode(self, ages):
        return max(set(ages), key=ages.count)
    def std(self, ages):
        calc_mean = sum(ages) / len(ages)
        variance = sum([((each - calc_mean)**2) for each in ages]) / len(ages)
        res = variance ** 0.5
        return res
    def var(self, ages):
        calc_mean = sum(ages) / len(ages)
        variance = sum([((each - calc_mean)**2) for each in ages]) / len(ages)
        return variance

data = Statistics()

print('Count:', data.count(ages)) # 25
print('Sum: ', data.sum(ages)) # 744
print('Min: ', data.min(ages)) # 24
print('Max: ', data.max(ages)) # 38
print('Range: ', data.range(ages)) # 14
print('Mean: ', data.mean(ages)) # 30
print('Median: ', data.median(ages)) # 29
print('Mode: ', data.mode(ages)) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std(ages)) # 4.2
print('Variance: ', data.var(ages)) # 17.5