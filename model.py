#Dependencies Imports
import pandas
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#csv file read and cleaned
data= pandas.read_csv("Datasets/HousePriceIndia.csv")
data.fillna(data.mean(),inplace=True)

print(data.columns)
#split data into train and test
x = data[['Bedrooms', 'Bathrooms', 'LivingArea', 'Floors', 'Views', 'Condition', 'HouseArea', 'BasementArea', 'BuiltYear', 'PostalCode', 'SchoolsNearby']]
y = data['Price']


xTrain,xTest,yTrain,yTest=train_test_split(x,y,test_size=0.2,random_state=42)
#train model using linear regression
model=LinearRegression()
model.fit(xTrain,yTrain)


#save model
with open('model.pkl','wb') as file:
    pickle.dump(model,file)