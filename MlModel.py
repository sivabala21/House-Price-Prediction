import pandas
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data= pandas.read_csv("Datasets/housing2_cleaned.csv")
data.fillna(data.mean(),inplace=True)

x = data[['area','bedrooms','bathrooms','stories','parking']]
y = data['median_house_value']

xTrain,xTest,yTrain,yTest=train_test_split(x,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(xTrain,yTrain)



with open('model.pkl','wb') as file:
    pickle.dump(model,file)