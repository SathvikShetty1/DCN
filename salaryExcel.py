import pandas as pd

df=pd.read_excel(r"D:\data.xlsm")

print("First few rows:")
print(df.head())


print("\nSummary Statistics")
print(df.describe())

filtered_data=df[df['Age']>30]
print("\nFiltered data (Age>30):")
print(filtered_data)


sorted_data=df.sort_value(by='Salary',ascending=false)
print("\nSOrted data(by Salary):")
print(sorted_data)

df['Bonus']=df['Salary']*0.1
print("\nData with new column(Bonus):")
print(df)

df.excel('Output.xlsx',index=False)
print("\nData written to output.xlsx")
