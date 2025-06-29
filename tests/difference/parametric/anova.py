from typing import Dict, List

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
