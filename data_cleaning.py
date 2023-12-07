import os
from pathlib import Path
import pandas as pd
import numpy as np

root = r'C:\Users\user\OneDrive - yuntech.edu.tw\文件\Python Scripts\Selenium_the_traffic_web'
year_np = np.array([])

elc_np = np.array([])
motor_np = np.array([])

concat_data = pd.DataFrame(index = None)
col_name = ['Age', 'Frequency', 'Death_toll', 'Injuries', 'Casualties']

for file in os.listdir(Path(root, 'eletronic_motor')):

    year_col = np.array([file[:3] for i in range(6)]).reshape(6,1)
    year_np = np.append(year_np, year_col)

    elc_col = np.array(['eletronic' for i in range(6)]).reshape(6,1)
    elc_np = np.append(elc_np, elc_col)
    
    data = pd.read_excel(Path(root, 'eletronic_motor', file), header = None, skiprows = 1)
    data = data.drop(0, axis = 1)
    data.columns = col_name
    
    concat_data = pd.concat([concat_data, data.iloc[1:7]], axis=0)

for file in os.listdir(Path(root, 'motor')):

    year_col = np.array([file[:3] for i in range(6)]).reshape(6,1)
    year_np = np.append(year_np, year_col)

    elc_col = np.array(['motor' for i in range(6)]).reshape(6,1)
    elc_np = np.append(elc_np, elc_col)
    
    data = pd.read_excel(Path(root, 'motor', file), header = None, skiprows = 1)
    data = data.drop(0, axis = 1)
    data.columns = col_name
    
    concat_data = pd.concat([concat_data, data.iloc[1:7]], axis=0)


concat_data['Year'] = year_np.reshape(-1, 1)
concat_data['Vehicle_type'] = elc_np.reshape(-1, 1)
concat_data = concat_data.reset_index(drop = True)
concat_data['death_rate'] = concat_data['Death_toll'] / concat_data['Frequency'] # 死亡人數 / 事故數
concat_data['injury_rate'] = concat_data['Injuries'] / concat_data['Frequency'] # 受傷人數 / 事故數
concat_data.to_csv(Path(root, 'concat_data.csv'), encoding = 'Big5', index = False)
print(concat_data)


