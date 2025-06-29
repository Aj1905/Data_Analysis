import math
import csv
from statistics import mean, variance, NormalDist


def run(groups):
    data1 = groups.get('A', [])
    data2 = groups.get('B', [])
    if not data1 or not data2:
        return {'error': 'Both groups must have data.'}
    n1, n2 = len(data1), len(data2)
    mean1, mean2 = mean(data1), mean(data2)
    var1, var2 = variance(data1), variance(data2)
    se = math.sqrt(var1 / n1 + var2 / n2)
    if se == 0:
        return {'error': 'Standard error is zero.'}
    t_stat = (mean1 - mean2) / se
    df_num = (var1 / n1 + var2 / n2) ** 2
    df_den = (var1 ** 2) / ((n1 ** 2) * (n1 - 1)) + (var2 ** 2) / ((n2 ** 2) * (n2 - 1))
    df = df_num / df_den if df_den != 0 else float('inf')
    p_value = 2 * (1 - NormalDist().cdf(abs(t_stat)))
    return {
        'test': 't-test',
        't_stat': t_stat,
        'df': df,
        'p_value_approx': p_value
    }
