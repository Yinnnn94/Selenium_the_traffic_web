import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'concat_data.csv', encoding = 'Big5')
age = set(data['Age'])
for i in age:
    data_age = data[data['Age'] == i]
    plt.figure()
    plt.title(i)
    plt.plot(data_age['Year'], data_age['Casualties'], label = 'Casualties')
    plt.plot(data_age['Year'], data_age['Death_toll'], label = 'Death_toll')
    plt.plot(data_age['Year'], data_age['Injuries'], label = 'Injuries')
    plt.show()