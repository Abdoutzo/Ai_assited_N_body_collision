from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.optimizers import Adam
from keras.losses import MeanAbsoluteError
import os
from sklearn.model_selection import StratifiedKFold
from keras.constraints import max_norm
from keras.layers import BatchNormalization
import numpy as np
from keras.utils import plot_model
from keras.callbacks import TensorBoard
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

xlsx_file = 'DATA.xlsx'
df = pd.read_excel(xlsx_file)

# Assuming the last 20 columns are the target variables
X = df.iloc[:, :-20].values
y = df.iloc[:, -20:].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit(X_train)
X_train_normalized = scaler.fit_transform(X_train)
X_test_normalized = scaler.transform(X_test)
input_size = X_train_normalized.shape[1]

model = Sequential()
model.add(Dense(20, input_dim=input_size, activation='relu'))
model.add(Dense(1050, activation='relu'))  # Increased to 512 neurons
model.add(Dense(1050, activation='relu'))  # Added layer with 256 neurons
model.add(Dense(1050, activation='relu'))  # Added layer with 128 neurons
model.add(Dense(200, activation='relu'))   # Added layer with 64 neurons
model.add(Dense(32, activation='relu'))   # Added layer with 32 neurons
model.add(Dense(16, activation='relu'))   # Added layer with 16 neurons
model.add(Dense(8, activation='relu'))    # Added layer with 8 neurons
model.add(Dense(20, activation='linear'))

tensorboard_callback = TensorBoard(log_dir='./logs', histogram_freq=1, write_graph=True, write_images=True)
# compile the keras model
optimizer = Adam(learning_rate=1)
model.compile(loss=MeanAbsoluteError(), optimizer=optimizer, metrics=['mae'])

# fit the keras model on the dataset
model.fit(X_train_normalized, y_train, epochs=250, batch_size=16, validation_data=(X_test_normalized, y_test),callbacks=[tensorboard_callback])

# Save the trained model
model.save('my_trained_model.h5')

# Evaluate the keras model on the testing dataset
_, mae = model.evaluate(X_test_normalized, y_test)  # Use normalized input for evaluation
print('Mean Absolute Error: %.2f' % mae)

input_values = "42,0000 32,0000 40,0902 37,8779 35,0902 41,5106 28,9098 41,5106 23,9098 37,8779 22,0000 32,0000 23,9098 26,1221 28,9098 22,4894 35,0902 22,4894 40,0902 26,1221 "
values_list = [float(value.replace(',', '.')) for value in input_values.split()]
input_data = np.array(values_list).reshape(1, -1)
prediction = model.predict(scaler.transform(input_data))  # Scale input data before prediction
print(prediction)
