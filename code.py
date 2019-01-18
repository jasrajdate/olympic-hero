# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)

data.head()

data.rename(columns = {"Total":"Total_Medals"}, inplace = True)
data.head(10)


# --------------
#Code starts here

# data['Better_Event'] = np.where(df['Total_summer']>df['Total_summer'])

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event']) 

better_event = data['Better_Event'].value_counts().index.values[0]


# --------------
#Code starts here

top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]

# top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]


top_countries=top_countries[:-1]
def top_ten(data,col):
    country_list = list((data.nlargest(10,col)['Country_Name']))
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')
print("Top 10 Summer:\n",top_10_summer, "\n")

#Calling the function for Top 10 in Winter
top_10_winter=top_ten(top_countries,'Total_Winter')
print("Top 10 Winter:\n",top_10_winter, "\n")

#Calling the function for Top 10 in both the events
top_10=top_ten(top_countries,'Total_Medals')
print("Top 10:\n",top_10, "\n")

#Extracting common country names from all three lists
common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))

print('Common Countries :\n', common, "\n")


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]

winter_df = data[data['Country_Name'].isin(top_10_winter)]

top_df = data[data['Country_Name'].isin(top_10)]

plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'], align='center', alpha=0.5)
plt.xlabel('Country_Name')
plt.ylabel('Total_Summer')
plt.title('Summer Info')
plt.show()


plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'], align='center', alpha=0.5)
plt.xlabel('Country_Name')
plt.ylabel('Total_Winter')
plt.title('Winter Info')
plt.show()


plt.bar(top_df['Country_Name'], top_df['Total_Medals'], align='center', alpha=0.5)
plt.xlabel('Country_Name')
plt.ylabel('Total_Medals')
plt.title('Total Info')
plt.show()


top_df.head()


# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']

summer_max_ratio = summer_df['Golden_Ratio'].max()

summer_country_gold = summer_df['Country_Name'][summer_df['Golden_Ratio'] == summer_df['Golden_Ratio'].max()]

print(summer_max_ratio)
print(summer_country_gold)


winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']

winter_max_ratio = winter_df['Golden_Ratio'].max()

winter_country_gold = winter_df['Country_Name'][winter_df['Golden_Ratio'] == winter_df['Golden_Ratio'].max()]


print(winter_max_ratio)
print(winter_country_gold)


top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']

top_max_ratio = top_df['Golden_Ratio'].max()

top_country_gold = top_df['Country_Name'][top_df['Golden_Ratio'] == top_df['Golden_Ratio'].max()]


print(top_max_ratio)
print(top_country_gold)

print(data['Gold_Total'].max())



# --------------
#Code starts here
data_1 = data[:-1]
data_1.tail()

data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2+data_1['Bronze_Total']
most_points = data_1['Total_Points'].max()
print(most_points)
# data_1['Country_Name'] = data_1['Country_Name'].astype(str)

# best_country = data_1.loc[data_1['Total_Points'].argmax()]
best_country = data_1.loc[data_1['Total_Points'].idxmax(), 'Country_Name']
print(best_country)


# --------------
#Code starts here

best = data.loc[data['Country_Name']==best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar()

best.plot(kind='bar', stacked=False, figsize=(15,10))


#Changing the x-axis label
plt.xlabel('United States')

#Changing the y-axis label
plt.ylabel('Medals Tally')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)



