"""
Example:
    python3 tests/association/nonparametric/chi2_independence.py --csv data/sample_data.csv --group-col group
"""

from typing import Dict, List
import argparse

from loaders import base_loader
from utils import result_formatter, logger

# Placeholder for Chi-square test of independence

def run(groups: Dict[str, List[float]]):
    return {'test': 'Chi-square independence', 'implemented': False}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Chi-square independence test on CSV data")
    parser.add_argument("--csv", default="data/sample_data.csv", help="CSV file path")
    parser.add_argument("--group-col", default="group", help="Group column name")
    args = parser.parse_args()

    rows = base_loader.load_csv(args.csv)
    groups = base_loader.group_by(rows, args.group_col)
    result = run(groups)
    logger.log(result_formatter.format_result(result))


if __name__ == "__main__":
    main()
