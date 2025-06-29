"""
Example:
    python3 tests/difference/parametric/anova.py --csv data/sample_data.csv --group-col group
"""

from typing import Dict, List
import argparse

from loaders import base_loader
from utils import result_formatter, logger

# Simple one-way ANOVA implementation (approximate)

def run(groups: Dict[str, List[float]]):
    all_data = [v for vals in groups.values() for v in vals]
    if len(groups) < 2 or not all_data:
        return {'error': 'Need at least two groups.'}
    n_total = len(all_data)
    grand_mean = sum(all_data) / n_total
    ss_between = 0.0
    ss_within = 0.0
    for vals in groups.values():
        ss_between += len(vals) * (sum(vals)/len(vals) - grand_mean) ** 2
        ss_within += sum((x - sum(vals)/len(vals)) ** 2 for x in vals)
    df_between = len(groups) - 1
    df_within = n_total - len(groups)
    ms_between = ss_between / df_between if df_between else 0
    ms_within = ss_within / df_within if df_within else 0
    f_stat = ms_between / ms_within if ms_within else 0
    return {'test': 'ANOVA', 'F': f_stat, 'df_between': df_between, 'df_within': df_within}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one-way ANOVA on CSV data")
    parser.add_argument("--csv", default="data/sample_data.csv", help="CSV file path")
    parser.add_argument("--group-col", default="group", help="Group column name")
    args = parser.parse_args()

    rows = base_loader.load_csv(args.csv)
    groups = base_loader.group_by(rows, args.group_col)
    result = run(groups)
    logger.log(result_formatter.format_result(result))


if __name__ == "__main__":
    main()
