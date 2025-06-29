"""
Example:
    python3 tests/difference/nonparametric/mann_whitney_u.py --csv data/sample_data.csv --group-col group
"""

import math
from statistics import NormalDist
import argparse

from loaders import base_loader
from utils import result_formatter, logger


def rank_data(data1, data2):
    combined = [(x, 'A') for x in data1] + [(x, 'B') for x in data2]
    combined.sort(key=lambda x: x[0])
    ranks = {}
    i = 1
    while i <= len(combined):
        val = combined[i-1][0]
        j = i
        while j <= len(combined) and combined[j-1][0] == val:
            j += 1
        avg_rank = (i + j - 1) / 2
        for k in range(i, j):
            group = combined[k-1][1]
            ranks.setdefault(group, []).append(avg_rank)
        i = j
    return ranks


def run(groups):
    data1 = groups.get('A', [])
    data2 = groups.get('B', [])
    if not data1 or not data2:
        return {'error': 'Both groups must have data.'}
    ranks = rank_data(data1, data2)
    r1 = sum(ranks.get('A', []))
    n1, n2 = len(data1), len(data2)
    u1 = r1 - n1 * (n1 + 1) / 2
    mean_u = n1 * n2 / 2
    std_u = math.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)
    z = (u1 - mean_u) / std_u if std_u != 0 else 0
    p_value = 2 * (1 - NormalDist().cdf(abs(z)))
    return {
        'test': 'Mann-Whitney U',
        'u_stat': u1,
        'z_stat': z,
        'p_value_approx': p_value
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Mann-Whitney U test on CSV data")
    parser.add_argument("--csv", default="data/sample_data.csv", help="CSV file path")
    parser.add_argument("--group-col", default="group", help="Group column name")
    args = parser.parse_args()

    rows = base_loader.load_csv(args.csv)
    groups = base_loader.group_by(rows, args.group_col)
    result = run(groups)
    logger.log(result_formatter.format_result(result))


if __name__ == "__main__":
    main()
