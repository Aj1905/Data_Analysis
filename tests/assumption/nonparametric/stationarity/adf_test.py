"""
Example:
    python3 tests/assumption/nonparametric/stationarity/adf_test.py data.csv value --date_col date
"""

import argparse
import sys

import pandas as pd
from statsmodels.tsa.stattools import adfuller


def load_time_series(path: str, column: str, date_col: str | None = None) -> pd.Series:
    """Read a CSV and return the specified column as a Series."""
    df = pd.read_csv(path)
    if date_col:
        df[date_col] = pd.to_datetime(df[date_col])
        df.set_index(date_col, inplace=True)
    return df[column].dropna()


def run_adf_test(series: pd.Series, maxlag: int | None = None, regression: str = 'c'):
    """Run the Augmented Dickey–Fuller test and print the result."""
    result = adfuller(series, maxlag=maxlag, regression=regression, autolag='AIC')
    print("=== Augmented Dickey–Fuller Test ===")
    print(f"Test Statistic : {result[0]:.5f}")
    print(f"p-value        : {result[1]:.5f}")
    print(f"# lags used    : {result[2]}")
    print(f"# observations : {result[3]}")
    print("Critical Values:")
    for k, v in result[4].items():
        print(f"  {k}: {v:.5f}")
    if result[1] < 0.05:
        print("\u2192 \u5e30\u7121\u4f8b\u8a34\u8a1f\uff08\u55b6\u55b6\u6839\u3042\u308a\uff09\u306f\u68c4\u5374\u3055\u308c\u3001\u7cfb\u5217\u306f\u5b9a\u5e38\u3067\u3042\u308b\u53ef\u80fd\u6027\u304c\u9ad8\u3044\u3002")
    else:
        print("\u2192 \u5e30\u7121\u4f8b\u8a34\u8a1f\u3092\u68c4\u5374\u3067\u304d\u305a\u3001\u975e\u5b9a\u5e38\u306e\u53ef\u80fd\u6027\u304c\u3042\u308b\u3002")


def main() -> None:
    parser = argparse.ArgumentParser(description="\u6642\u7cfb\u5217\u30c7\u30fc\u30bf\u306b\u5bfe\u3057ADF\u691c\u5b9a\u3092\u884c\u3044\u307e\u3059\u3002")
    parser.add_argument("csv_path", help="\u5165\u529b CSV \u30d5\u30a1\u30a4\u30eb\u30d1\u30b9")
    parser.add_argument("column", help="\u691c\u5b9a\u5bfe\u8c61\u306e\u5217\u540d")
    parser.add_argument("--date_col", default=None, help="\u65e5\u4ed8\u5217\u540d (\u7701\u7565\u53ef)")
    parser.add_argument("--maxlag", type=int, default=None, help="\u6700\u5927\u30e9\u30b0\u6570 (\u7701\u7565\u6642\u306f\u81ea\u52d5\u9078\u629e)")
    parser.add_argument("--regression", choices=['c', 'ct', 'nc'], default='c', help="\u5b9a\u6570\u9805/\u30c8\u30ec\u30f3\u30c9\u9805\u306e\u6307\u5b9a: c, ct, nc")
    args = parser.parse_args()

    try:
        series = load_time_series(args.csv_path, args.column, args.date_col)
    except Exception as e:
        print(f"\u30c7\u30fc\u30bf\u8aad\u307f\u8fbc\u307f\u30a8\u30e9\u30fc: {e}", file=sys.stderr)
        sys.exit(1)

    run_adf_test(series, maxlag=args.maxlag, regression=args.regression)


if __name__ == "__main__":
    main()
