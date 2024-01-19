This is a novel approach that we developed as a scientific project. We created a GPS-based approach primarily focused on collecting robot locations using local GPS to predict their paths, ensuring collision-free navigation.

It involves the implementation of an AI-assisted N-body collision avoidance method. The main.py file contains the implementation of a deep neural network trained on specific data, as shown in the DATA.xlsx file.

The data is generated through an OCRA algorithm-based data generation process, explained in the DATA_Collection folder. The dataset used has a shape of 10,000 rows and 40 columns. The first 20 columns display the positions of 10 robots at step i, while the last 20 columns show the positions of the same 10 robots at step i+1.

The Python code is adaptable to any particular dataset by adjusting the configurations of input and output layers in the main.py file. The model is loaded in the model_loading.py file for predicting the next positions of robots.

To control the model parameters, TensorBoard can be used by executing "tensorboard --logdir=logs" in the terminal, providing a local interface for monitoring.
