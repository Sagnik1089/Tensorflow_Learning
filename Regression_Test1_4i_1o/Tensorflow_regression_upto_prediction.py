#%%
import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import os

from data_set_generation import coeff
from data_set_generation import r

print("All imported")


#%%
#Loading CSV
data=pd.read_csv(os.path.join(os.getcwd(), 'data{}.csv'.format(r)))
print("csv data loaded")

#%%
# Separate the inputs and outputs
inputs=data.iloc[:, 1:5].values
outputs=data.iloc[:, 5].values
print("Input Output Separated")
# print(inputs)

# %%
X_Train, X_Test, Y_Train, Y_Test= train_test_split(inputs,outputs,test_size=0.2,random_state=42)
print("Test-Train Splitted")

# %%
scaler=MinMaxScaler()
X_Train_scaled=scaler.fit_transform(X_Train)
X_Test_scaled=scaler.fit_transform(X_Test)
print("Input Scaled")

#%%
# Model Architechture
model= tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1)
])
print("Model Defined")

# %%
# Compiling Model
model.compile(optimizer='adam', loss='mean_squared_error')
print("Model Compiled!")

#%%
# Training
model.fit(X_Train_scaled, Y_Train, epochs=10, batch_size=32, verbose=1)
print("Model Trained!")

#%%
#Evaluate the model
loss= model.evaluate(X_Test_scaled, Y_Test, verbose=1)
print(f"Test Loss: {loss}")


#%%
# Prediction
print("Start Prediction: ")
pred_inp=input("Enter 4 number separated with , : " )
values=pred_inp.split(',')
for ind, i in enumerate(values):
    values[ind]=int(i)
new_data=pd.DataFrame([values], columns=['a','b','c','d'])
new_data_scaled=scaler.transform(new_data)
prediction=model.predict(new_data_scaled)[0][0]

calculated=(coeff[0]*values[0])-(coeff[1]*values[1])+(coeff[2]*values[2])-(coeff[3]*values[3])  

print("Calculated: {}\n Predicted: {}".format(calculated, prediction))
#%%
# saving the model
model.save(os.path.join(os.getcwd(),'Regression_Model_4i_1o.h5'))