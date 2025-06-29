"""
Example:
    python3 tests/association/parametric/pearson_correlation.py --csv data/sample_data.csv --group-col group
"""

from typing import Dict, List
from statistics import mean
import argparse

from loaders import base_loader
from utils import result_formatter, logger


def run(groups: Dict[str, List[float]]):
    xs = groups.get('x')
    ys = groups.get('y')
    if not xs or not ys or len(xs) != len(ys):
        return {'error': 'Need paired x and y groups'}
    n = len(xs)
    mean_x, mean_y = mean(xs), mean(ys)
    num = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    den_x = sum((x - mean_x) ** 2 for x in xs)
    den_y = sum((y - mean_y) ** 2 for y in ys)
    den = (den_x * den_y) ** 0.5
    r = num / den if den else 0
    return {'test': 'Pearson correlation', 'r': r}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Pearson correlation on CSV data")
    parser.add_argument("--csv", default="data/sample_data.csv", help="CSV file path")
    parser.add_argument("--group-col", default="group", help="Group column name")
    args = parser.parse_args()

    rows = base_loader.load_csv(args.csv)
    groups = base_loader.group_by(rows, args.group_col)
    result = run(groups)
    logger.log(result_formatter.format_result(result))


if __name__ == "__main__":
    main()
