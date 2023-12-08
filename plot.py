import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


data = pd.read_csv(r'concat_data.csv', encoding = 'Big5')

feature_name = ['死亡比例', '受傷比例', '死傷比例']
orignal_age = list(set(data['Age']))

# 將不明、兒童的資料刪除
for i in orignal_age:
    if '不明' in i or '兒童' in i:
        data = data[data['Age'] != i]
    else:
        pass

age = list(set(data['Age']))
year = list(set(data['Year']))
vehicle_type = list(set(data['Vehicle_type']))
data = data.sort_values(by = ['Age', 'Year'])

# 如果沒有資料夾就新增
if not Path('不同年紀比較不同運具的三種feature').exists():
    Path('不同年紀比較不同運具的三種feature').mkdir()

if not Path('金字塔圖').exists():
    Path('金字塔圖').mkdir()

# 不同年紀比較不同運具的三種feature
for i in age:
    fig, ax = plt.subplots(1, 3, figsize = (15, 5))
    filter_age_data = data[data['Age'] == i]
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    for plot_number,feat in zip(ax, feature_name):
        for v in vehicle_type:
            plot_number.set_title(f'{i} {feat}')
            filter_vehicle_data = filter_age_data[filter_age_data['Vehicle_type'] == v]
            plot_number.plot(filter_vehicle_data['Year'], filter_vehicle_data[feat], label = f'{v}')
        plot_number.legend()       
    fig.savefig(Path('不同年紀比較不同運具的三種feature', f'{i}歲不同運具三種feature比較.png'))

# 不同年紀在不同年份的三種feature畫在同一張金字塔圖
for i in year:
    xtick = []
    fig, ax = plt.subplots(figsize = (12, 10))
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    plt.rcParams['axes.unicode_minus'] = False
    filter_year_data = data[data['Year'] == i]
    ax.set_title(f'{i}年人口金字塔死亡比例')
    for v in vehicle_type:
        if v == 'motor':
            filter_motor_data = filter_year_data[filter_year_data['Vehicle_type'] == v]
            ax.barh(filter_motor_data['Age'], filter_motor_data['死亡比例'], label = f'{v}', color = 'gray')
        else:
            filter_elc_data = filter_year_data[filter_year_data['Vehicle_type'] == v]
            ax.barh(filter_elc_data['Age'], filter_elc_data['死亡比例'] * (-1), label = f'{v}', color = 'green')
    org_xticks = ax.get_xticks()
    zero_index = np.where(org_xticks == 0)
    org_xticks[:zero_index[0][0]] = org_xticks[:zero_index[0][0]] * (-1)
    final_ticks = [round(i, 3) for i in org_xticks]
    ax.set_xticklabels(final_ticks)
    ax.legend()
    fig.savefig(Path('金字塔圖', f'{i}年金字塔圖.png'))





