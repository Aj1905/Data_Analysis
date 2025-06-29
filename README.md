# Data_Analysis

検定スクリプトを実行してデータの性質を調べるためのリポジトリです。

## 使い方
1. `data/sample_data.csv` に検定したいデータを配置します。
2. `python3 run_all_tests.py` を実行すると `tests` 以下のスクリプトが順に実行されます。

## ディレクトリ構成
```
project_root/
├─ data/
│   ├─ database.sqlite
│   └─ sample_data.csv
├─ loaders/
│   └─ base_loader.py
├─ tests/
│   ├─ assumption/
│   │   ├─ parametric/
│   │   │   ├─ normality/
│   │   │   │   ├─ shapiro_test.py
│   │   │   │   └─ kolmogorov_smirnov.py
│   │   │   └─ homoscedasticity/
│   │   │       └─ levene_test.py
│   │   └─ nonparametric/
│   │       └─ stationarity/
│   │           ├─ adf_test.py
│   │           └─ kpss_test.py
│   ├─ difference/
│   │   ├─ parametric/
│   │   │   ├─ t_test.py
│   │   │   └─ anova.py
│   │   └─ nonparametric/
│   │       ├─ mann_whitney_u.py
│   │       └─ kruskal_wallis.py
│   ├─ association/
│   │   ├─ parametric/
│   │   │   └─ pearson_correlation.py
│   │   └─ nonparametric/
│   │       ├─ spearman_correlation.py
│   │       └─ chi2_independence.py
│   └─ goodness_of_fit/
│       └─ chi2_gof.py
├─ reports/
├─ utils/
│   ├─ result_formatter.py
│   └─ logger.py
└─ README.md
```
