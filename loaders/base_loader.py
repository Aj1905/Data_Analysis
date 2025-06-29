import csv
from typing import Dict, List

try:
    import pandas as pd
except ImportError:  # pragma: no cover - pandas might not be installed
    pd = None


def load_csv(path: str):
    """Load CSV data.

    If pandas is available, return a pandas.DataFrame. Otherwise return a list
    of dict rows.
    """
    if pd is not None:
        return pd.read_csv(path)
    rows = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def group_by(data, key: str) -> Dict[str, List[float]]:
    """Group loaded rows by key and cast 'value' column to float."""
    groups: Dict[str, List[float]] = {}
    for row in data:
        group = row.get(key)
        value = float(row.get('value', 0))
        groups.setdefault(group, []).append(value)
    return groups
