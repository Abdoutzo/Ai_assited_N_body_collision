This is an implementation of an AI-assited N-body collision avoidance method. The file main.py contains the the implementation of a deep neural network trained on a partcular DATA shown in the file DATA.xlsx

This DATA is generated using a DATA generaton process using OCRA algorthm. This process is explained is folder DATA_Collection.

The DATA used is the following shape : 10000rows X 40 columns. The first 20 column show the positions of 10 robots in step i, and the last 20 columns show the position of 10 robots in the step i+1.

The pyton code can be used for any particular DATASET by changing the configurations of input and oupput layers in main.py file. The model is loaded in model_loading.py file to use it to predict next robots posions.

To control the model parameters you can use TensorBoad by writing tensorboard --logdir=logs in the terminal. A local interface is shown as return.
