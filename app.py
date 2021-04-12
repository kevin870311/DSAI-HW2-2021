from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("training.csv", header=None)
price = df.iloc[1:,3]
x = df.iloc[:1487,0:3]

model = LinearRegression()
model.fit(x,price)


df2 = pd.read_csv("testing.csv", header=None)
price2 = df2.iloc[:,3]
x2 = df2.iloc[:,0:3]
x2 = np.array(x2)

predict = model.predict(x2)

l = []
a = 0
status = 0
for i in range(len(predict)-1):
    if x2[i,0] < predict[i]:     #開盤小於收盤(漲)
        a = 1
    elif x2[i,0] == predict[i]:  #開盤等於收盤(平)
        a = 0
    else:                        #開盤大於收盤(跌)
        a = -1
    
    if status == 0:
        if a == 1:
            status = 1
            l.append(1)
        elif a == 0:
            status = 0
            l.append(0)
        else:
            status = 0
            l.append(0)
    elif status == 1:
        if a == 1:
            status = 1
            l.append(0)
        elif a == 0:
            status = 1
            l.append(0)
        else:
            status = 0
            l.append(-1)

l = np.array(l)            
df = pd.DataFrame(l,columns = ["action"])       
df.to_csv("output.csv") 
            



