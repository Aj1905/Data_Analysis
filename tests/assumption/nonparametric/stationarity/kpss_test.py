"""
Example:
    python3 tests/assumption/nonparametric/stationarity/kpss_test.py data.csv value --date_col date
"""

import argparse
import sys

import pandas as pd
from statsmodels.tsa.stattools import kpss


def load_time_series(path: str, column: str, date_col: str | None = None) -> pd.Series:
    """Read a CSV and return the specified column as a Series."""
    df = pd.read_csv(path)
    if date_col:
        df[date_col] = pd.to_datetime(df[date_col])
        df.set_index(date_col, inplace=True)
    return df[column].dropna()


def run_kpss_test(series: pd.Series, regression: str = 'c', nlags: str = 'auto'):
    """Run the KPSS test and print the result."""
    statistic, p_value, lags, crit_values = kpss(series, regression=regression, nlags=nlags)
    print("=== KPSS Test ===")
    print(f"Test Statistic : {statistic:.5f}")
    print(f"p-value        : {p_value:.5f}")
    print(f"# lags used    : {lags}")
    print("Critical Values:")
    for k, v in crit_values.items():
        print(f"  {k}: {v:.5f}")
    if p_value < 0.05:
        print("\u2192 \u5e30\u7121\u4f8b\u8a34\u8a1f\uff08\u5b9a\u5e38\uff09\u306f\u68c4\u5374\u3055\u308c\u3001\u975e\u5b9a\u5e38\u306e\u53ef\u80fd\u6027\u304c\u3042\u308b\u3002")
    else:
        print("\u2192 \u5e30\u7121\u4f8b\u8a34\u8a1f\u3092\u68c4\u5374\u3067\u304d\u305a\u3001\u7cfb\u5217\u306f\u5b9a\u5e38\u3067\u3042\u308b\u53ef\u80fd\u6027\u304c\u9ad8\u3044\u3002")


def main() -> None:
    parser = argparse.ArgumentParser(description="\u6642\u7cfb\u5217\u30c7\u30fc\u30bf\u306b\u5bfe\u3057KPSS\u691c\u5b9a\u3092\u884c\u3044\u307e\u3059\u3002")
    parser.add_argument("csv_path", help="\u5165\u529b CSV \u30d5\u30a1\u30a4\u30eb\u30d1\u30b9")
    parser.add_argument("column", help="\u691c\u5b9a\u5bfe\u8c61\u306e\u5217\u540d")
    parser.add_argument("--date_col", default=None, help="\u65e5\u4ed8\u5217\u540d (\u7701\u7565\u53ef)")
    parser.add_argument("--regression", choices=['c', 'ct'], default='c', help="\u30e2\u30c7\u30eb: c (\u5b9a\u5e38), ct (\u5b9a\u5e38\u30c8\u30ec\u30f3\u30c9)")
    parser.add_argument("--nlags", default='auto', help="\u4f7f\u7528\u30e9\u30b0\u6570 ('auto' \u307e\u305f\u306f\u6570\u5024)")
    args = parser.parse_args()

    try:
        series = load_time_series(args.csv_path, args.column, args.date_col)
    except Exception as e:
        print(f"\u30c7\u30fc\u30bf\u8aad\u307f\u8fbc\u307f\u30a8\u30e9\u30fc: {e}", file=sys.stderr)
        sys.exit(1)

    run_kpss_test(series, regression=args.regression, nlags=args.nlags)


if __name__ == "__main__":
    main()
