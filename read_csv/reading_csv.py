import pandas as pd
from pandas import DataFrame

# returns the number of passegers based on age and gender
def gender_between_gender(dataframe:DataFrame,gender:str,max_age:int,min_age:int,index_age:int,index_gender:int):
    male_adult=0
    data=dataframe.values
    for i in range(len(data)):
        if min_age<=data[i][index_age]<=max_age and data[i][index_gender]==gender:
            male_adult+=1
    return male_adult

# returns dictionary satisfaction info (neutral or dissatisfied, satisfied and total interviews) in percentage and quantity
def satisfaction_measure(dataframe:DataFrame,index_satisfaction:int):
    data=dataframe.values
    data_satisfaction=[]
    neutral_or_dissatisfied_quantity=satisfied_quantity=0

    for d in data:
        if d[index_satisfaction] == 'neutral or dissatisfied':
            neutral_or_dissatisfied_quantity+=1
        if d[index_satisfaction] == 'satisfied':
            satisfied_quantity+=1
    tot = neutral_or_dissatisfied_quantity + satisfied_quantity
    satisfied_percentage = (satisfied_quantity / tot) * 100
    neutral_dissatisfied_percentage = (neutral_or_dissatisfied_quantity / tot) * 100

    return  {"total interviews":tot,'neutral or dissatisfied quantity':neutral_or_dissatisfied_quantity,'satisfied quantity':satisfied_quantity,'neutral or dissatisfied percentage': f'{neutral_dissatisfied_percentage:.2f}', 'satisfied percentage' : f"{satisfied_percentage:.2f}"}

#dataframe
df=pd.read_csv("airline/train.csv", encoding="latin1")

gender,max_age,min_age='Male',30,18

print(f'\nNumber of {gender} between {min_age} years and {max_age} years')
print(gender_between_gender(df,gender,max_age,min_age,4,2))

print('\nDictionary of information about satisfaction measure')
print(satisfaction_measure(df,24))


