from keras.models import load_model
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.callbacks import TensorBoard
# Load the trained model
loaded_model = load_model('my_trained_model.h5')

scaler = MinMaxScaler(feature_range=(0, 1))
scaler_min = np.array([23, 22, 22, 22, 32, 28, 22, 22, 26, 35, 23, 32, 22, 26, 28, 22, 35, 22, 40, 26], dtype=float)
scaler_scale = np.array([19, 10, 19, 16, 10, 19, 19, 19, 16, 10, 19, 10, 19, 16, 19, 19, 10, 19, 19, 16], dtype=float)
scaler.min_ = scaler_min
scaler.scale_ = scaler_scale



# Input values for prediction
input_values = "22,3843	32,7382	24,6600	38,2227	29,7135	41,4031	35,6911	40,9185	40,0893	37,0291	41,0388	31,1813	38,3520	26,7111	34,4006	22,3383	28,4352	23,2418	25,0872	27,4677 "
values_list = [float(value.replace(',', '.')) for value in input_values.split()]
input_data = np.array(values_list).reshape(1, -1)

# Scale input data using the loaded scaler
input_data_scaled = scaler.transform(input_data)
tensorboard_callback = TensorBoard(log_dir='./logs', histogram_freq=1, write_graph=True, write_images=True)

# Make prediction
prediction = loaded_model.predict(input_data_scaled)
print(prediction)

