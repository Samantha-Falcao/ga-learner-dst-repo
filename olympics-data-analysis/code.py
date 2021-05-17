# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data = pd.read_csv(path)
data.rename(columns = {'Total': 'Total_Medals'}, inplace = True)
data.head(10)

# Summer or Winter

data['Better_Event'] =np.where(data.Total_Summer > data.Total_Winter, 'Summer', (np.where(data.Total_Summer < data.Total_Winter, 'Winter', 'Both')))

better_event = data['Better_Event'].value_counts().index[0]

# Top 10
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(data.tail(1).index, inplace = True)

def top_ten(df, col):
    country_list =list(df.nlargest(10, col)['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')

print('Top 10 Summer: ', top_10_summer)
print('Top 10 winter: ', top_10_winter)
print('Top 10 overall: ', top_10)

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print('Common: ', common)

# Plotting top 10

summer_df = data[data.Country_Name.isin(top_10_summer)]
winter_df = data[data.Country_Name.isin(top_10_winter)]
top_df = data[data.Country_Name.isin(top_10)]

summer_df.plot(x = 'Country_Name', y = 'Total_Summer', kind = 'bar', legend = False)
plt.xlabel('Country')
plt.ylabel('Summer Medals')
plt.show()

winter_df.plot(x = 'Country_Name', y = 'Total_Winter', kind = 'bar', legend = False)
plt.xlabel('Country')
plt.ylabel('Winter Medals')
plt.show()

top_df.plot(x = 'Country_Name', y = 'Total_Medals', kind = 'bar', legend = False)
plt.xlabel('Country')
plt.ylabel('Total Medals')
plt.show()
# Top Performing Countries

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = round(max(summer_df['Golden_Ratio']),2)
summer_country_gold = summer_df[summer_df['Golden_Ratio'] == max(summer_df['Golden_Ratio'])]['Country_Name'].values[0]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = round(max(winter_df['Golden_Ratio']),2)
winter_country_gold = winter_df[winter_df['Golden_Ratio'] == max(winter_df['Golden_Ratio'])]['Country_Name'].values[0]

top_df['Golden_Ratio'] = top_df['Gold_Total']/summer_df['Total_Medals']
top_max_ratio = round(max(top_df['Golden_Ratio']),2)
top_country_gold = top_df[top_df['Golden_Ratio'] == max(top_df['Golden_Ratio'])]['Country_Name'].values[0]
print(top_max_ratio)
print(top_country_gold)
# Best in the world 

data_1 = data.drop(data.tail(1).index)
data_1['Total_Points'] = (3*data_1['Gold_Total']) + (2*data_1['Silver_Total']) + (data_1['Bronze_Total'])

most_points = data_1['Total_Points'].max()
best_country = data_1[data_1['Total_Points'] == most_points]['Country_Name'].values[0]

print('Best Country:',best_country, '\nMost Points:', most_points)


# Plotting the best

best = data[data['Country_Name'] == best_country][['Gold_Total', 'Silver_Total', 'Bronze_Total']]

best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()





