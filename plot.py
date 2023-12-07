import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'concat_data.csv', encoding = 'Big5')
age = list(set(data['Age']))
vehicle_type = list(set(data['Vehicle_type']))

for i in age:
    if '不明' in i :
        pass
    else:
        fig, ax = plt.subplots(1, 2)
        for v, plot_number in zip(vehicle_type, ax):
            filter1 = data['Age'] == i
            filter2 = data['Vehicle_type'] == v
            filter_data = data[filter1 & filter2]
            plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
            plot_number.set_title(f'{i}{v}死亡與受傷率')
            plot_number.plot(filter_data['Year'], filter_data['death_rate'], label = f'{v}死亡率')
            plot_number.legend()
        plt.show()