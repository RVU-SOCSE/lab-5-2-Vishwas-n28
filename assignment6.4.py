import pandas as pd
data=pd.Series([10,120,30,40,50] , index=['a','b','c','d','e'])

print(data)
#data manupulation using pandas

print(data[0:3])
print(data[2:])
print(data[data>20])
print(data[data<20])
print(data.mean())
print(data.median())
print(data.std())
print(data.sum())
print(data.count())
print(data.sort_values())
print(data.sort_values(ascending=False))
print(data.describe())


#accessing the values of a series using index
print(data['a'])
print(data[['a','b']])

##accessing the values based on colum names
print(data.name)
print(data.index)
print(data.values)

##head and tail 
print(data.head(2)) #if we dont give any argument it will give the first 5 rows
print(data.tail(2))



import pandas as pd

team_info = {
    'Staff_ID': ['S01', 'S02', 'S03', 'S04', 'S05'],
    'Full_Name': ['Marcus V.', 'Sarah J.', 'Kevin L.', 'Elena R.', 'Chris P.'],
    'Role': ['DevOps', 'Designer', 'DevOps', 'Manager', 'Analyst'],
    'Monthly_Pay': [6200, 5800, 6500, 7000, 5200],
    'Remote_Work': [True, False, True, False, True]
}

df = pd.DataFrame(team_info)
df.to_csv('team_roster.csv', index=False)

names_list = df['Full_Name']
third_row = df.iloc[2]
elena_pay = df.at[3, 'Monthly_Pay']

remote_total = df[df['Remote_Work'] == True]['Monthly_Pay'].sum()
top_tier = df[df['Monthly_Pay'] > 6000]
-
df['Bonus'] = df['Monthly_Pay'] * 0.10
avg_by_role = df.groupby('Role')['Monthly_Pay'].mean()

stats = df['Monthly_Pay'].describe()

print("Full DataFrame with Bonus Column:")
print(df)

print("\nAverage Pay by Role:")
print(avg_by_role)

print("\nSummary Statistics for Pay:")
print(stats)

print(f"\nTotal remote worker budget: {remote_total}")
print(f"Third person in list: {third_row['Full_Name']}")

 




