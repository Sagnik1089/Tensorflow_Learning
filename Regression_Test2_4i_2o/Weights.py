#%%
import tensorflow as tf
model=tf.keras.models.load_model(r'C:\Users\Sagnik Chakraborty\Desktop\Tensorflow\Regression_Test1\regression_model_1.h5')
print("Model loaded")
#%%
weights=model.get_weights()
print(weights)
# %%