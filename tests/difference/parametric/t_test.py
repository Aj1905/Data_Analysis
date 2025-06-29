"""
Example:
    python3 tests/difference/parametric/t_test.py --csv data/sample_data.csv --group-col group
"""

import math
from statistics import mean, variance, NormalDist
import argparse

from loaders import base_loader
from utils import result_formatter, logger


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


def main() -> None:
    parser = argparse.ArgumentParser(description="Run t-test on CSV data")
    parser.add_argument("--csv", default="data/sample_data.csv", help="CSV file path")
    parser.add_argument("--group-col", default="group", help="Group column name")
    args = parser.parse_args()

    data_rows = base_loader.load_csv(args.csv)
    groups = base_loader.group_by(data_rows, args.group_col)
    result = run(groups)
    logger.log(result_formatter.format_result(result))


if __name__ == "__main__":
    main()
