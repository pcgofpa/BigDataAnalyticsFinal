import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

# Create Dataframe
data = pd.read_csv('cs356_Data.csv')
county = data['county']
population = data['population']
asthma = data['asthma']
smoking = data['smoking']

data.sort_values(['asthma'], ascending=False, inplace=True)
print(data)

# Create Visualization
plt.scatter(asthma, smoking)
plt.xlabel('Asthma')
plt.ylabel('Smoking')
plt.show()
