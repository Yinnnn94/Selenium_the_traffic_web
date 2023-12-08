import os
from pathlib import Path
import pandas as pd
import numpy as np

root = r'C:\Users\user\OneDrive - yuntech.edu.tw\文件\Python Scripts\Selenium_the_traffic_web'
col_name = ['Age', 'Frequency', 'Death_toll', 'Injuries', 'Casualties']
concat_data = pd.DataFrame(index = None)
year_np = np.array([])
vehicle_np = np.array([])

def cleaning_data(file_name, concat_data, year_np, vehicle_np):
    for file in os.listdir(Path(root, file_name)):
        year_col = np.array([file[:3] for i in range(6)]).reshape(6,1)
        year_np = np.append(year_np, year_col)
        vehicle_col = np.array([file_name for i in range(6)]).reshape(6,1)
        vehicle_np = np.append(vehicle_np, vehicle_col)
        data = pd.read_excel(Path(root, file_name, file), header = None, skiprows = 1)
        data = data.drop(0, axis = 1)
        data.columns = col_name
        concat_data = pd.concat([concat_data, data.iloc[1:7]], axis=0)
    return concat_data, year_np, vehicle_np

elc_clean_data, elc_year, elc_np = cleaning_data('eletronic', concat_data, year_np, vehicle_np)
motor_clean_data, motor_year, motor_np = cleaning_data('motor', concat_data, year_np, vehicle_np)
year_np = np.append(elc_year, motor_year).reshape(-1,1)
vehicle_np = np.append(elc_np, motor_np).reshape(-1,1)
clean_data = pd.concat([elc_clean_data, motor_clean_data], axis = 0)

clean_data['Year'] = year_np.reshape(-1, 1)
clean_data['Vehicle_type'] = vehicle_np.reshape(-1, 1)
clean_data = clean_data.reset_index(drop = True)

clean_data['所有死傷裡面造成死亡的比例'] = clean_data['Death_toll'] / clean_data['Casualties'] # 死亡人數 / 死傷人數
clean_data['所有死傷裡面造成受傷的比例'] = clean_data['Injuries'] / clean_data['Casualties'] # 受傷人數 / 死傷人數
clean_data['有車禍但未受傷或死亡人數'] = clean_data['Frequency'] - clean_data['Casualties'] # 事件數 - 死傷人數

clean_data['死亡比例'] = clean_data['Death_toll'] / clean_data['Frequency'] # 死亡人數 / 事件數
clean_data['受傷比例'] = clean_data['Injuries'] / clean_data['Frequency'] # 受傷人數 / 事件數
clean_data['死傷比例'] = clean_data['Casualties'] / clean_data['Frequency'] # 死傷人數 / 事件數

clean_data.to_csv(Path(root, 'concat_data.csv'), encoding = 'Big5', index = False)