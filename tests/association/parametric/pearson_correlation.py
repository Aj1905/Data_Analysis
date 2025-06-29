from typing import Dict, List
from statistics import mean


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
